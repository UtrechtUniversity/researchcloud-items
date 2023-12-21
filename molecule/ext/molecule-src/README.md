# SURF Research Cloud Molecule Testing Configuration

This repository contains default configuration for running [Molecule](https://ansible.readthedocs.io/projects/molecule/) tests for SURF Research Cloud (SRC) Components and Catalog Items. The repository is meant to be included into other repositories as a subtree.

## Getting Started

Follow the installation and setup instructions below, then run:

`molecule -c molecule/ext/molecule-src/molecule.yml test -s <scenario-name>`

...where <scenario-name> is the name of one of the subdirectories of the `molecule` directory, e.g. `playbook-security_updates`. 

### Requirements

1. Docker and/or Podman (to spin up test containers)
1. Python and pip
1. Ansible
1. Access to the [test container images](https://github.com/UtrechtUniversity/SRC-test-workspace)

The default `molecule.yml` is configured to use the images from [this package](https://github.com/UtrechtUniversity/SRC-test-workspace/i), but you can override this to use other images.

### Install SRC-specific configuration

To add Molecule tests to your SRC component or catalog item repository, follow these steps:

1. create a `molecule` directory in your repository's root: `mkdir molecule`
1. include the contents of this repository as a subtree, under `molecule/ext/molecule-src`
  * `git remote add molecule-src https://github.com/UtrechtUniversity/SRC-molecule.git`
  * `git subtree add --prefix molecule/ext/molecule-src molecule-src main --squash`
1. copy the default `.env.yml` file to your repository root: `cp molecule/ext/molecule-src/default.env.yml .env.yml`
  * optionally edit the contents of `.env.yml`, if your playbooks are not in the default location (the repository root)
1. run `pip install -r molecule/ext/molecule-src/requirements.txt`

That's it for setup! You're now ready to start [adding your own scenarios](#adding-scenarios).

### Scenarios

Molecule runs tests for each *scenario* defined under the `molecule` directory. You can think of each scenario as a self-contained test suite. A scenario is just a subdirectory of the `molecule` directory that contains a number of configuration files and playbooks. For our purposes, these are minimally:

* `molecule.yml` - sets general configuration variables for the test suite (e.g. what platform to run on). Overrides the defaults in `molecule/ext/molecule-src/molecule.yml`.
* `prepare.yml`  - a playbook used to make preparations on the container before running the Ansible code that we want to test on it.
* `converge.yml` - a playbook that specifies how to deploy the Ansible role or playbook that we want to test on the container.
* `verify.yml`   - a playbook that contains additional test assertions after the `converge` step is run.

We want to test our SURF Research Cloud (SRC) components in a specific way, namely by:

1. copying them onto the workspace
2. then executing them with Ansible *on the workspace* (as opposed to using Ansible on the host).

We want this procedure because that is [how components are actually deployed onto SRC workspaces](https://github.com/UtrechtUniversity/SRC-test-workspace#how-it-works).

To help us achieve this, the `default` scenario contains a `prepare.yml` that takes care of 1., and a `converge.yml` that takes care of 2. Each individual scenario will automatically use these default playbooks, as long as `molecule` is run with the ` -c molecule/default/molecule.yml`.

### Adding scenarios

To create a Molecule scenario to test, just create a subdirectory of the `molecule` directory, e.g.:

`mkdir molecule/my-component`

Now add a `molecule.yml` file to the `my-component` subdirectory, with contents like the following:

```yaml
provisioner:
  name: ansible
  env:
    components:
      - name: 'my-component'
        path: 'my-component.yaml'
        parameters: # Define all parameters needed by the component here
          my_component_param1: 'Foo'
```

The above config file does not provide a `platforms` key, so tests for this scenario will use the default platforms (containers) specified in `molecule/ext/molecule-src/molecule.yml` (Ubuntu Focal and Ubuntu Jammy). You can override this by adding your own platform definition, e.g.:

```yaml
platforms:
  - name: workspace-src-ubuntu_focal-desktop
    image: ghcr.io/utrechtuniversity/src-test-workspace:ubuntu_focal-desktop # You can also change this to another image
    pre_build_image: true
    # The following lines are an example of how to specify a container registry to pull the image from, if it is not already available locally.
    registry:
      url: $DOCKER_REGISTRY # Use environment variables to define the URL and credentials
      credentials:
        username: $DOCKER_USER
```

Note that you can also define multiple platforms.

### Specifying a Driver

The molecule tests can use either Docker or Podman (default). You can override the default driver in your scenario's `molecule.yml`. Or even easier: set an environment variable like `DRIVER=docker`.

### Adding additional preparation tasks

Sometimes it may be helpful to perform certain tasks before the `converge` step. The default `prepare.yml` playbook will check if the user has set the `extra_prepare_tasks` key in the scenario's `molecule.yml` `env` section. Set this key to a relative path to a playbook (relative to the location of the default molecule configuration), and the tasks in that playbook will be executed at the end of the `prepare` step.

### Adding additional assertions

You can a `verify.yml` to your scenario to perform additional assertions. See the [Molecule docs](https://ansible.readthedocs.io/projects/molecule/configuration/#verifier).

The main thing we are testing using Molecule is whether our playbooks are deployable on SRC workspaces. Since Ansible itself checks whether each task is actually successful (i.e. *changes* the target in the required way), we do not need to assert that everything we do in a playbook actually happens: when a playbook contains the instruction to e.g. install a certain package, and the playbook deploys on our test containers without error, we *know* that the container is in the required state.

However, in some cases, it may be desirable to perform additional assertions after deployment is complete. Molecule allows you to do this by adding a `verify.yml` playbook to your scenario. You can use this perform assertions either using Ansible's own [assert module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/assert_module.html), or using [testinfra](https://ansible.readthedocs.io/projects/molecule/configuration/#molecule.verifier.testinfra.Testinfra).

What can/should be tested in a `verify.yml`? For instance:

* behaviour that is conditional on certain parameters, and therefore not already triggered by simply executing the playbook on the test container (in `converge.yml`)
* lower level behaviour: e.g., not whether service `apache2` is running (we know that it is, since we require this in our playbook), but whether connecting to port 80 actually yields the desired webservice (e.g. a Jupyter notebook).

## Debugging

### Inspecting the workspace

For debugging and development purposes, it can be useful to inspect what's going on on a container after executing a playbook or role on it. There are two ways of doing this:

1. Run `molecule` with the `create` command instead of the `test` command: `molecule -c molecule/default/molecule.yml create -s <scenario-name>`
2. Run `molecule` with the `--destroy=never` flag: `molecule -c molecule/default/molecule.yml test -s <scenario-name> --destroy=never`

Both of these methods ensure that the container is not destroyed after molecule is done. This means you can then login to the container and see what's going on. For instance, after molecule is done, you can:

1. `docker container list`
  * see that the container `workspace-src-ubuntu_focal` is still running
2. `docker exec -it workspace-src-ubuntu_focal bash`
  * login to the container as root
