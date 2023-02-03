# Playbook transferuser
[back to index](../index.md#Playbooks)

## Summary
Allows users to transfer data between a remote host and the workspace using
a dedicated ssh keypair and Linux account. This is useful in cases where the user
does not need or seeks to avoid to store her own private key on the remote host.  

## Properties
Status: Experimental, use with caution  
Suitability: Sensitive data         

## Requires
Linux with SUDO enabled. To use the transfer account, workspace users need Sudo rights.

## Description
On the SURF Research Cloud workspace, users can execute the command "transfer on" to 
install a transfer key (=public key). After this preparation step, the user can initiate ssh type 
commands such as scp on a remote host to transfer files to the workspace (to a
fixed workspace user account named "transfer").
The transfer key is the public key part of a key pair that the user must have generated
and installed on the remote host (for instance using the command ssh-keygen).  


## Variables
It is possible to customize/override the name of the Linux user "transfer" and the commandline
script "transfer". See the transferuser role for details.

## See also
Role [transferuser](../roles/transferuser.md)

## History
2023 Written by Ton Smeele (Utrecht University)

[back to index](../index.md#Playbooks)
