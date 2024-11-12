# External roles

This directory contains open source external roles that have been included as git subtrees. Including them serves a number of purposes:

* we need to adjust the roles to accomodate the fact that on SRC, we presently cannot use FQDNs to specify Ansible modules
* it allows us to remove files from the external roles that we don't need (e.g. `.gitlab`)
* it gives us control over code that is executed

For these reasons, some subtrees are created from forks of the roles (see below).

Licences are included in the directories, or else are specified in the `README`s.

### Repos utilized

* https://github.com/dometto/ansible-role-aptly
* https://github.com/juju4/ansible-gpgkey_generate