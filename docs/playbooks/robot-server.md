# Playbook robot-server
[back to index](../index.md#Playbooks)

## Summary
Deploys a robot server, that other workspaces can connect to (see [robotuser](./robotuser.md)). 

## Requires
Debian-like OS

## Description

Deploys a robot server, that other workspaces can connect to (see [robotuser](./robotuser.md)). Will create a fresh SSH keypair that workspaces will use to communicate with the robot server.

### Redeployment

It is good practice to redeploy the robot server periodically. This ensures the catalog item is functional, and rotates the used SSH keys. After redployment, the client components need to be updated with the new SSH key for the robotuser!

Steps:

1. Delete current robot-server workspace (need to free the reserve IP address)
2. Create new workspace
    - attach the robotserver storage
    - attach the reserved IP for the robotserver
    - CO: ResearchCloud Development
    - Wallet: "SRC account for ResearchCloud Development, Roboserver Image"
    - Ensure deletion time far in the future :)
3. Update private key in robot client components: robot-client, Robot Copy
    * connect to the new robot server via SSH. This will throw a warning about the fact that the server's host key has changed, if you had previously connected to the old server!
    * `[sudo] cat /home/uurobot/.ssh/id_rsa`
    * copy and update components
    * don't forget to promote the new `Development` versions of the component to `Live`!
4. Test: roll out a catalog item that uses the robot server (e.g. SAS, Matlab)


## Variables
```
robotuser_name: String. Default: `uurobot`. Name of the user that workspaces can connect to this server as.
robotuser_generate_ssh_key: Boolean. Default: `true`. Whether to generate a fresh SSH keypair.

```

## See also
Role [sshfs_configrobot](../roles/sshfs_configrobot) robot used to mount remote filesystem
Playbook [robotuser](./robotuser.md) playbook used to connect to a robotserver


## History
2021-2025 Written by Ton Smeele and Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
