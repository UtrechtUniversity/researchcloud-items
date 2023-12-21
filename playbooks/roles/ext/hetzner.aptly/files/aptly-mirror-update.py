#!/usr/bin/env python3

# Copyright (C) 2023 Hetzner Cloud GmbH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import datetime
import http.client as http_client
import json
import logging
import os
import sys
import time
from enum import Enum

import requests
import yaml

if sys.version_info < (3, 10):
    sys.exit("Python 3.10 or later is required.\n")


class TaskState(Enum):
    """
    These values have been reverse-engineered from the aptly source code.
    """

    IDLE = 0
    RUNNING = 1
    SUCCEEDED = 2
    FAILED = 3


class AptlyClient:
    """
    Helper class which calls the Aptly API.
    """

    def __init__(self, api_url: str = "http://localhost:9091/api"):
        self.api_url = api_url
        self.headers = {"Content-Type": "application/json"}

    def get(self, endpoint, params: dict = {}, headers: dict = None):
        headers = self.headers if headers is None else headers
        return requests.get(
            self.api_url + endpoint, params=params, headers=headers
        ).json()

    def post(self, endpoint, payload="", params: dict = {}, headers: dict = None):
        headers = self.headers if headers is None else headers
        return requests.post(
            self.api_url + endpoint, params=params, data=payload, headers=headers
        ).json()

    def delete(self, endpoint, params: dict = {}, headers: dict = None):
        headers = self.headers if headers is None else headers
        return requests.delete(
            self.api_url + endpoint, params=params, headers=headers
        ).json()

    def put(self, endpoint, payload="", params: dict = {}, headers: dict = None):
        headers = self.headers if headers is None else headers
        return requests.put(
            self.api_url + endpoint, params=params, data=payload, headers=headers
        ).json()

    def get_task_state(self, task_id):
        return TaskState(self.get(f"/tasks/{task_id}")["State"])

    def wait_for_task(self, task_id):
        while True:
            state = self.get_task_state(task_id)
            match state:
                case TaskState.SUCCEEDED:
                    break
                case TaskState.FAILED:
                    raise ValueError("Task failed", task_id)
                case TaskState.IDLE | TaskState.RUNNING:
                    time.sleep(10)
                case _:
                    raise ValueError("Undefined task state")


class Mirror:
    def __init__(self, client, mirror):
        self.client = client
        self.mirror = mirror

    def update(self, async_run: bool = True, wait: bool = True):
        print(
            f"Update mirror {self.mirror} {'asynchronous' if async_run else 'synchronous'}"
        )
        update_mirror_task = self.client.put(
            endpoint=f"/mirrors/{self.mirror}", params={"_async": async_run}, headers={}
        )
        if async_run and wait:
            self.client.wait_for_task(update_mirror_task["ID"])


class Snapshot:
    def __init__(self, client, snapshot):
        self.client = client
        self.snapshot = snapshot

    def check_if_exists(self):
        try:
            return next(
                item
                for item in self.client.get("/snapshots")
                if item.get("Name") == self.snapshot
            )
        except StopIteration:
            return False

    def create_from_mirror(self, mirror, async_run: bool = True, wait: bool = True):
        print(f"Create snapshot {self.snapshot} from mirror {mirror}")
        create_snapshot_task = self.client.post(
            endpoint=f"/mirrors/{mirror}/snapshots",
            payload=json.dumps({"Name": self.snapshot}),
            params={"_async": async_run},
        )
        if async_run and wait:
            self.client.wait_for_task(create_snapshot_task["ID"])

    def delete(self, async_run: bool = True, wait: bool = True):
        print(f"Delete snapshot {self.snapshot}")
        delete_snapshot_task = self.client.delete(
            endpoint=f"/snapshots/{self.snapshot}",
            headers={},
            params={"_async": async_run},
        )
        if async_run and wait:
            self.client.wait_for_task(delete_snapshot_task["ID"])

    def rename(self, new_name, async_run: bool = True, wait: bool = True):
        print(f"Rename Snapshot {self.snapshot} to {new_name}")
        rename_snapshot_task = self.client.put(
            endpoint=f"/snapshots/{self.snapshot}",
            params={"Name": new_name, "_async": async_run},
            headers={},
        )
        if async_run and wait:
            self.client.wait_for_task(rename_snapshot_task["ID"])

    def merge(
        self,
        snapshots: list[str],
        package_refs: list[str],
        async_run: bool = True,
        wait: bool = True,
    ):
        print(f'Create snapshot {self.snapshot} from snapshots {",".join(snapshots)}')
        payload = {
            "Name": self.snapshot,
            "SourceSnapshots": snapshots,
            "Description": "Merged from snapshots",
            "PackageRefs": package_refs,
        }

        merge_snapshot_task = self.client.post(
            endpoint="/snapshots",
            payload=json.dumps(payload),
            params={"_async": async_run},
        )
        if async_run and wait:
            self.client.wait_for_task(merge_snapshot_task["ID"])


