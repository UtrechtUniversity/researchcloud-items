This directory contains molecule tests for the following roles:

- robotuser
- sshfs_configrobot
- sshfs_mount
- sshfs_cleanup

Since these roles are meant to be executed together, it only
makes sense to test them in one scenario.

The `robotuser` role contains the test directory, while the
other roles contain symlinks to it. This is to ensure tests
are run in CI when changing something in any of these roles.
