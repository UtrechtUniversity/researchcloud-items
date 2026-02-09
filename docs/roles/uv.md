# Role uv
[back to index](../index.md#Roles)

## Summary

`uv` is an extremely fast Python version, package and project manager, written in Rust. This role:

1. Installs `uv` (if it is not already present).
2. Installs desired versions of python with `uv`.
3. Creates virtual envs with specified python versions.

Note that the SRC-External component, which is executed on most if not all workspaces, already installs `uv` (as of February 2025). Actual installation of `uv` is therefore skipped by this role to save time, unless a special variable is toggled (see below).

## Requires
* Debian-based system

## Description

This role will install `uv` using `pipx`, to the default location defined by the [pipx role](./pipx_install_systemwide.md). A link to the `uv` binary installed by `pipx` is placed in `/usr/local/bin/`, so `uv` is on the PATH for each user.

Aditionally, a script `/usr/local/bin/uv_pip` is installed, which is essentially an alias for `uv pip`. This is for convenience of use in Ansible playbook: it e.g. allows passing `uv_pip` as the executable for a call to Ansible's [pip module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/pip_module.html).

The role also supports creating venvs and installing desired Python versions (see below).

The role will set a fact `uv_python_paths`, which contains a dict containing the location of the python interpreter for each requested versions. For example:

```
uv_python_paths: {
    '3.11': '/root/.local/share/uv/cpython-xxxxx/bin/python3'
}
```

## Variables

- `uv_vens`: List of dicts describing virtual environments to be initialized with `uv`. Each item in the dict is expected to contain a `path` attribute: specifying the location of the venv. You can also specify the `python` attribute to install a specific python version and use it with the venv. If you want to default to the system python, don't set the `python` attribute, and instead set the `python_preference` attribute to `'system'` (see `uv venv`'s `--python-preference` option.) Examples: `{ path: '/tmp/foo', python: '3.11' }`, or `{ path: '/tmp/foo', python_preference: 'system' }`.
- `uv_python_versions`: List of strings of python versions to be installed with `uv`. For example: `[ '3.11', '3.12.3' ]`.
- `uv_become`: Boolean. Whether to excute UV tasks (installation of Python versions and creation of venvs) as a different (non-root) user. Default: `false`.
- `uv_become_user`: String. If `uv_become` is set to `true`, which user should the tasks be executed as? E.g. `www-data`. Default: `root`.
- `uv_force_install`: Boolean. By default it is assumed that `uv` is already present on the system. Setting this variable to `true` will force-install it. Default: `false`.

## See also

- [pipx_install_systemwide role](./pipx_install_systemwide.md)

## History
2024-2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
