# Playbook keycloak
[back to index](../index.md#Playbooks)

## Summary
Installs [keycloak](https://www.keycloak.org/) 
as an identity and access management service.
NB: Configuration suitable for test/training purposes only.

## Requires
Ubuntu operating system with desktop environment, and
a SURF ResearchCloud configured nginx web server.

## Description
Keycloak is an open source identity and access management service.
It can act as a SAML or OIDC authentication/authorization service.
The playbook installs Keycloak for development, testing and training purposes.
Note that some addtional hardening and configuration will be needed to use
Keycloak in production environments.

Client applications and users access Keycloak services via 
`https://<hostname>/auth/realms/<realm>/`.
Requests are forwarded by nginx (reverse proxy) to an
application server running Keycloak.

Keycloak admins are required to login to the Linux server on `https://<hostname>/`
where they access Keycloak via the desktop menu. 

## Configuration
Nginx fronts Keycloak as a reverse proxy and offloads ssl. 
As a consequence, Keycloak will report its realm endpoints as having 'http' scheme 
instead of 'https'.
To compensate for the proxy, set an alternative frontend url for each realm
that you have added to the system:
```
    Alternative frontend url:  https://<hostname>/auth
```
NB: Do *NOT* update the *master* realm Alternative frontend url!! 

## Variables

## See also
Role [keycloak](../roles/keycloak.md).   
Role [keycloak_behind_nginx](../roles/keycloak_behind_nginx.md).

## History
2021 Written by Ton Smeele (Utrecht University)

[back to index](../index.md#Playbooks)
