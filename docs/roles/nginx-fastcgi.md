# Role nginx_fastcgi
[back to index](../index.md#Roles)

## Summary
Adds support for execution of shell script with the nginx
webserver. 

## Requires
Workspace that has nginx installed.

## Description
Installs the fcgiwrap package and creates a /var/www/cgi-bin directory
where scripts can be placed.  Installs an example script within this
directory.

An example nginx configuration to execute a script "hello" at 
location /example/hello would be: 
```
  location /example {
     gzip off;
     root /var/www/cgi-bin;
     fastcgi_pass unix:/var/run/fcgiwrap.socket;
     include /etc/nginx/fastcgi_params;
     fastcgi_param SCRIPT_FILENAME /var/www/cgi-bin$fastcgi_script_name;
  }
```

## Variables
n/a

## See also
- [ngx_http_fastcgi module](https://nginx.org/en/docs/http/ngx_http_fastcgi_module.html)  

## History
2022 Written by Ahmad Hesam (SURF) and Ton Smeele (Utrecht University)


[back to index](../index.md#Roles)
