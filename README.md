# researchcloud-items
This repository contains [Ansible](https://docs.ansible.com) installation scripts for use in conjunction with [SURF ResearchCloud](https://portal.live.surfresearchcloud.nl). ResearchCloud catalog maintainers can configure a playbook from this repo as a script source for a plugin-type catalog item.  
Alternatively feel free to clone this repository on a target host and locally run a playbook using the command  
`ansible-playbook <name-of-the-playbook>`. 

## Documentation
Script developers, please consult the [developer documentation](docs/index.md) before using a playbook 
to find out if the playbook meets your use case.  
For end-users, there is a [Primer SURF ResearchCloud](docs/primer-for-users.md).

## Applicable licences
Some of the code maintained in this repo is derived from other sources. As a consequence, unfortunately we are unable to provide the entire repo content under a single general license. We use the following licensing policy:
1) If their exists a license file in the root directory of a role then that license applies to all files belonging to that role. 
2) In all other cases the license specified in the top-level directory of this repository applies. 

## Contributing
We are very happy with any contributions in terms of new Ansible scripts for Research Plug-ins and/or documentation. Read the contributing [guidelines](/CONTRIBUTING.md).
