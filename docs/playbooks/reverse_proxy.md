# Playbook reverse_proxy
[back to index](../index.md#Playbooks)

## Summary

This component can be added to any configuration that contains a webapp that listens on localhost, and make that webapp approachable from the internet at the workspace's FQDN, optionally including SRAM authentication.

It builds on top a standard SRC [nginx](https://nginx.org/en/) environment to define [reverse proxies](https://en.wikipedia.org/wiki/Reverse_proxy), allowing one to:

* utilize the workspace's SSL certificate for its FQDN (e.g. https://myworkspace.myco.src.surf-hosted.nl) to serve webapplications behind a reverse proxy.
* easily utilize various kinds of authorization for webapplications running on a workspace
  * using SRAM
  * using HTTP basic auth.

When developing your own component for a webapp, it may be better to utilize the [reverse proxy role](../roles/nginx-reverse_proxy.md) in your own component directly, rather than adding this component to a separate component for your webapp in an SRC Catalog Item. However, this component may be useful when wanting to add reverse proxy capabilities to components that you don't control or can't customize further (such as docker or docker-compose components on SRC).

## Requires

* SRC Component: [SRC-Nginx Component](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) must be executed prior to this component.
* OS: Ubuntu or Debian.

## Description

This component allows you to configure a list of *locations* which will be turned into reverse proxies. You can configure the proxy backend, timeouts and limits, and authentication options, including SRAM authentication. You can also pass in a list *authentication information* that can be used to perform http basic auth.
## Variables

`reverse_proxy_locations`: String of YAML dict objects (one on every newline) defining reverse proxy locations. Example:

```yaml
{name: test_noauth, location: /, backend: "http://localhost:8000"} # no authentication for /
{name: test_basicauth, location: = /test_basicauth, auth: {type: basic, auth_info: myfile1}, backend: "http://localhost:8000/" } # http basic auth using the file myfile1 (see below)
{name: test_sramauth, location: /test_sramauth, auth: {type: sram}, backend: "http://localhost:8000/"} # sram auth for /test_sramauth
{name: test_authoff, location: = /test_basicauth/api, auth: {type: noauth}, backend: "http://localhost:8000/bin/"} # turn off sram auth for sublocation /test_sramauth/api
```

For location attributes allowing you to configure standard nginx reverse proxy options, see the [role documentation](../roles/nginx-reverse_proxy.md).

`nginx_reverse_proxy_auth_info`: String of YAML dict objects (one on every newline) defining authentication information that will be stored in an htpasswd file. You can pass the name of each htpasswd file to the `auth_info` attribute of the `auth` attribute of a location. Example:

```yaml
# Reference myfile1 etc. in the location definitions: `auth: {type: basic, auth_info: myfile1}`
{name: myfile1, username: test, password: letmein}
{name: myfile1, username: test2, password: letmein} # second user for myfile1
{name: myfile2, username: test3, password: letmein} # a second file myfile2
```

## See also

Role [nginx-reverse_proxy](../roles/nginx-reverse_proxy.md)

## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)