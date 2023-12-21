# Molecule tests

From the project root, run:

`molecule -c molecule/ext/molecule-src/molecule.yml test -s <scenario-name>`

...where <scenario-name> is the name of one of the subdirectories of the `molecule` directory, e.g. `playbook-security_updates`. 

Using `-c molecule/ext/molecule-src/molecule.yml` ensures molecule uses the default configuration [for testing Research Cloud images](https://github.com/UtrechtUniversity/SRC-molecule#scenarios).

**For more information on the molecule testing setup, see: https://github.com/UtrechtUniversity/SRC-molecule/blob/main/README.md**

## Playbooks tests

Playbook tests use a specific setup that aims to be as close as possible to the way components are executed on Research Cloud. See [here](https://github.com/UtrechtUniversity/SRC-molecule#scenarios) for more information. Running `molecule` with the parameters explained above automatically takes care of this.

## Role tests

For simplicity's sake, roles are currently not tested in the specific way that playbooks are.

Keep in mind that this may mean that a role for which the tests pass locally on your machine may not work on a SRC workspace, e.g. due to different versions of Ansible on your machine and on SRC workspaces. Of course, as soon as you create a playbook/component that uses the role, the tests for this playbook *will* check that everything passes in an SRC environment!

This means that:

* Role tests may be used to test things like the behaviour of the role given different parameter settings.
* Playbook tests should be used to test whether everything works on SRC environments.

# CI tests

The workflow `.github/workflows/molecule.yml` utilises the playbook and role testing setup explained above to achieve CI for our playbooks and roles.

## Which scenarios are run?

There are some tricky aspects to the workflow file that derive from the fact that all our components and roles are currently in one big repository. Since we do not want tests to run for *every* role and playbook in every PR, the workflow needs to:

1. check which roles and playbooks were modified in the PR/push event
1. check whether a corresponding scenario for each of the modified items exists in the `molecule/` directory

Currently, this means that a test for the scenario `playbook-python-workbench` is *only* triggered when the file `playbooks/python-workbench.yml` is modified. The scenario is **not** run when the files in `molecule/playbook-python-workbench.yml` are changed, and **also not** when any of the *roles* that the playbook relies on are changed. Since we may anyway move to a setup where every component has its own repository, it is presently not worth it to implement these triggers.

**Note: the CI tests expect the scenario for `playbook-foo.yml` to live in `molecule/playbook-foo`. A scenario for a role `bar` should live in `molecule/role-bar.**

## Which images are used?

The default `molecule.yml` is configured to use the images from [this package](https://github.com/UtrechtUniversity/SRC-test-workspace/), which are designed to mimick SURF Research Cloud (SRC) workspaces. On CI, the latest images for each OS flavour (tags are e.g. `ubuntu_focal`, `ubuntu_jammy`, `ubuntu_focal-desktop`) are automatically pulled from the Github Container Registry (https://ghcr.io).
