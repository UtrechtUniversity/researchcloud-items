# Best practices

## Test-driven development
While unit tests are not present in these plugins made for SURF Research Cloud, there are other tools that can help you: [Ansible testing modules](https://docs.ansible.com/ansible/latest/reference_appendices/test_strategies.html), [Ansible Lint](https://ansible-lint.readthedocs.io/en/latest/) and [Ansible Provisioning in Vagrant VMs](https://www.vagrantup.com/docs/provisioning/ansible).
Try to incorporate as much of TDD into developing playbooks and roles: first determine when your code is succesfull or when it should fail, and then code around those requirements.

## Specific roles
Reuse the roles defined inside this repository for certain tasks, instead of doing it yourself. Especially for SURF Research Cloud, these roles come in handy:

- Use [runonce](roles/runonce.md) to have a piece of code ran once the first time a user logs in.
- Use [desktop_file](roles/desktop_file.md) to create menu and desktop entries.
- Use [fact_regular_users](roles/fact_regular_users.md) to gather a list of all users on the system.
- Use [git_clone](roles/git_clone.md) to let users clone a git repository into a environment through arguments.

## Keep userspace and system-wide seperate
Especially for python-related software: most times, keeping everything seperate and private for all users is the best default approach. Let users select their own versions to avoid clashes.
