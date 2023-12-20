# Playbook aptly
[back to index](../index.md#Playbooks)

## Summary

Installs [Aptly](https://www.aptly.info/), the "Swiss army knife for Debian repository management", and uses it to serve apt repositories on the workspace, as defined by the user.

## Requires

* OS: Ubuntu `jammy` or higher.
* OS: Debian `bookworm` or higher.
* Component: `nginx` must be installed and running on the workspace when this component is executed.

## Description

This component:

1. installs Aptly.
1. uses Aptly to create apt repositories, as defined by the user (see [Variables](#Variables)).
1. uses Aptly to add packages to the created repositories, as defined by the user (see [Variables](#Variables)).
1. uses `nginx` to serve the apt repositories from the workspace.
  * repositories are served under the `/apt/` location (e.g. `https://<workspace_fqdn>/apt/dists/...`)

To publish repositories, Aptly must have access to a valid GPG Keypair. This component:

* uses a keypair provided by the user in the component parameters (see [Variables](#Variables)).
* creates a new keypair when none is provided by the user.
  * the new public key is served by `nginx` alongside the apt repositories (URL: `<workspace_fqdn>/apt/aptly_pubkey.asc`), so that it can easily be downloaded.

To add packages to repositories, the component creates the script `/usr/local/bin/aptly_add_packages.sh`. The script is run once when this component is executed, but you can also use it at any later time to add more packages to the repositories defined by this component. See the [aptly_add role](../roles/security_updates.md) for documentation.

## Variables

### Aptly repositories

`aptly_repositories`: String of YAML dict objects (one on every newline) defining repositories to be created. Example:

```yaml
{name: jammy, distribution: jammy, label: test, state: present, components: [main, experimental], architectures: [amd64, arm64]}
{name: focal, distribution: focal, label: test, state: present, components: [main, experimental], architectures: [amd64]}
```

This creates repositories for two distributions (`jammy` and `focal`), each with two 'components' (channels, in this case `main` and `experimental`). The `focal` repo will contain only `amd64` packages, while the `jammy` repo also supports `arm64`. The `name` and `label` attributes are descriptive. For more info, compare the [format of an apt repo](https://wiki.debian.org/DebianRepository/Format).

### Aptly packages

`aptly_packages`: String of YAML dict objects (one on every newline) defining directories from which predefined repositories (see `aptly_repositories`) will be provisioned. Put your `.deb` packages in these directories to automatically add them to the repositories you have defined. Example:

```yaml
{name: jammy, component: main, packages: /pkgs/jammy, architectures: [amd64, arm64]}
{name: focal, component: main, packages: /pkgs/focal, architectures: [amd64]}
```

This adds all `.deb` files `/pkgs/jammy` to the `jammy-main` channel, and all `.deb` files in `/pkgs/focal` to the `focal-main` channel.

### Aptly general

- `aptly_gpg_private_key`: String GPG private key. ResearchCloud will turn newlines into `\n` characters, so these are replaced by true newlines in the playbook. **Note**: a key without a passphrase is expected.
- `aptly_gpg_public_key`: String GPG public key. ResearchCloud will turn newlines into `\n` characters, so these are replaced by true newlines in the playbook.
- `aptly_user`: String name for the aptly user (default: `aptly`).
- `aptly_home`: String homedirectory for the aptly user (default: `/srv/aptly`).

### GPG

When not setting the GPG keys as parameters (see above), these variables can be used to configure key generation on the workspace:

- `aptly_gpg_realname`: String name of the user to which the key belongs (default: 'Aptly on Research Cloud').
- `aptly_gpg_useremail`: String email of the user to which the key belongs (default: `aptly@localhost`).
- `aptly_gpg_algo`: String algorithm to use for key generation, e.g. `rsa4096` (default: `future-default`, which utilizes the algorithm that is planned to be used in future GPG releases).
- `aptly_gpg_expire`: Integer days after which the key expires (default: 360).
- `aptly_gpg_passphrase`: String passphrase with which to protect the private key (default: `None`). **Note: creating a passphrase-protected key is possible, but not yet supported, as the aptly role currently does not allow importing a key with a passphrase.**


## See also

Role [aptly_add](../roles/aptly_add.md)

Two external roles are used. See the README in their respective directories for documentation:

* role [hetzner.aptly](https://github.com/UtrechtUniversity/researchcloud-items/tree/main/playbooks/roles/ext/hetzner.aptly)
* role [juju4.gpgkey_generate](https://github.com/UtrechtUniversity/researchcloud-items/tree/main/playbooks/roles/ext/juju4.gpgkey_generate)

## History
2023 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)