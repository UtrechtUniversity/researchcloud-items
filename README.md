# SURF Research Cloud Molecule Testing Configuration

This repository contains default configuration for running [Molecule](https://ansible.readthedocs.io/projects/molecule/) tests for SURF Research Cloud (SRC) Components and Catalog Items. The repository is meant to be included into other repositories as a subtree.

## Getting Started

### Requirements

1. Docker and/or Podman (to spin up test containers)
1. Python and pip
1. Ansible
1. Access to the [test container images](https://github.com/UtrechtUniversity/SRC-test-workspace)

### Install SRC-specific configuration

To add Molecule tests to your SRC component or catalog item repository, follow these steps:

1. create a `molecule` directory in your repository's root: `mkdir molecule`
1. include the contents of this repository as a subtree, under `molecule/ext/molecule-src`
  * `git remote add molecule-src https://github.com/UtrechtUniversity/SRC-molecule.git`
  * `git subtree add --prefix molecule/ext/molecule-src molecule-src main --squash`
1. copy the default `.env.yml` file to your repository root: `cp molecule/ext/molecule-src/default/env.yml .env.yml`
  * optionally edit the contents of `.env.yml`, if your playbooks are not in the default location (the repository root)
1. run `pip install -r molecule/ext/molecule-src/requirements.txt`

That's it for setup! You're now ready to start adding your own scenarios.

## Adding scenarios

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
    image: ghcr.io/utrechtuniversity/src-test-workspace:ubuntu_focal-desktop
    pre_build_image: true
    # The following lines are an example of how to specify a container registry to pull the image from, if it is not already available locally.
    registry:
      url: $DOCKER_REGISTRY
      credentials:
        username: $DOCKER_USER
```

## Adding additional assertions