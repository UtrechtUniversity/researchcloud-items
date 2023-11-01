# Molecule tests

From the project root, run:

`molecule -c molecule/default/molecule.yml test -s <scenario-name>`

...where <scenario-name> is the name of one of the subdirectories of the `molecule` directory, e.g. `playbook-security_updates`. 

Using `-c molecule/default/molecule.yml` ensures molecule uses the default configuration [for testing SRC images](#Testing-SRC-workspaces). By default (unless [overriden](#Overriding-the-default-configuration-for-a-scenario) in a scenario's own `molecule.yml`), this will test the scenario on both Ubuntu Focal and Ubuntu Jammy.

### Images

The default `molecule.yml` is configured to use the images from [this package](https://github.com/UtrechtUniversity/SRC-test-workspace/i), which are designed to mimick SURF Research Cloud (SRC) workspaces. For local test, these images are therefore expected to present on your machine. To pull the images on your local machine, do the following:

1. `docker login ghcr.io -u <githubusername>`
  * enter a valid GitHub token with the apprioriate priviliges to read the package. See [here](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) for more info.
2. `docker pull ghcr.io/utrechtuniversity/src-test-workspace:ubuntu_focal` (and similarly for other tags)
  * NB: pulling these images currently is only possible for members of the UtrechtUniversity organisation

### Inspecting the workspace

For debugging and development purposes, it can be useful to inspect what's going on on a container after executing a playbook or role on it. There are two ways of doing this:

1. Run `molecule` with the `create` command instead of the `test` command: `molecule -c molecule/default/molecule.yml create -s <scenario-name>`
2. Run `molecule` with the `--destroy=never` flag: `molecule -c molecule/default/molecule.yml test -s <scenario-name> --destroy=never`

Both of these methods ensure that the container is not destroyed after molecule is done. This means you can then login to the container and see what's going on. For instance, after molecule is done, you can:

1. `docker container list`
  * see that the container `workspace-src-ubuntu_focal` is still running
2. `docker exec -it workspace-src-ubuntu_focal bash`
  * login to the container as root

## Scenarios

Molecule runs tests for each *scenario* defined under the `molecule` directory. You can think of each scenario as a self-contained test suite. A scenario is just a subdirectory of the `molecule` directory that contains a number of configuration files and playbooks. For our purposes, these are minimally:

* `molecule.yml` - sets general configuration variables for the test suite (e.g. what platform to run on)
* `prepare.yml`  - a playbook used to make preparations on the container before running the Ansible code that we want to test on it
* `converge.yml` - a playbook that specifies how to deploy the Ansible role or playbook that we want to test on the container
* `verify.yml`   - a playbook that contains additional test assertions after the `converge` step is run

Each scenario's own `molecule.yml` is merged onto the default `molecule.yml` configuration when using the `-c molecule/default/molecule.yml` flag, so settings from the default config can be overriden on a per-scenario basis.

### Testing SRC workspaces

We want to test our SURF Research Cloud (SRC) components in a specific way, namely by:

1. copying them onto the workspace
2. then executing them with Ansible *on the workspace* (as opposed to using Ansible on the host).

We want this procedure because that is how components are actually deployed onto SRC workspaces.

To help us achieve this, the `default` scenario contains a `prepare.yml` that takes care of 1., and a `converge.yml` that takes care of 2. Each individual scenario will automatically use these default playbooks, as long as `molecule` is run with the ` -c molecule/default/molecule.yml`.

This means a new scenario only needs to configure the right component to be copied and deployed onto the workspace. We can easily do so in the scenario's `molecule.yml`:

```yaml
# molecule/new_scenario/molecule.yml
provisioner:
  name: ansible
  env:
    PLAYBOOK_PATH: 'new_scenario.yml' # The path to the playbook we want to test in this scenario. Relative to PLAYBOOK_DIR defined in default/molecule.yml
```

Optionally, your scenario can also contain a `verify.yml` to [perform additional assertions](#assertions-in-verifyyml) after `converge` is run.

### Overriding the default configuration for a scenario

You can override the settings from `molecule/default/molecule.yml` for individual scenario's in that scenario's own `molecule.yml`. This file is located in `molecule/<scenario-name>/molecule.yml`.

You can override, for instance, the platforms on which molecule is supposed to test:

```yaml
# Tests are run on Ubuntu focal and jammy by default, this will cause the scenario to use the focal-desktop image instead
platforms:
  - name: workspace-src-ubuntu_focal-desktop
    image: ghcr.io/utrechtuniversity/src-test-workspace:ubuntu_focal-desktop
    pre_build_image: true
```

...or you can specify multiple platforms!


### Setting component parameters for a playbook

In a scenario's `molecule.yml`, you can override the following settings to pass component parameters on to the playbook that will be executed on the container workspace:

```yaml
provisioner:
  name: ansible
  env:
    PLAYBOOK_PATH: 'my-playbook.yml'
    REMOTE_PLUGIN_PARAMETERS:
    # Your parameters go here
```

### Assertions in `verify.yml`

The main thing we are testing using Molecule is whether our playbooks are deployable on SRC workspaces. Since Ansible itself checks whether each task is actually successful (i.e. *changes* the target in the required way), we do not need to assert that everything we do in a playbook actually happens: when a playbook contains the instruction to e.g. install a certain package, and the playbook deploys on our test containers without error, we *know* that the container is in the required state.

However, in some cases, it may be desirable to perform additional assertions after deployment is complete. Molecule allows you to do this by adding a `verify.yml` playbook to your scenario. You can use this perform assertions either using Ansible's own [assert module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/assert_module.html), or using [testinfra](https://ansible.readthedocs.io/projects/molecule/configuration/#molecule.verifier.testinfra.Testinfra).

What can/should be tested in a `verify.yml`? For instance:

* behaviour that is conditional on certain parameters, and therefore not already triggered by simply executing the playbook on the test container (in `converge.yml`)
* lower level behaviour: e.g., not whether service `apache2` is running (we know that it is, since we require this in our playbook), but whether connecting to port 80 actually yields the desired webservice (e.g. a Jupyter notebook).

### Role tests

For simplicity's sake, roles are currently not tested in the specific way explained above: i.e., we do not test them by running Ansible on the container/workspace, but simply by runnning Ansible on the controller (i.e., your machine). Keep in mind that this may mean that a role for which the tests pass locally on your machine may not work on a SRC workspace, e.g. due to different versions of Ansible on your machine and on SRC workspaces. Of course, as soon as you create a playbook/component that uses the role, the tests for this playbook *will* check that everything passes in an SRC environment!

This means that:

* Role tests may be used to test things like the behaviour of the role given different parameter settings.
* Playbook tests should be used to test whether everything works on SRC environments.

# CI tests

The workflow `molecule.yml` utilises the molecule testing setup explained above to achieve CI for our playbooks and roles.

### Which scenarios are run?

There are some tricky aspects to the workflow file that derive from the fact that all our components and roles are currently in one big repository. Since we do not want tests to run for *every* role and playbook in every PR, the workflow needs to:

1. check which roles and playbooks were modified in the PR/push event
1. check whether a corresponding scenario for each of the modified items exists in the `molecule/` directory

Currently, this means that a test for the scenario `playbook-python-workbench` is *only* triggered when the file `playbooks/python-workbench.yml` is modified. The scenario is **not** run when the files in `molecule/playbook-python-workbench.yml` are changed, and **also not** when any of the *roles* that the playbook relies on are changed. Since we may anyway move to a setup where every component has its own repository, it is presently not worth it to implement these triggers.

**Note: the CI tests expect the scenario for `playbook-foo.yml` to live in `molecule/playbook-foo`.**

### Which images are used?

The default `molecule.yml` is configured to use the images from [this package](https://github.com/UtrechtUniversity/SRC-test-workspace/), which are designed to mimick SURF Research Cloud (SRC) workspaces. On CI, the latest images for each OS flavour (tags are e.g. `ubuntu_focal`, `ubuntu_jammy`, `ubuntu_focal-desktop`) are automatically pulled from the Github Container Registry (https://ghcr.io).