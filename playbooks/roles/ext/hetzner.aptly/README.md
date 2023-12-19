# Ansible Role - Aptly

[![CI](https://github.com/hetznercloud/ansible-role-aptly/workflows/CI/badge.svg?event=push)](https://github.com/hetznercloud/ansible-role-aptly/actions?query=workflow%3ACI)

Install and configure Aptly (The "Swiss army knife for Debian repository management") automatically via Ansible.

## Requirements

* A pre-generated GPG key for signing packages

## Dependencies

* `jmespath` (`pip3 install jmespath`)
* `community.general.json_query` (for mirror state logic)

## Role variables

``` yaml
aptly__repo: 'squeeze'
```

The repository has to be either `squeeze` or `nightly`.

```yaml

aptly__user: 'aptly'
aptly__groups:
  - 'www-data'
aptly__user_home_directory: '/srv/aptly'
aptly__user_shell: '/bin/bash'
```

By default, the role will create a separate user using `/srv/aptly` as home directory for the whole aptly processing. The user must be a member of `www-data` if the data should be served via nginx or apache2. This can also be an empty list.

``` yaml
aptly__become_method: ansible.builtin.su
```

Ansible needs to run some tasks using the aptly user (e.g. adding gpg keys). By default, the role will use the `su` method. Depending on the host configuration, this may need to be changed to the proper become plugin. For more information, please see the [Ansible docs](https://docs.ansible.com/ansible/latest/plugins/become.html#become-plugins).

``` yaml
aptly__gpg_private_key: |
  -----BEGIN PGP PRIVATE KEY BLOCK-----

  .....................................
  -----END PGP PRIVATE KEY BLOCK-----
aptly__gpg_public_key: |
  -----BEGIN PGP PUBLIC KEY BLOCK-----

  ....................................
  -----END PGP PUBLIC KEY BLOCK-----

aptly__api_enable: true
aptly__apt_listen_address: "127.0.0.1"
aptly__api_listen_port: 9091
aptly__api_extra_arguments:
  - "-no-lock"
```

By default, the API of the aptly server will be enabled and started locally. The API will be required for mirrors as the update script uses the asynchronous scheduling feature which is only available via API.

## Example config

```yaml
---
aptly__mirrors:
  - name: ddebs-ubuntu-jammy
    publish_prefix: ddebs
    no_block_mirror_task: true
    label: test
    origin: asdf.movie
    distribution: jammy # this needs to be set, no matter if childrens exist or not
    childrens: # Either set it with childrens or not
      - name: main
        distribution: jammy
        archive_url: "http://ddebs.ubuntu.com"
        state: present
        components:
          - main
        architectures:
          - amd64
          - arm64
        keys:
          - string: ""
          - file: ""
          - url: ""
        filter: "mysql-client (>= 3.6)"
        filter_with_deps: true
        ignore_signatures: false
        with_sources: true
        with_installer: false
        with_udebs: false
  - name: ceph-quincy-focal
    publish_prefix: ceph-quincy
    no_block_mirror_task: true
    distribution: focal
    archive_url: https://download.ceph.com
    label: test
    origin: asdf.movie
    state: present
    components:
      - main
    keys:
      - url: ""

aptly__repositories:
  - name: jammy
    distribution: jammy
    label: cloud_platform
    state: present
    components:
      - main
      - experimental
    architectures:
      - amd64
      - arm64
```

## Example playbook

``` yaml
---
- hosts: all
  roles:
    - role: hetzner.aptly
```

## License

GPL-3.0