class Publish:
    def __init__(self, client):
        self.client = client

    def get(self):
        return self.client.get(endpoint="/publish", headers={})

    def check_if_exists(self, name, prefix="."):
        try:
            return next(
                item for item in self.get() if item.get("Path") == f"{prefix}/{name}"
            )
        except StopIteration:
            return False

    def create_from_snapshot(
        self,
        sources: list[dict],
        distribution,
        origin="",
        label="",
        architectures: list[str] = [],
        prefix=".",
        async_run: bool = True,
        wait: bool = True,
    ):
        print(
            f"Publish {distribution} with"
            f'{"default prefix" if prefix == "." else f"prefix {prefix}"}'
        )

        endpoint = "/publish" if prefix == "." else f"/publish/{prefix}"
        payload = {
            "SourceKind": "snapshot",
            "Sources": sources,
            "Distribution": distribution,
            "Label": label,
            "Origin": origin,
            "Architectures": architectures,
        }

        publish_from_snapshot_task = self.client.post(
            endpoint=endpoint, payload=json.dumps(payload), params={"_async": async_run}
        )
        if async_run and wait:
            self.client.wait_for_task(publish_from_snapshot_task["ID"])

    def switch_snapshot(
        self,
        snapshots: list[dict],
        prefix=".",
        distribution="",
        force_overwrite: bool = True,
        async_run: bool = True,
        wait: bool = True,
    ):
        print(
            f"Publish new snapshots for {distribution} with"
            f'{"default prefix" if prefix == "." else f"prefix {prefix}"}'
        )

        endpoint = f"/publish/{prefix}/{distribution}"
        payload = {"ForceOverwrite": force_overwrite, "Snapshots": snapshots}

        switch_snapshot_task = self.client.put(
            endpoint=endpoint, payload=json.dumps(payload), params={"_async": async_run}
        )
        if async_run and wait:
            self.client.wait_for_task(switch_snapshot_task["ID"])


