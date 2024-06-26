# Developer documentation
This is the developer documenation for this repository.
See [primer SURF ResearchCloud](primer-for-users.md) for end-user documentation).


Below is a section for [playbooks](#Playbooks) and a section for [roles](#Roles).
The playbook can be used stand-alone (run them locally on the target host) 
or as a SURF ResearchCloud plugin.

The roles serve as reusable building blocks for these playbooks.

Contributed playbooks and roles should meet criteria specified in our [item quality checklist](./item_quality_checklist.md).


When adding documentation, please consider to format your text
using the file [template-playbooks.md](playbooks/template-playbooks.md) to
document a playbook
or the file [template-roles.md](roles/template-roles.md) to document a role.

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
- [robotuser](playbooks/robotuser.md) agent used for remote filesystem mounts   
- [r-workbench](playbooks/r-workbench.md)  R development
- [stata](playbooks/stata.md) Stata18 statistical analysis suite
- [security_updates](playbooks/security_updates.md)  automatic updates for Ubuntu
- [shared_directories](playbooks/shared_directories.md) create shared data directories for regular users
- [reverse_proxy](playbooks/reverse_proxy.md) add reverse proxies to the SRC-Nginx environment

### Experimental

- [anaconda](playbooks/anaconda.md)  python data science development
- [asreview](playbooks/asreview.md)  machine-learning powered application for systematic reviews
- [camunda](playbooks/camunda.md)  a business process workflow suite
- [camunda-modeler](playbooks/camunda-modeler.md)  part of the camunda suite
- [docker](playbooks/docker.md) application container management
- [ephor](playbooks/ephor.md) selected roles for ephor use-case
- [irods-desktop](playbooks/irods-desktop.md) desktop application tools for iRODS data grid
- [keycloak](playbooks/keycloak.md)  OpenIDConnect/SAML Server
- [transferuser](playbooks/transferuser.md) dedicated user for file exchange with remote host


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
- [nginx-reverse_proxy](roles/nginx-reverse_proxy.md)
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
- [myrods-sync](roles/myrods-sync.md)  
- [nginx-fastcgi](roles/nginx-fastcgi.md)   
- [nginx-pam](roles/nginx-pam.md)
- [rstudio](roles/rstudio.md)
- [transferuser](roles/transferuser.md)   
- [userspace_applications](roles/userspace_applications.md)
- [uwsgi](roles/uwsgi.md)
