# Item Quality Checklist
Below list can be used to check the quality of your ResearchCloud-items software and documentation.


## Documentation 
### Location
As a general guideline, documentation must be maintained in the same environment and as-close-as-possible to 
related program source code. This guideline aims to protect consistency between source code and documentation.  

The guideline translates to the following concrete requirements:   
- workspace compositions listed in the SURF ResearchCloud catalog are effectively specifications (= programs) that reference 
other catalog items. Hence these composition items should be documented in the catalog itself.   
- other catalog items (plugins) merely reference externally held installation scripts. Their "Ansible Playbook" 
scripts are located elsewhere, in a Git repository. The plugin/playbook documentation should be maintained in 
that Git repository.  It suffices to have the catalog item document a refererence to the URL of the documentation in the 
Git repository.  Any other descriptive catalog item information should be derived from the documentation kept in Git.         
- Ansible Roles should be documented in the Git repository that lists their source code.

### Content
As a general guideline, documentation concerning workspace compositions ("application", "application offer") should
target end users. Documentation for other catalog items ("plugins") should target dveelopers/integrators.

Next to descriptive information, the ResearchCloud catalog must document at least for each catalog item:
- name and contact information for the author/maintainer of the item   
- indication of provided level of support to users ("Status: Experimental, use with care" or "Status: Supported")    
- url of documentation (as mentioned in above paragraph)

Catalog items that comprise entire workspace compositions must, in addition to the above, also provide:      
- indication of suitability ("Suitability: non-sensitive data only", "Suitability: sensitive data")    
- indication of maintenance level ("Maintenance: automated (security) patches configured", 
"Maintenance: User must manually apply (security) patches")   
- information on required or recommended workspace dimensions (e.g. cores, memory, operating system version)    
- list of any other user responsibilities, if any     
- information on any monitoring services that are included (e.g. vulnerability scanning of software)    

## Git documentation format
When adding documentation to the Git repository, please consider to format your text
using the file [template-playbooks.md](playbooks/template-playbooks.md) to
document a playbook
or the file [template-roles.md](roles/template-roles.md) to document a role.

NB: The files section of roles may include [base64 encoded](icons.md) icon files. 
These files can be used to decorate a related catalog item in 
SURF ResearchCloud.


## Functionality Scope
Ansible Playbooks (ResearchCloud plugins) should be able to run independent of any other Playbooks. This guideline 
ensures that the Playbook can be reused within the context of different workspace compositions.
Dependencies should be managed within, and hidden by, the Playbook. For instance a Role referenced in the Playbook
could list the other Roles that it depends on. 

Note that the installation script specified by a Playbook will run in isolation from other Playbook installation scripts. 
For instance Ansible variables are scoped to a single ResearchCloud plugin (Playbook) and their value will not be 
passed on to the next plugin Playbook script.

Ansible Roles should follow the principe "doing one thing well".  
For more information, see [Design Principles](./design_principles.md).


## Interoperability
Avoid the use of hardcoded constants or literals in installation scripts. 
Instead, always reference an Ansible variable and include a default value for such variable in the Role specification.

Parameters provided to Ansible Playbooks must follow the naming conventions for SURF ResearchCloud items. 

## Reusability
Source code must always be accompanied by an explicit License. It suffices to mention a common license applicable to the
entire Git repository, except where source code deviates from such convention.

Licences must be compatible with licenses for any other software it depends on. 
The [Public License Selector](https://ufal.github.io/public-license-selector) is a tool that has been developed as 
part of a European Research program. It assists you to select an appropriate and compatible license for software and data.


## Support and Maintenance
A Catalog item should be marked either "experimental" or "supported".
Supported items are expected to be actively maintained and proactively checked for any defects on an annual basis 
or more frequent. They have been tested in use case workspace compositions.
They must be fully documented according to the specifications in this guideline.
They may not comprise of any catalog items that are experimental.

Unsupported items should include a disclaimer to indicate their experimental status. This alerts end users to double-check
compliance with policies.

## Security 
Responsibilities of users with regard to security must be listed in the documentation of workspace compositions.  
As a rule of thumb, it should be clear to end users what level of responsibility they will assume when deploying
a workspace.

A workspace composition should be compliant with applicable policies. When in doubt, limit the authorized use of a 
workspace type to a specified community/collaboration.

## Best practices
### Test-driven development
While unit tests are not present in these plugins made for SURF Research Cloud, there are other tools that can help you: [Ansible testing modules](https://docs.ansible.com/ansible/latest/reference_appendices/test_strategies.html), [Ansible Lint](https://ansible-lint.readthedocs.io/en/latest/) and [Ansible Provisioning in Vagrant VMs](https://www.vagrantup.com/docs/provisioning/ansible).
Try to incorporate as much of TDD into developing playbooks and roles: first determine when your code is succesfull or when it should fail, and then code around those requirements.

### Specific roles
Reuse the roles defined inside this repository for certain tasks, instead of doing it yourself. Especially for SURF Research Cloud, these roles come in handy:

- Use [runonce](roles/runonce.md) to have a piece of code ran once the first time a user logs in.
- Use [desktop_file](roles/desktop_file.md) to create menu and desktop entries.
- Use [fact_regular_users](roles/fact_regular_users.md) to gather a list of all users on the system.
- Use [git_clone](roles/git_clone.md) to let users clone a git repository into a environment through arguments.

### Keep userspace and system-wide seperate
Especially for python-related software: most times, keeping everything separate and private for all users is the best default approach. Let users select their own versions to avoid clashes.
