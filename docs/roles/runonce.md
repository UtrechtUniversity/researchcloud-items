# Role runonce
[back to index](../index.md#Roles)

## Summary
Schedules so called "userspace application" scripts to run once (by each user), 
upon first login of the user.

## Requires

- Linux flavor operating system.
- `bash` or `zsh` shell.

## Description
Bash/zsh scripts that need to run can be placed in directory `/etc/runonce.d`,
either directly or within a subdirectory. Upon the user's first login, 
the scripts will be run (only once) in sequence, sorted alphabetically by pathname.

Script(s) output (`stdout` and `stderr`) is saved in a file `~/.runonce.log`.

### How it works

The script `/etc/profile.d/runonce.sh` is triggered whenever a user starts a [login
shell](https://help.gnome.org/users/gnome-terminal/stable/pref-login-shell.html.en). The script checks whether the shell is also an [interactive shell](https://unix.stackexchange.com/questions/43385/what-do-you-mean-by-interactive-shell), and executes
the scripts in `/etc/runonce.d/` if so.

On Desktop workspaces, `/etc/profile.d/runonce.sh` is triggered by a special `.desktop`
item placed in `/etc/xdg/autostart`, which is started every time a user logs in
to the desktop.
 
## Variables

## See also
Role [userspace_applications](./userspace_applications.md) can be used to store
(sets of) your runonce scripts.

## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
