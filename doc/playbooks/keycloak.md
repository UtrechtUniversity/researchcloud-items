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
Requests areforward by nginx as a remote proxy to an
application server running Keycloak.

Keycloak admins are required to login to the Linux server on `https://<hostanme>/`
and access Keycloak via the desktop menu. 

## Variables

## See also
[keycloak](../roles/keycloak.md).

## History
2021 Written by Ton Smeele (Utrecht University)

[back to index](../index.md#Playbooks)
