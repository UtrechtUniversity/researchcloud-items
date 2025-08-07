# Role openvscodeserver
[back to index](../index.md#Roles)

## Summary

This role installs [OpenVSCode Server](https://github.com/gitpod-io/openvscode-server), a webapplication that is a completely open source version of the server version of VSCode. It installs only the application, not a webserver/proxy or a system service to run it (you can do this using e.g. the [jupyterhub standalone role](./jupyterhub_standalone_proxy.md), as the [OpenVSCode Server component](../playbooks/openvscodeserver.md) does).

By default, the latest archive from the OpenVSCode server GitHub releases is fetched.

## Variables

- `openvscodeserver_dir`: String. Location where openvscode should be installed. Default: `/opt/openvscode-server`.
- `openvscodeserver_user`: String. User which should own the openvsode installation dir and files. Default: `root`.
- `openvscodeserver_group`: String. Group which should own the openvsode installation dir and files. Default: `root`.
- `openvscodeserver_version`: String. Specific version which should be fetched. Should correspond to one of the version string from the [OpenVSCode GitHub releases](https://github.com/gitpod-io/openvscode-server/releases/), e.g. `v1.102.3`. Default: `""` (which means the latest version will be fetched).
- `openvscodeserver_arch`: String. Architecture for which openvscode should be dowloaded. Should correspond to the architecture part of the download URLs in the [GitHub releases](https://github.com/gitpod-io/openvscode-server/releases/), e.g. `arm64`. Defaults to `x64`, or the value of the `ansible_architecure` fact if not on an `x64` machine.

## See also

- Role [jupyterhub_standalone_proxy](./jupyterhub_standalone_proxy.md)
- Playbook [openvscodeserver](../playbooks/openvscodeserver.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
