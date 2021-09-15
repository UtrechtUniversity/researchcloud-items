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
- [camunda](playbooks/camunda.md)  a business process workflow suite
- [camunda-modeler](playbooks/camunda-modeler.md)  part of the camunda suite
- [icommands](playbooks/icommands.md)  commandline tools for iRODS data grid
- [keycloak](playbooks/keycloak.md)  OpenIDConnect/SAML Server
- [python-workbench](playbooks/python-workbench.md)  Python application development
- [miniconda-base](playbooks/miniconda-base.md)   Python application development

## Roles
- [camunda-modeler](roles/camunda-modeler.md)
- [camunda-server](roles/camunda-server.md)
- [fact_regular_users](roles/fact_regular_users.md)
- [irods_repo](roles/irods_repo.md)
- [irods_icommands](roles/irods_icommands.md)
- [irods_iselect](roles/irods_iselect.md)
- [irods_skel](roles/irods_skel.md)
- [keycloak](roles/keycloak.md)
- [keycloak_behind_nginx](roles/keycloak_behind_nginx.md)
- [python](roles/python.md)
- [runonce](roles/runonce.md)
- [userspace_applications](roles/userspace_applications.md)
- [uwsgi](roles/uwsgi.md)
