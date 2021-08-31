# Role uwsgi
[back to index](../index.md#Roles)

## Summary
Installs the [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/) subscription server
and its Python3 plugin as a service behind nginx.

## Requires
nginx web server, as preconfigured by SURF.

## Description
The uwsgi services translate HTTP requests into UWSGI protocol requests, suitable
for consumption by for instance Python web applications.

The nginx web server is used as a reverse proxy, all HTTP(S) requests that have prefix `/w/`
are routed to uwsgi. 

## Variables

## See also
The `files` section of this role includes an example file for adding a Python application
to uwsgi.

## History
2021 Written by Ton Smeele (Utrecht university)



[back to index](../index.md#Roles)
