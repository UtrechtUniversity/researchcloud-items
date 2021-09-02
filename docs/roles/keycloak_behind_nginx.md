# Role keycloak_behind_nginx
[back to index](../index.md#Roles)

## Summary
Adds to nginx a reverse proxy configuration that allows internet users and applications
to access Keycloak services, for instance for authentication purposes. 

## Requires
Ubuntu operating system with desktop environment, nginx webserver

## Description
Keycloak will be accessible to client applications and regular users as an 
internet service on `https://<hostname>/auth/realms/<realmname>/`.

Internally HTTP requests are forwarded to a Keycloak process listening on port `8180`.

NB: The Keycloak admin console is not accessible via the reverse proxy. It requires
admins to login to the Keycloak server as remote desktop and use the desktop menu. 

## Variables
Compatibility with this role require the variables `keycloak_bind_port:"8180"` 
and `keycloak_bind_address:"127.0.0.1"` to remain unchanged.
 

## See also
Role [keycloak](./keycloak.md).


## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
