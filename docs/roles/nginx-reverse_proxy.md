# Role reverse_proxy
[back to index](../index.md#Roles)

## Summary

This role can be added to any configuration that starts a webapp that listens on localhost, and make that webapp approachable from the internet at the workspace's FQDN, optionally including SRAM authentication.

It builds on top a standard SRC [nginx](https://nginx.org/en/) environment to define [reverse proxies](https://en.wikipedia.org/wiki/Reverse_proxy), allowing one to:

* utilize the workspace's SSL certificate for its FQDN (e.g. https://myworkspace.myco.src.surf-hosted.nl) to serve webapplications behind a reverse proxy.
* easily utilize various kinds of authorization for webapplications running on a workspace
  * using SRAM
  * using HTTP basic auth.

This assumes the standard https nginx server has been configured using the [SRC-Nginx](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) component, and so that `/etc/nginx/app-location-conf.d/authentication.conf` exists.

## Requires

Debian/Ubuntu operating system.

## Description

1. Adds location definitions to `/etc/nginx/app-location-conf.d/` that define reverse proxies
2. Optionally generates `htpasswd` files for HTTP basic auth.
3. Restarts nginx.
 
## Variables

All these variables are required:

- `nginx_reverse_proxy_locations`: Required. List of dict objects defining the reverse proxy. Examples:
```yaml
- name: root # required
  location: / # required
  backend: http://localhost:8000/ # required -- the webapp running on localhost
  # auth: # setting the auth attribute is not required
  # The options below correspond to nginx reverse proxy options: https://nginx.org/en/docs/http/ngx_http_proxy_module.html
  proxy_read_timeout: 
  proxy_connect_timeout:
  proxy_send_timeout:
  send_timeout:
  x_forwarded_for:
  proxy_redirect: 
- name: basicauthlocation
  location: /test_basicauth/ # uri
  backend: http://localhost:8000/ # the webapp running on localhost
  auth:
    type: basic
    auth_info: myfile1 # which of the htpasswd files to use for auth, see the nginx_reverse_proxy_auth_info variable
- name: sramauthlocation
  location: /test_sramauth
  backend: http://localhost:8000/ # the webapp running on localhost
  auth:
    type: sram
- name: api
  location: /test_sramauth/api
  backend: http://localhost:8000/ # the webapp running on localhost
  auth:
    type: noauth # explicitly disables auth for the location -- useful to make exceptions for sublocations of otherwise protected locations

```
- `htpasswd_location`: String. Where to store and look for `htpasswd` files. Default: `/etc/nginx/passwd`.
- `nginx_reverse_proxy_auth_info`: Optional. List of dict objects defining `htpasswd` files for use with HTTP basic auth. These files will be generated using the provided username/password combinations. Example:

```yaml
- name: myfile1 # will be stored under <htpasswd_location>/myfile1
  username: tester
  password: letmein
- name: myfile1,
  username: tester2
  password: letmein
- name: myfile2
  username: tester2
  password: letmein
```

## See also

## History
2024 Written by Dawa Ometto (Utrecht University)


[back to index](../index.md#Roles)
