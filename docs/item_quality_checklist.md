# Item Quality Checklist
Below list can be used to check the quality of your ResearchCloud-items software and documentation.

## Documentation

### Components

Components in the ResearchCloud catalog should contain a brief description:

- name and contact information for the author/maintainer of the item or component.
- link to developer documentation (e.g. to this repository).

For Ansible-based Components (see [here](./index.md#a-note-on-windows) for more info), both the *playbooks* and the *roles* utilized by the playbook should be documented.

### Catalog Items

ResearchCloud _catalog items_ are effectively compositions that reference various components. Catalog items should be described in the ResearchCloud catalog itself, including:

- name and contact information for the author/maintainer of the item or component   
- link to enduser documentation. For UU Catalog Items, this documentation can be found at https://utrechtuniversity.github.io/vre-docs/docs/workspace-catalogue.html
- a brief description

The description field should provide:

- indication of suitability ("Suitability: non-sensitive data only", "Suitability: sensitive data")
- indication of maintenance level ("Maintenance: automated (security) patches configured", 
"Maintenance: User must manually apply (security) patches")
- information on required or recommended workspace dimensions (e.g. cores, memory, operating system version)    
- list of any other user responsibilities, if any     
- information on any monitoring services that are included (e.g. vulnerability scanning of software)
- if the item is experimental or not yet fully supported, this should be clear from the description or subtitle.

## Functionality Scope
Ansible Playbooks (ResearchCloud components) should be able to run independent of any other Playbooks. This guideline 
ensures that the Playbook can be reused within the context of different workspace compositions.
Dependencies should be managed within, and hidden by, the Playbook. For instance a Role referenced in the Playbook
could list the other Roles that it depends on. 

Note that the installation script specified by a Playbook will run in isolation from other Playbook installation scripts. 
For instance Ansible variables are scoped to a single ResearchCloud component (Playbook) and their value will not be 
passed on to the next component Playbook script.

Ansible Roles should follow the principe "doing one thing well".  
For more information, see [Design Principles](./design_principles.md).


## Interoperability
Avoid the use of hardcoded constants or literals in installation scripts. 
Instead, always reference an Ansible variable and include a default value for such variable in the Role specification.

Parameters provided to Ansible Playbooks must follow the naming conventions for SURF ResearchCloud items.

## Reusability
Source code must always be accompanied by an explicit License. It suffices to mention a common license applicable to the
entire Git repository, except where source code deviates from such convention.

Licences should be compatible with licenses for any other software it depends on. 
The [Public License Selector](https://ufal.github.io/public-license-selector) is a tool that has been developed as 
part of a European Research program. It assists you to select an appropriate and compatible license for software and data.


## Support and Maintenance

Supported catalog items and components:

- are expected to be actively maintained and proactively checked for any defects, for instance through automated testing.
- they have been tested in use case workspace compositions.
- they must be fully documented according to the specifications in this guideline.
- supported catalog items may not comprise of any catalog components that are experimental.

Components should be set to *Public* (usable by all Collaborative Organisations) only if they meet the above criteria.

Unsupported items/components should include a disclaimer to indicate their experimental status. This alerts end users to double-check
compliance with policies.

## Security 
Catalog item documentation should list the responsibilities of users with regard to security.  
As a rule of thumb, it should be clear to end users what level of responsibility they will assume when deploying
a workspace.

A workspace composition should be compliant with applicable policies. When in doubt, limit the authorized use of a 
workspace type to a specified community/collaboration.

## Best practices

### Test-driven development

While unit tests are not present in these components made for SURF Research Cloud, there are other tools that can help you:

- [Molecule deployment tests](https://github.com/ansible/molecule). See [here](https://github.com/UtrechtUniversity/SRC-molecule) for more information on how to utilize Molecule for ResearchCloud items.
- [Ansible testing modules](https://docs.ansible.com/ansible/latest/reference_appendices/test_strategies.html)
- [Ansible Lint](https://ansible-lint.readthedocs.io/en/latest/)
- [Ansible Provisioning in Vagrant VMs](https://www.vagrantup.com/docs/provisioning/ansible).

Try to incorporate as much of TDD into developing playbooks and roles: first determine when your code is succesfull or when it should fail, and then code around those requirements.

CI pipelines for Ansible Lint and Molecule are essential to guarding against the introduction of bugs and maintaining code quality.

### Specific roles

The roles in the [uusrc.general collection](./index.md#installing-as-a-collection) contain many roles that faciliate best practices on ResearchCloud, for instance:

- Use [runonce](roles/runonce.md) to have a piece of code ran once the first time a user logs in.
- Use [desktop_file](roles/desktop_file.md) to create menu and desktop entries.
- Use [fact_regular_users](roles/fact_regular_users.md) to gather a list of all users on the system.
- Use [fact_workspace_info](roles/fact_workspace_info.md) to gather general facts about the workspace, including whether it is a desktop workspace and which [SRAM CO roles](https://utrechtuniversity.github.io/vre-docs/docs/glossary.html#collaboration) are defined.
- Use [nginx_reverse_proxy](roles/nginx_reverse_proxy.md) to easily define reverse proxies and other Nginx locations on top of the SURF Nginx component.
- Use [pipx_install_systemwide](roles/pipx_install_systemwide.md) to avoid installing Python applications using the system Python interpeter (e.g. `/usr/bin/python3`), which might break `pip` dependencies on which the system depends.
