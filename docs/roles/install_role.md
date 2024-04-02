# Role install_role
[back to index](../index.md#Roles)

## Summary

A utility role that allows you to install external roles to be used in playbooks on SRC.
Context is that the SRC platform currently does not support external dependencies for components, for instance via specification of an Ansible `requirements.yml` file.
So as a workaround, this role will 'manually' install external role dependencies using `ansible-galaxy`.

Note: there is no support for installing external collections at the moment.
This because the Ansible version in use on SRC is outdated and does not support the current collections API.

Note for usage: when using external roles, best practice is to depend on a specific (semantic) version for 'official' roles,
and a specific git commit or git tag for 'unoffical' roles.
The latter is a security precaution: specifying a git revision will guard against installing a later version of
the role that possibly contains harmful code.

## Requires

Works on all systems that have `ansible-galaxy` installed.

## Description

1. Include this role in your playbook as follows:

```yaml
- name: Install role dependencies
  include_role:
    name: install_role
  vars:
    install_role_roles:
    # Just some test roles:
      - ANXS.postgresql
      - git+https://github.com/ANXS/generic-users.git,1c6c6ee
```

Your playbook, or other roles you reference, may now make us of the roles installed in this way.

## Variables

* list `install_role_roles`: Required. A list of String ansible role dependencies as resolved by `ansible-galaxy install`.
For instance:

```yaml
install_role_roles:
    - ANXS.postgresql
    - git+https://github.com/ANXS/generic-users.git,1c6c6ee
```

## See also

## History

2024 Written by Dawa Ometto (Utrecht University)



[back to index](../index.md#Roles)
