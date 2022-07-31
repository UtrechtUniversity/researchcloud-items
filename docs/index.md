# Developer documentation
(see [primer SURF ResearchCloud](primer-for-users.md) for end-user documentation).   

Below is a section for [playbooks](#Playbooks) and a section for [roles](#Roles).
The playbook can be used stand-alone (run them locally on the target host) 
or as a SURF ResearchCloud plugin.

The roles serve as reusable building blocks for these playbooks.

When adding documentation, please consider to format your text
using the file [template-playbooks.md](playbooks/template-playbooks.md) to
document a playbook
or the file [template-roles.md](roles/template-roles.md) to document a role.

NB: The files section of roles may include [base64 encoded](icons.md) icon files. 
These files can be used to decorate a related catalog item in 
SURF ResearchCloud.

## Playbooks
- [anaconda](playbooks/anaconda.md)  python data science development
- [asreview](playbooks/asreview.md)  machine-learning powered application for systematic reviews
- [camunda](playbooks/camunda.md)  a business process workflow suite
- [camunda-modeler](playbooks/camunda-modeler.md)  part of the camunda suite
- [docker](playbooks/docker.md) application container management
- [ephor](playbooks/ephor.md) selected roles for ephor use-case
- [icommands](playbooks/icommands.md)  commandline tools for iRODS data grid
- [irods-desktop](playbooks/irods-desktop.md) desktop application tools for iRODS data grid
- [keycloak](playbooks/keycloak.md)  OpenIDConnect/SAML Server
- [matlab](playbooks/matlab.md) Data analysis and simulation suite
- [miniconda-base](playbooks/miniconda-base.md)   Python application development
- [python-workbench](playbooks/python-workbench.md)  Python application development
- [robotuser](playbooks/robotuser.md) agent used for remote filesystem mounts


## Roles
- [anaconda](roles/anaconda.md)
- [asreview](roles/asreview.md)
- [camunda-modeler](roles/camunda-modeler.md)
- [camunda-server](roles/camunda-server.md)
- [desktop-file](roles/desktop_file.md)
- [docker](roles/docker.md)
- [fact_regular_users](roles/fact_regular_users.md)
- [git_clone](roles/git_clone.md)
- [irods_guisync](roles/irods_guisync.md)
- [irods_repo](roles/irods_repo.md)
- [irods_icommands](roles/irods_icommands.md)
- [irods_iselect](roles/irods_iselect.md)
- [irods_skel](roles/irods_skel.md)
- [keycloak](roles/keycloak.md)
- [keycloak_behind_nginx](roles/keycloak_behind_nginx.md)
- [matlab](roles/matlab.md)
- [poetry](roles/poetry.md)
- [pip](roles/pip.md)
- [pyenv](roles/pyenv.md)
- [python](roles/python.md)
- [robotuser](roles/robotuser.md)
- [rstudio](roles/rstudio.md)
- [runonce](roles/runonce.md)
- [sshfs-configrobot](roles/sshfs-configrobot.md)
- [sshfs-mount](roles/sshfs-mount.md)
- [sshfs-umount](roles/sshfs-umount.md)
- [userspace_applications](roles/userspace_applications.md)
- [uwsgi](roles/uwsgi.md)
