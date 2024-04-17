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

## CI

[Molecule](https://ansible.readthedocs.io/projects/molecule/) tests are run in GitHub Actions for pull requests and pushes to the `main` branch. In order to avoid running expensive tests (spinning up [SRC workspace containers](https://github.com/UtrechtUniversity/SRC-test-workspace) for every scenario), the workflow checks which files have been modified, and thus need to be tested again.

There are two kinds of tests:

1. Role tests. Molecule scenarios should be stored in the `playbooks/roles/<role>/molecule/` directory.
1. Playbook tests. Molecule scenarios should be stored in the `molecule/` directory and given a `playbook-` prefix.

By following this convention, the CI workflow knows that when a pull request modifies e.g. `playbooks/roles/pyenv/tasks/main.yml`, the scenario `molecule/role-pyenv` should be run. The CI tests are also run when anything changes in the scenario itself (so e.g. when you change `molecule/playbook-python-workbench/molecule.yml`).