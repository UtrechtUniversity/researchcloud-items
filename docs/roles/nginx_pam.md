# Role nginx_pam
[back to index](../index.md#Roles)

## Summary
Installs support for pam-based authentication with the nginx
webserver. 

## Requires
Linux Debian/Ubuntu distribution in SURF ResearchCloud.

## Description
Installs the nginx-full package which contains the nginx-pam module.. 
Ensures that the nginx processes can be used to check TOTP passwords
in SURF Research Cloud.

Example nginx configuration:
```
   location /restricted {
      auth_pam "Realm for secured info";
      auth_pam_service_name "login";
      ...
   }
```

## Variables
n/a

## See also
- [ngx_http_auth_pam module](https://github.com/sto/ngx_http_auth_pam_module)  

## History
2022 Written by Ton Smeele (Utrecht University)


[back to index](../index.md#Roles)
