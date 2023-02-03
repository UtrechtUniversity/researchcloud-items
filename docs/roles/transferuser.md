# Role transferuser
[back to index](../index.md#Roles)

## Summary
Allows users to transfer data between a remote host and the workspace 
using a keypair created specifically for the transfer (hence not the 
keypair used for regular logon).  

## Requires
Linux OS with SUDO for users that need access to this service.

## Description
Supports data transfers originating from remote hosts where a user does 
not want to install her private ssh key. Adds a user account "transfer" 
to the workspace. Existing workspace users (sudo rights needed) may use 
the command "transfer on" to be prompted for a transfer key (a public key). 
This transfer key is then installed as "authorized_key" for the transfer 
account. 

To create the transfer key: generate a new keypair on a remote host 
using the ssh-keygen command. This installs the private key in ~/.ssh. 
Use the related public key ~/.ssh/rsa_id.pub as the transfer key (copy/paste 
as input for the transfer command on the workspace). 

After this preparation, the user on the remote host can transfer files 
using scp to the transfer user account on the workspace. 
When all file transfers are done, users should execute command "transfer off"
to disable further use of the keypair based access.


## Variables
transferuser_name: "transfer"   
transferuser_command: "transfer"


## See also
n/a

## History
2023 Written by Ton Smeele (Utrecht University)

[back to index](../index.md#Roles)
