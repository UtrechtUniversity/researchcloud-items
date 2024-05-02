# Playbook python_workbench
[back to index](../index.md#Playbooks)

## Summary
Installs a Python development environment equiped with 
*[pyenv](https://pypi.org/project/pyenv/)* 
to allow the user to select an arbitrary Python version and
*[poetry](https://pypi.org/project/poetry/)* 
to facilitate Python module dependency management.
*[miniconda](https://docs.anaconda.com/free/miniconda/index.html)* 
to facilitate general dependency management.

## Requires
Ubuntu .

## Description
The Linux distribution influences which Python3 and pip3 versions are installed system-wide. Users should not install python packages using the system python interpreter, since this may break system packages. This component therefore installs `pyenv` and via the `runonce` role, so that each user on the system can manage their own Python environment. `pyenv` and `poetry` are installed (in userspace) the first time the user logs in.

For additional development convenience, `poetry` and `miniconda` are also intalled on a per-user basis. If users want to use `miniconda`, they have to manually run `conda init` in their shell (this is not done by default, because it may interfere with users' workflows if they do not want to use `conda`).

## Variables

- `default_python_version`: String. The version of Python to be automatically installed for each in user via `pyenv`, at first login. This version is also set as the default version for that user (with `pyenv global`). If this parameter is omitted or set to `system`, `pyenv` will not install a specific version but install use the system's python version by default . If this parameter is set to `system-latest`, the latest version of Python available from `apt` will be fetched and set as `pyenv`'s global version for each user. Default: `system-latest`.

## See also

- role [runonce](../roles/runonce.md)
- role [pyenv](../roles/pyenv.md)
- role [runonce](../roles/poetry.md)
- role [miniconda](../roles/miniconda.md)

## History
2021-2024 Written by Ton Smeele and Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
