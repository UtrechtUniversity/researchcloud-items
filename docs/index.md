# Developer documentation
This is the developer documentation for this repository.
See this [primer SURF ResearchCloud](https://utrechtuniversity.github.io/vre-docs/docs/research-cloud-intro.html) for end-user documentation.

Below is a section for [playbooks](#Playbooks) and a section for [roles](#Roles) (reusable items that can be included in a playbook).
The playbook and roles can be used stand-alone (run them locally on the target host), but are
designed with the goal of deploying them in the deployment of a ResearchCloud workspace.

Contributed playbooks and roles should meet criteria specified in our [item quality checklist](./item_quality_checklist.md).

## External component repositories

This repository contains the bulk of UU's ResearchCloud components for Unix/Linux workspaces, which are based on Ansible playbooks, and it also provides reusable roles as a [collection](#installing-as-a-collection). This documentation is exclusively for the playbooks and roles contained in this repo.

However, some components are not part of this repository and can be found elsewhere. This can be for several reasons (see below). Below is a list of important UU-maintained ResearchCloud components outside of this repository. Documentation should be contained in these external repositories.

| Name                                                                                     | Description                                                                                                                                                                                                                                 | Component type   | Why not in this repo?              |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------------------------------|
| [Grobid](https://github.com/UtrechtUniversity/src-component-grobid)                      | Grobid can help you perform bibliographic analyses on  scientific papers. | Docker Compose | Non-Ansible                        |
| [Galaxy](https://github.com/UtrechtUniversity/src-component-galaxy)                      | Galaxy is a workflow engine for bioinformatics.                                                                                                                                                                                             | Ansible          | Non-standard access rights         |
| [ibridges-ansible](https://github.com/UtrechtUniversity/ibridges-ansible)                | A component to easily download iRODS collections to a workspace.                                                                                                                                                                            | Ansible          | Available as a separate collection |
| [researchcloud-items-win](https://github.com/UtrechtUniversity/researchcloud-items-win/) | Various components targeting Windows workspaces                                                                                                                                                                                             | PowerShell       | Non-Ansible                        |

Components for specific research projects (not intended for general use) should preferably also be stored in a separate repository. They can use the roles in this repo by [installing it as a collection](#installing-as-a-collection).

## Installing as a collection

The roles and playbooks in this repository can also be installed as an Ansible collection. The collection is named `uusrc.general`. After installation, this means you can use the roles from this repository, for example as follows:

```yaml
roles:
    - role: uusrc.general.fact_regular_users
```

To install the collection you have two options:

* install manually with `ansible-galaxy collection install git+https://github.com/utrechtuniversity/researchcloud-items.git`
* add this repository to your `requirements.yml`:

```yaml
---
collections:
  - name: https://github.com/UtrechtUniversity/researchcloud-items.git
    type: git
```

## Playbooks
The status of a playbook is either Experimental or Supported. Supported playbooks are subjected to automated [testing](./index.md#Test-driven-development) and must be fully documented.

For public items in the SURF Research Cloud catalog, this
status should be indicated in the description field of the catalog plugin item.

### Supported

- [agisoft](playbooks/agisoft.md) install Agisoft Metashape
- [alphafold](playbooks/alphafold.md) install DeepMind AlphaFold
- [aptly](playbooks/aptly.md)  serve apt repositories on the workspace
- [asreview](playbooks/asreview_server.md)  machine-learning powered webapplication for systematic reviews
- [custom packages](playbooks/custom_packages.md) download projects, install their dependencies into separate environments, and create Jupyter kernels for them
- [ibridges](playbooks/ibridges.md)  userfriendly commandline client for iRODS
- [icommands](playbooks/icommands.md)  commandline tools for iRODS data grid
- [irods_tools](playbooks/irods_tools.md)  install both iBridges and icommands command line tools
- [irods_sync](playbooks/irods_sync.md)  sync folders from iRODS or Yoda to the workspace at creation time
- [jupyterhub](playbooks/jupyterhub.md) install [JupyterHub](https://jupyterhub.readthedocs.io/)
- [jupyter_rtc](playbooks/jupyter_rtc.md) add Real-time Collaboration functionality to an existing [JupyterHub](https://jupyterhub.readthedocs.io/).
- [flask_app](roles/flask_app.md)  serve a Flask app with Nginx, optionally with SRAM authorization.
- [matlab](playbooks/matlab.md)  Data analysis and simulation suite
- [miniconda](playbooks/miniconda.md)  Python development
- [nextflow](playbooks/nextflow.md) [Nextflow](https://nextflow.io) workflow engine
- [openvscodeserver](playbooks/openvscodeserver.md) installs the OpenVSCode web IDE and serves it for all users
- [openrefine](playbooks/openrefine.md) installs the OpenRefine data cleaning and manipulation webapp
- [python-workbench](playbooks/python-workbench.md)  Python development
- [reverse_proxy](playbooks/reverse_proxy.md) add reverse proxies to the SRC-Nginx environment
- [robot-server](playbooks/robot-server.md) agent used for remote filesystem mounts   
- [robotuser](playbooks/robotuser.md) agent used for remote filesystem mounts
- [r-workbench](playbooks/r-workbench.md)  R development
- [stata](playbooks/stata.md)  Stata18 statistical analysis suite
- [security_updates](playbooks/security_updates.md)  automatic updates for Ubuntu
- [shared_directories](playbooks/shared_directories.md)  create shared data directories for regular users
- [transferuser](playbooks/transferuser.md)  dedicated user for file exchange with remote host
- [uu_provisioning](playbooks/uu_provisioning.md) common tasks for UU workspaces

### Experimental

- [anaconda](playbooks/anaconda.md)  python data science development
- [camunda](playbooks/camunda.md)  a business process workflow suite
- [camunda-modeler](playbooks/camunda-modeler.md)  part of the camunda suite
- [ephor](playbooks/ephor.md) selected roles for ephor use-case
- [keycloak](playbooks/keycloak.md)  OpenIDConnect/SAML Server


## Roles

The status of a role is either Experimental or Supported. Supported roles are subjected to automated [testing](./index.md#Test-driven-development) and must be fully documented.

### Supported

- [agisoft](roles/agisoft.md) install Agisoft Metashape
- [alphafold](roles/alphafold.md) install DeepMind AlphaFold
- [aptly_add](roles/aptly_add.md) add packages to Aptly repositories on the workspace
- [asreview_server](roles/asreview_server.md)
- [default_group](roles/default_group.md) set desired groups as default for regular users
- [desktop-file](roles/desktop_file.md) add desktop icons and login items for custom apps
- [fact_regular_users](roles/fact_regular_users.md) facts about users on the system
- [fact_workspace_info](roles/fact_workspace_info.md) facts about the workspace, and groups and users from the CO (SRAM)
- [ibridges](roles/ibridges.md)  installs [iBridges](https://github.com/UtrechtUniversity/iBridges), a userfriendly commandline client for iRODS (GUI and/or CLI)
- [install_role](roles/install_role.md)
- [irods_repo](roles/irods_repo.md)
- [irods_icommands](roles/irods_icommands.md)
- [irods_iselect](roles/irods_iselect.md)
- [irods_skel](roles/irods_skel.md)
- [julia](roles/julia.md) install the Julia language
- [jupyterhub](roles/jupyterhub.md) install [JupyterHub](https://jupyterhub.readthedocs.io) on the workspace, with SRAM auth.
- [jupyterhub_app](roles/jupyterhub_app.md) install arbitrary applications as an extension for JupyterLab, or as a standalone app served with JupyterHub.
- [jupyterhub_rtc](roles/jupyterhub_rtc.md) add real-time collaboration functionality to an existing JupyterHub.
- [jupyterhub_standalone_proxy](roles/jupyterhub_standalone_proxy.md) use [Jupyter Standalone Proxy](https://jupyter-server-proxy.readthedocs.io/en/latest/standalone.html) to spawn an arbritary web application running as a logged in user.
- [keycloak](roles/keycloak.md)
- [matlab](roles/matlab.md)
- [miniconda](roles/miniconda.md)
- [nextflow](playbooks/nextflow.md) [Nextflow](https://nextflow.io) workflow engine
- [nginx_reverse_proxy](roles/nginx_reverse_proxy.md)
- [nginx_uwsgi](roles/nginx_uwsgi.md) serve uWSGI applications with the SRC-Nginx installation
- [openvscode](roles/openvscodeserver.md) install OpenVSCode server
- [openrefine](roles/openrefine.md) installs the OpenRefine data cleaning and manipulation webapp
- [poetry](roles/poetry.md)
- [pip](roles/pip.md)  install pip
- [pipx_install_systemwide](roles/pipx_install_systemwide.md) install pip packages in a shared directory for all users
- [pyenv](roles/pyenv.md)  install pyenv and use it to install custom python version
- [robotuser](roles/robotuser.md)
- [rstudio](roles/rstudio.md)
- [runonce](roles/runonce.md)
- [rust](roles/rust.md) install the Rust language
- [require_src_docker](roles/require_src_docker.md)
- [require_src_nginx](roles/require_src_nginx.md)
- [security_updates](roles/security_updates.md)
- [sshfs_configrobot](roles/sshfs_configrobot.md)
- [sshfs_mount](roles/sshfs_mount.md)
- [sshfs_cleanup](roles/sshfs_cleanup.md)   
- [system_python](roles/system_python.md) install latests version of python available through the system package manager
- [tidyverse_dependencies](roles/tidyverse_dependencies.md)
- [tigervnc](roles/tigervnc.md) installs TigerVNC server
- [transferuser](roles/transferuser.md)
- [uu_generic](roles/uu_generic.md) generic uu flavouring for workspaces
- [uv](roles/uv.md) lightning fast python version and dependency manager

### Experimental

- [anaconda](roles/anaconda.md)
- [camunda_modeler](roles/camunda_modeler.md)
- [camunda_server](roles/camunda_server.md)
- [rstudio](roles/rstudio.md)
