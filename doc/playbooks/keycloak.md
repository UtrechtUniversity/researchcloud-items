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
It can act as a SAML or OIDC authorization service.
The playbook installs Keycloak for development, testing and training purposes.
Note that some addtional hardening and configuration will be needed to use
Keycloak in production environments.

Client applications and users access Keycloak via their browser on uri `/auth/...`.
The Keycloak admin console is only accessible to Linux users logged in to the server itself. 
Please see the role [keycloak](../roles/keycloak.md) for further details.

## Variables

## See also

## History
2021 Written by Ton Smeele (Utrecht University)

[back to index](../index.md#Playbooks)
