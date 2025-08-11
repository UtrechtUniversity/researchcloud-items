# Role openrefine
[back to index](../index.md#Roles)

## Summary

This role installs [OpenRefine]https://openrefine.org/), an open-source web application for data cleanup and transformation to other formats, an activity commonly known as data wrangling. It installs only the application, not a webserver/proxy or a system service to run it (you can do this using e.g. the [jupyterhub standalone role](./jupyterhub_standalone_proxy.md), as the [OpenRefine Server component](../playbooks/openrefine.md) does).

## Description

The role:

- Downloads OpenRefine from GitHub (by default the latest version is fetched, but see the `openrefine_version` variable below).
- Places it in `openrefine_dir` (see below).
- Installs any desired extensions by downloading and unarchiving them to the `webapp/extensions` directory inside `openrefine_dir`.
- Sets the `openrefine_cmd_path` fact to a path to the OpenRefine executable.
- Sets the `openrefine_icon_path` fact to a path pointing at the OpenRefine logo.

## Variables

- `openrefine_dir`: String. Location where openrefine should be installed. Default: `/opt/openrefine-server`.
- `openrefine_user`: String. User which should own the openvsode installation dir and files. Default: `root`.
- `openrefine_group`: String. Group which should own the openvsode installation dir and files. Default: `root`.
- `openrefine_version`: String. Specific version which should be fetched. Should correspond to one of the version string from the [openrefine GitHub releases](https://github.com/OpenRefine/OpenRefine/releases/), e.g. `3.9.3`. Default: `""` (which means the latest version will be fetched).
- `openrefine_extensions`. Optional. List. A list of dictionaries specifying OpenRefine extensions that should be installed. Dictionaries should look as follows:

```yaml
roles:
- role: openrefine
    vars:
    openrefine_extensions:
        - name: file-extensions # name of archive after extraction
          get_latest: true # whether to get the latest version of the extension from github; if so, set `url` to the appropriate URL (see below)
          url: https://api.github.com/repos/OpenRefine/FilesExtension/releases/latest # this is to grab the latest version from github; specify a direct URL to an archive if `get_latest` ist false.
          ext: .zip # the file extension of the downloaded archive
```

## See also

- Role [jupyterhub_standalone_proxy](./jupyterhub_standalone_proxy.md)
- Playbook [openrefine](../playbooks/openrefine.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
