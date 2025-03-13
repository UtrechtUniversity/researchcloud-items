# Role uv
[back to index](../index.md#Roles)

## Summary

`uv` is an extremely fast Python version, package and project manager, written in Rust.

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

- `uv_vens`: List of dicts describing virtual environments to be initialized with `uv`. Each item in the dict is expected to contain a `python` and `path` attribute: the former determines which Python verison to use for the venv, while the latter is the location of the venv. Example: `{ path: '/tmp/foo', python: '3.11' }`. __Note__: Python versions are installed if necessary.
- `uv_python_versions`: List of strings of python versions to be installed with `uv`. For example: `[ '3.11', '3.12.3' ]`.
- `uv_become`: Boolean. Whether to excute UV tasks (installation of Python versions and creation of venvs) as a different (non-root) user. Default: `false`.
- `uv_become_user`: String. If `uv_become` is set to `true`, which user should the tasks be executed as? E.g. `www-data`. Default: `root`.

## See also

- [pipx_install_systemwide role](./pipx_install_systemwide.md)

## History
2024-2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
