# researchcloud-items
This repository contains [Ansible](https://docs.ansible.com) installation scripts for use in conjunction with [SURF ResearchCloud](https://portal.live.surfresearchcloud.nl). ResearchCloud catalog maintainers can configure components from the playbooks in this repo.

The scripts in this repository all target Unix/Linux workspaces. There is a separate repisitory for install scripts for Windows workspaces [here](https://github.com/UtrechtUniversity/researchcloud-items-win).

## Ansible Galaxy Collection

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

## Documentation
Script developers, please consult the [developer documentation](docs/index.md) before using a playbook 
to find out if the playbook meets your use case.
For end-users, there is a [Primer SURF ResearchCloud](docs/primer-for-users.md).

## Applicable licences
Some of the code maintained in this repo is derived from other sources. As a consequence, unfortunately we are unable to provide the entire repo content under a single general license. We use the following licensing policy:
1) If there exists a license file in the root directory of a role then that license applies to all files belonging to that role.
2) Logo's, pictures and icon files for external applications (for instance, for documentation purposes or for displaying app icons to endusers) not created by UU naturally do not fall under our license, but are used under fair use.
3) In all other cases the license specified in the top-level directory of this repository applies. 

## Contributing
We are very happy with any contributions in terms of new Ansible scripts for Research Plug-ins and/or documentation. Read the contributing [guidelines](./CONTRIBUTING.md).

## CI

[Molecule](https://ansible.readthedocs.io/projects/molecule/) tests are run in GitHub Actions for pull requests and pushes to the `main` branch. In order to avoid running expensive tests (spinning up [SRC workspace containers](https://github.com/UtrechtUniversity/SRC-test-workspace) for every scenario), the workflow checks which files have been modified, and thus need to be tested again.

There are two kinds of tests:

1. Role tests. Molecule scenarios should be stored in the `playbooks/roles/<role>/molecule/` directory.
1. Playbook tests. Molecule scenarios should be stored in the `molecule/` directory and given a `playbook-` prefix.

By following this convention, the CI workflow knows that when a pull request modifies e.g. `playbooks/foo.yml`, the scenario `molecule/playbook-foo` should be run. The CI tests are also run when anything changes in the scenario itself (so e.g. when you change `molecule/foo/molecule.yml`).
