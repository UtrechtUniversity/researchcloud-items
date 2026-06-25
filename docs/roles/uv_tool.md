# Role uv_tool
[back to index](../index.md#Roles)

## Summary

Installs python-based applications globally (for all users on a machine) using the `uv tool`. `uv` is an extremely fast Python version, package, and project manager. Applications will be installed by default in `/usr/local/uu-pip`. All users can use the installed applications. The application location will be automatically added to users' path.

## Requires

* Debian-based system
* RHEL-based system

## Description
This role:

- Installs desired Python packages globally for all users using the `uv tool` command.
- Adds the configured installation directory to each user's `$PATH` by placing a script in `/etc/profile.d.`
- Enables the installation of a specific Python version to a shared directory for all users, and uses that Python version for subsequent `uv tool` commands.

## Variables

- `uv_tool_package`: String. Required. The package to install. Example: `ibridges`.
- `uv_tool_extra_packages`: List. Optional. Additional dependencies to include.
- `uv_tool_requirements`: String. Path to a requirements file containing multiple dependencies.
- `uv_tool_location`: String. The installation directory. Default: `/usr/local/uu-pip`.
- `uv_tool_profile`: String. Script name placed in `/etc/profile.d/` to configure global paths. Default: `uv-tool-config.sh`.
- `uv_tool_options`: Dictionary. Optional extra arguments passed to the `uv tool` install command. See [uv tool docs](https://docs.astral.sh/uv/guides/tools/).
- `uv_tool_force`: Boolean. Force the installation (e.g., overwrite existing). Default: `true`.
- `uv_tool_python_version`: String. Optional. Specifies a Python version to be installed using `uv install python`. If set, this Python version will be used by `uv tool` in subsequent commands.
- `uv_tool_python_install_dir`: String. Directory where the selected Python version is installed. Default: `/usr/local/uu/share/uv/python`.
- `uv_tool_python_bin_dir`: String. Directory containing the binaries (e.g., `python3`, `uv`) for the installed Python version. Default: `/usr/local/uu/share/uv/python/bin`.

## See also

- [Role pipx_install_systemwide](pipx_install_systemwide.md)

## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
