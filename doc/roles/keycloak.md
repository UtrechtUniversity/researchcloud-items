# Role keycloak
[back to index](../index.md#Roles)

## Summary
[Keycloak](https://keycloak.org) is an open source identity and access management system.
It supports SAML and OIDC.

## License:
MIT

## Requires
Ubuntu operating system with desktop environment.

## Description
Installs Keycloak as a systemd service. Keycloak is installed along with a jboss
application server. Please note that the configuration is suitable for client
application development, testing and training purposes only. Production use will require
further configuration adjustments.

The service is accessible to local users on `http://localhost:8180/auth/...`. 
Access to the Keycloak admin console is added to the desktop menu.
The admin user is created with username/password admin/admin.
Other configurations are obtained by setting any of the below Ansible variables in a playbook.

We recommend to combine Keycloak with a web server (nginx) as a reverse proxy to add
internet access and encrypt all communication. Just add role 
[keycloak_behind_nginx](./keycloak_behind_nginx.md) to your playbook.

## Variables
The following variables and defaults are available:
```
keycloak_version: "15.0.2"
keycloak_tardir: "https://github.com/keycloak/keycloak/releases/download/{{ keycloak_version }}/"
keycloak_tarfile: "keycloak-{{ keycloak_version }}.tar.gz"
keycloak_dir: "/var/lib/keycloak/"
keycloak_jboss_home: "{{ keycloak_dir }}keycloak-{{ keycloak_version }}"
keycloak_jboss_log: "{{ keycloak_jboss_home }}/standalone/log"
keycloak_bind_port: "8180"
keycloak_bind_address: "127.0.0.1"
keycloak_admin_username: "admin"
keycloak_admin_password: "admin"
keycloak_create_admin: True
``` 

## See also
Role [keycloak_behind_nginx](./keycloak_behind_nginx.md).


## History
2019 Written by Andre Lohmann   
2021 Adapted for use with SURF ResearchCloud by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
