# Developer documentation
This is the developer documentation for this repository.
See [primer SURF ResearchCloud](https://utrechtuniversity.github.io/vre-docs/docs/research-cloud-intro.html) for end-user documentation).

This documentation concern ResearchCloud components for Unix/Linux workspaces, which are based on Ansible. There is a [separate repository](https://github.com/UtrechtUniversity/researchcloud-items-win/) for Windows components (using PowerShell).

Below is a section for [playbooks](#Playbooks) and a section for [roles](#Roles) (reusable items that can be included in a playbook).
The playbook and roles can be used stand-alone (run them locally on the target host), but are
designed with the goal of deploying them in the deployment of a ResearchCloud workspace.

Contributed playbooks and roles should meet criteria specified in our [item quality checklist](./item_quality_checklist.md).

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

- [aptly](playbooks/aptly.md)  serve apt repositories on the workspace
- [ibridges](playbooks/ibridges.md)  userfriendly commandline client for iRODS
- [icommands](playbooks/icommands.md)  commandline tools for iRODS data grid
- [irods_tools](playbooks/irods_tools.md)  install both iBridges and icommands command line tools
- [irods_sync](playbooks/irods_sync.md)  sync folders from iRODS or Yoda to the workspace at creation time
- [matlab](playbooks/matlab.md) Data analysis and simulation suite
- [miniconda](playbooks/miniconda.md)  Python development
- [python-workbench](playbooks/python-workbench.md)  Python development
- [reverse_proxy](playbooks/reverse_proxy.md) add reverse proxies to the SRC-Nginx environment
- [robotuser](playbooks/robotuser.md) agent used for remote filesystem mounts   
- [r-workbench](playbooks/r-workbench.md)  R development
- [stata](playbooks/stata.md) Stata18 statistical analysis suite
- [security_updates](playbooks/security_updates.md)  automatic updates for Ubuntu
- [shared_directories](playbooks/shared_directories.md) create shared data directories for regular users
- [transferuser](playbooks/transferuser.md) dedicated user for file exchange with remote host

### Experimental

- [anaconda](playbooks/anaconda.md)  python data science development
- [asreview](playbooks/asreview.md)  machine-learning powered application for systematic reviews
- [camunda](playbooks/camunda.md)  a business process workflow suite
- [camunda-modeler](playbooks/camunda-modeler.md)  part of the camunda suite
- [docker](playbooks/docker.md) application container management
- [ephor](playbooks/ephor.md) selected roles for ephor use-case
- [irods-desktop](playbooks/irods-desktop.md) desktop application tools for iRODS data grid
- [keycloak](playbooks/keycloak.md)  OpenIDConnect/SAML Server


## Roles

The status of a role is either Experimental or Supported. Supported roles are subjected to automated [testing](./index.md#Test-driven-development) and must be fully documented.

### Supported

- [aptly_add](roles/aptly_add.md) add packages to Aptly repositories on the workspace
- [default_group](roles/default_group.md) set desired groups as default for regular users
- [desktop-file](roles/desktop_file.md)
- [fact_regular_users](roles/fact_regular_users.md) facts about users on the system
- [fact_workspace_info](roles/fact_workspace_info.md) facts about the workspace, and groups and users from the CO (SRAM)
- [ibridges](roles/ibridges.md)  installs [iBridges](https://github.com/UtrechtUniversity/iBridges), a userfriendly commandline client for iRODS (GUI and/or CLI)
- [install_role](roles/install_role.md)
- [keycloak](roles/keycloak.md)
- [matlab](roles/matlab.md)
- [miniconda](roles/miniconda.md)
- [nginx_reverse_proxy](roles/nginx_reverse_proxy.md)
- [poetry](roles/poetry.md)
- [pip](roles/pip.md)  install pip
- [pipx_install_systemwide](roles/pipx_install_systemwide.md) install pip packages in a shared directory for all users
- [pyenv](roles/pyenv.md)  install pyenv and use it to install custom python version
- [robotuser](roles/robotuser.md)
- [runonce](roles/runonce.md)
- [security_updates](roles/security_updates.md)
- [sshfs-configrobot](roles/sshfs-configrobot.md)
- [sshfs-mount](roles/sshfs-mount.md)
- [sshfs-cleanup](roles/sshfs-cleanup.md)   
- [system_python](roles/system_python.md) install latests version of python available through the system package manager
- [transferuser](roles/transferuser.md)
- [uu_generic](roles/uu_generic.md) generic uu flavouring for workspaces

### Experimental

- [anaconda](roles/anaconda.md)
- [asreview](roles/asreview.md)
- [camunda-modeler](roles/camunda-modeler.md)
- [camunda-server](roles/camunda-server.md)
- [docker](roles/docker.md)
- [git_clone](roles/git_clone.md)
- [irods_repo](roles/irods_repo.md)
- [irods_icommands](roles/irods_icommands.md)
- [irods_iselect](roles/irods_iselect.md)
- [irods_skel](roles/irods_skel.md)
- [myrods_sync](roles/myrods_sync.md)  
- [nginx-fastcgi](roles/nginx-fastcgi.md)   
- [nginx-pam](roles/nginx-pam.md)
- [rstudio](roles/rstudio.md)
- [uwsgi](roles/uwsgi.md)
