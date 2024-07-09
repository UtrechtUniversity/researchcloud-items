# Playbook transferuser
[back to index](../index.md#Playbooks)

## Summary
Allows users to transfer data between a remote host and the workspace using SSH (secure shell).
This component sets up a special user with its own SSH keys to facilitate the transfer.
This is useful in cases where the user  does not need or seeks to avoid to store her own
private key on the remote host.  

Suitability: sensitive data.      

## Requires

- Unix OS
- sudo enabled for users who use the `transfer` command

## Description

- On the SURF Research Cloud workspace, users can execute the command `transfer on` to 
install a public key for the transfer user. The script will ask the user to input
an SSH public key. This should be public key corresponding to a private key on the 
machine that the user wants to login to the workspace from (let's call this machine: "the remote host").
If no keypair exists on the remote host, it can be generated e.g. with `ssh-keygen`.
- After this preparation step, the user can initiate ssh type 
commands such as `scp` on a remote host to transfer files to the workspace. For instance:

```
scp myfile.txt transfer@<workspace_ip>:~/mycopiedfile.txt
# transfers the file `myfile.txt` on the machine where `scp` is executed to `/home/transfer/mycopiedfile.txt` on the workspace where the `transfer on` command was run.
```

- When all file transfers are done, users should execute command `transfer off`
to disable further use of the keypair based access.


## Variables
It is possible to customize/override the name of the Linux user "transfer" and the commandline
script "transfer". See the transferuser role for details.

## See also
Role [transferuser](../roles/transferuser.md)

## History
2023 Written by Ton Smeele (Utrecht University)

[back to index](../index.md#Playbooks)
