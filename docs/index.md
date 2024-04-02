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
The status of a playbook is either Experimental or Supported. In the SURF Research Cloud catalog, this
status should be indicated in the description field of the catalog plugin item.

### Supported playbooks:   
("Status: Supported")    

Currently, all our playbooks are still considered Experimental. 


### Experimental playbooks:   
("Status: Experimental, use with caution")     
- [anaconda](playbooks/anaconda.md)  python data science development
- [aptly](playbooks/aptly.md) serve apt repositories on the workspace
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
- [miniconda](playbooks/miniconda.md)  Python applicaiton development
- [python-workbench](playbooks/python-workbench.md)  Python application development
- [security_updates](playbooks/security_updates.md)  automatic updates for Ubuntu
- [reverse_proxy](playbooks/reverse_proxy.md) add reverse proxies to the SRC-Nginx environment
- [robotuser](playbooks/robotuser.md) agent used for remote filesystem mounts   
- [transferuser](playbooks/transferuser.md) dedicated user for file exchange with remote host


## Roles
- [anaconda](roles/anaconda.md)
- [aptly_add](roles/aptly_add.md) add packages to Aptly repositories on the workspace
- [asreview](roles/asreview.md)
- [camunda-modeler](roles/camunda-modeler.md)
- [camunda-server](roles/camunda-server.md)
- [desktop-file](roles/desktop_file.md)
- [docker](roles/docker.md)
- [fact_regular_users](roles/fact_regular_users.md)
- [git_clone](roles/git_clone.md)
- [install_roles](roles/install_role.md)
- [irods_guisync](roles/irods_guisync.md)  NB: deprecated
- [irods_repo](roles/irods_repo.md)
- [irods_icommands](roles/irods_icommands.md)
- [irods_iselect](roles/irods_iselect.md)
- [irods_skel](roles/irods_skel.md)
- [keycloak](roles/keycloak.md)
- [keycloak_behind_nginx](roles/keycloak_behind_nginx.md)
- [matlab](roles/matlab.md)
- [miniconda](roles/miniconda.md)
- [myrods-sync](roles/myrods-sync.md)  
- [nginx-fastcgi](roles/nginx-fastcgi.md)   
- [nginx-pam](roles/nginx-pam.md)
- [nginx-reverse_proxy](roles/nginx-reverse_proxy.md)
- [poetry](roles/poetry.md)
- [pip](roles/pip.md)
- [pyenv](roles/pyenv.md)
- [python](roles/python.md)
- [robotuser](roles/robotuser.md)
- [rstudio](roles/rstudio.md)
- [runonce](roles/runonce.md)
- [security_updates](roles/security_updates.md)
- [sshfs-configrobot](roles/sshfs-configrobot.md)
- [sshfs-mount](roles/sshfs-mount.md)
- [sshfs-umount](roles/sshfs-umount.md)   
- [transferuser](roles/transferuser.md)   
- [userspace_applications](roles/userspace_applications.md)
- [uwsgi](roles/uwsgi.md)