def get_arguments():
    parser = argparse.ArgumentParser(
        description="""
        Update a specific mirror and publish it automatically.
        If the mirror is a children, it will only update the mirror but not publish it.
        """
    )
    parser.add_argument(
        "mirror_name", action="store", type=str, help="Name of the mirror used in aptly"
    )
    parser.add_argument(
        "--api-url",
        action="store",
        type=str,
        help="API URL of Aptly (default http://localhost:9091/api)",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    parser.add_argument(
        "--disable_async",
        action="store_false",
        help="Disable asynchronous scheduling (not recommended)",
    )
    return parser.parse_args()


def publish_mirror(client, mirror_name, mirror_config, current_day, async_run: bool):
    publish = Publish(client)
    distribution = mirror_config.get("mirror_distribution")
    prefix = mirror_config.get("mirror_prefix")

    if publish.check_if_exists(name=distribution, prefix=prefix):
        sources = next(
            item.get("Sources")
            for item in publish.get()
            if item.get("Path") == f"{prefix}/{distribution}"
        )
        for source in sources:
            source |= {
                "Name": f"{mirror_name}-{current_day}",
                "Component": source.get("Component"),
            }

        publish.switch_snapshot(
            snapshots=sources,
            prefix=prefix,
            distribution=distribution,
            async_run=async_run,
        )
    else:
        publish.create_from_snapshot(
            sources=[{"Name": f"{mirror_name}-{current_day}"}],
            distribution=mirror_config.get("mirror_distribution"),
            origin=mirror_config.get("mirror_origin"),
            label=mirror_config.get("mirror_label"),
            prefix=mirror_config.get("mirror_prefix"),
            async_run=async_run,
        )


def mirror_update_and_snapshot(client, mirror_name, current_day, async_run: bool):
    mirror = Mirror(client=client, mirror=mirror_name)
    mirror.update(async_run=async_run)

    snapshot_name = f"{mirror_name}-{current_day}"
    snapshot = Snapshot(client, snapshot_name)
    if next(
        (
            item
            for item in client.get(endpoint="/snapshots", headers={})
            if item.get("Name") == snapshot_name
        ),
        None,
    ):
        snapshot.rename(new_name=f"{snapshot_name}-old")
        snapshot.create_from_mirror(mirror=mirror_name, async_run=async_run)
    else:
        snapshot.create_from_mirror(mirror=mirror_name, async_run=async_run)


def main():
    args = get_arguments()
    logging.basicConfig()

    if args.debug:
        http_client.HTTPConnection.debuglevel = 1
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    mirror_name = args.mirror_name
    mirror_api_url = args.api_url or os.getenv(
        "APTLY_MIRROR_API_URL", "http://localhost:9091/api"
    )
    mirror_async = args.disable_async or True

    client = AptlyClient(mirror_api_url)

    current_day = f"day{datetime.datetime.today().weekday()}"
    with open(f"/etc/aptly/mirror/{mirror_name}.conf.yaml") as stream:
        print("Read mirror configuration")
        mirror_config = yaml.safe_load(stream)

    if mirror_config.get("mirror_childrens"):
        for children_mirror_name in mirror_config.get("mirror_childrens"):
            with open(f"/etc/aptly/mirror/{children_mirror_name}.conf.yaml") as stream:
                children_mirror_config = yaml.safe_load(stream)
            if children_mirror_config.get("mirror_parent") != mirror_name:
                raise ValueError(
                    f"Children mirror {children_mirror_name} is not the parent of {mirror_name}"
                )

            mirror_update_and_snapshot(
                client, children_mirror_name, current_day, mirror_async
            )

        parent_snapshot_name = f"{mirror_name}-{current_day}"
        parent_snapshot = Snapshot(client, parent_snapshot_name)
        if parent_snapshot.check_if_exists():
            parent_snapshot.rename(new_name=f"{parent_snapshot_name}-old")

        snapshots = []
        for snapshot in mirror_config.get("mirror_childrens"):
            snapshots.append(f"{snapshot}-{current_day}")

        packages = []
        for snapshot in snapshots:
            packages.extend(
                client.get(endpoint=f"/snapshots/{snapshot}/packages", headers={})
            )

        parent_snapshot.merge(snapshots=snapshots, package_refs=packages)

        print("Switch publish to new snapshot")
        publish_mirror(client, mirror_name, mirror_config, current_day, mirror_async)

        print("Delete all old snapshots")
        old_snapshot = Snapshot(client, f"{parent_snapshot_name}-old")
        if old_snapshot.check_if_exists():
            old_snapshot.delete()
        for children_mirror_name in mirror_config.get("mirror_childrens"):
            snapshot = Snapshot(client, f"{children_mirror_name}-{current_day}-old")
            if snapshot.check_if_exists():
                snapshot.delete()

    elif mirror_config.get("mirror_parent"):
        mirror = Mirror(client=client, mirror=mirror_name)
        mirror.update(async_run=mirror_async)
    else:
        mirror_update_and_snapshot(client, mirror_name, current_day, mirror_async)
        publish_mirror(client, mirror_name, mirror_config, current_day, mirror_async)
        old_snapshot = Snapshot(client, f"{mirror_name}-{current_day}-old")
        if old_snapshot.check_if_exists():
            old_snapshot.delete()


if __name__ == "__main__":
    main()
