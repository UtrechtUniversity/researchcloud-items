# Playbook Custom Packages
[back to index](../index.md#Playbooks)

## Summary

This component serves three purposes:

1. Download projects (see below for what counts as a 'project')
2. Automatically detect their dependencies
3. Install the dependencies into separate environments
3. Create [Jupyter kernels](https://docs.jupyter.org/en/stable/projects/kernels.html) for these environments

This means a user can create a workspace, provide a list of URLs/project identifiers, and a workspace will be created that contains their projects, including Notebooks, with pre-created environments in which the dependencies are already installed. This allows easy reproducibility, and prevents users from having to re-install projects and dependencies every time they re-create a workspace.

Catalog items can set the `custom_packages_projects` [parameter](#parameters) to 'Interactive' to let users provide URLs/project identifiers in the last step of workspace creation.

Please note that the created environments will be read-only (unless users have `sudo` rights).

### Supported projects

A project can be either a git repo, or a Dataverse or Zenodo project. We can specify either direct URLs, or [DOIs](https://www.doi.org/) (or Dataverse or Zenodo identifiers) pointing at one of the former.

Users can specify a specific version (e.g. git tag, brach or commit) of a project by adding `@myversion` after a project identifier. For instance: `https://github.com/binder-examples/conda.git@nbgitpuller`.

See [here](https://github.com/UtrechtUniversity/repo2kernel/blob/main/README.md#supported-projects) for supported languages/dependency types.

## Requirements

- Debian/Ubuntu workspace
- [Jupyter](./jupyterhub.md) installed (optionally; to use the created kernels)

## Description

This component:

1. Install `repo2kernel` and its dependencies. It will be added to `PATH` so users can also use `repo2kernel` after the workspace is created. 
  * this includes `miniconda`, `julia`, `uv`
1. Fetches the determined projects
2. Creates environments for them in the location specified by the `custom_packages_env_dir` [parameter](#parameters)
3. Creates Jupyter kernels for these environments that are installed 'globally' (i.e. all Jupyter users can find the kernels)

This component uses the [repo2kernel](https://github.com/UtrechtUniversity/repo2kernel) utility. This is broadly compatible with Jupyter's [Binder](https://jupyter.org/binder), so that any projects that can be launched with Binder can most likely also be resolved by `repo2kernel`.

### Downloading projects

Downloaded projects will by default will stored in the directory specified by the `custom_packages_code_dir` [parameter](parameter). Each project will be stored in its own folder, which will receive a name that is based on the provided project identifier. For instance, if a DOI was provided, the directory name will be the DOI (with certain disallowed characters removed). If a URL to a git repo was provided, e.g. `https://github.com/UtrechtUniversity/repo2kernel.git` the name of the project's directory will be `repo2kernel`.

Users can specify a specific version (e.g. git tag, brach or commit) of a project by adding `@myversion` after a project identifier. For instance: `https://github.com/binder-examples/conda.git@nbgitpuller` will fetch the `nbgitpuller`.

### Using this component without Jupyter 

The installed environments can also be used without Jupyter by setting the `custom_packages_create_kernels` [parameter](#parameter) to `false`. Naturally, projects will be downloaded as normal, and the created dependency environments can be used manually:

- For Julia projects, the installed Julia packages will automatically be added to the `JULIA_DEPOT_PATH`.
- For Python projects, users can activate the created virtual environments (under `{{custom_packages_env_dir}}/python`).
- For Conda and R projects, users can activate the created `conda` environments (under `{{custom_packages_env_dir}}/conda`).

### Error handling

It is possible that `repo2kernel` fails to create the required dependency environments, or to install a kernel for it. In that case, the component will not fail, so the workspace is still created. Debug output for `repo2kernel` is saved in each downloaded project's folder, by default in `/local-share/<project_name>/repo2kernel.log`.

## Parameters

- `custom_packages_install_uv`: Boolean. Whether the component should attempt to install `uv` (not needed if already installed). Default: `true`.
- `custom_packages_install_conda`: Boolean. Whether the component should attempt to install conda (not needed if already installed). Default: `true`.
- `custom_packages_install_julia`: Boolean. Whether the component should attempt to install julia (not needed if already installed). Default: `true`.
- `custom_packages_projects`: String. Comma-separated list of project identifiers, the dependencies of which will be installed into separate environments. Can be git repo URLs, Zenodo or Dataverse URLs, or DOIs pointing to the former. Users can specify a specific version (e.g. git tag, brach or commit) of a project by adding `@myversion` after a project identifier. For instance: `https://github.com/binder-examples/conda.git@nbgitpuller`.
- `custom_packages_extra_envs`: String. Comma-separated list of extra environments that should be created. Provide the language name and optionally a version. For example: `julia 1.12, python 3` will install an empty (no additional dependencies) julia version 1.12 kernel, and an emtpy python version 3 kernel.
- `custom_packages_code_dir`: String. Path where the specified projects should be downloaded to. Default: `/local-share/projects`.
- `custom_packages_env_dir`: String. Path where the newly created environments will be stored. Default: `/usr/local/uu/env`.
- `custom_packages_group`: String. Group that will be used for group-ownership of the code and environment paths. Default: `root`.
- `custom_packages_create_kernels`: Boolean. Whether to create kernels for the created environments (or only install dependencies). Default: `true`.
- `custom_packages_extra_path`: String. Extra PATH directories in which repo2kernel will search for dependencies. Default: `/usr/local/jupyterhub/bin` (which adds the default UU [JupyterHub](../roles/jupyterhub.md)'s `jupyter` executable to path).

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
