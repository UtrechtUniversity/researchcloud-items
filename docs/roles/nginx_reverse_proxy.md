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

- `nginx_reverse_proxy_locations`: Required. List of dict objects defining the reverse proxy. Examples:

```yaml
- name: root # required
  location: / # required
  proxy_pass: http://localhost:8000/ #  the webapp running on localhost -- not required! you can instead use e.g. 'alias' as well.
  add_headers: # headers that nginx will add to the response
    foo: bar
    bar: foo
  # auth: # setting the auth attribute is not required
  # The options below are example of common nginx options
  # Any "key: value" pair you add will be translated to "key value;" in the nginx config
  proxy_read_timeout: # Default when proxy_pass is set: 300
  proxy_connect_timeout: # Default when proxy_pass is set: 300
  proxy_send_timeout: # Default when proxy_pass is set: 300
  send_timeout: # Default when proxy_pass is set: 300
  x_forwarded_for: # Default when proxy_pass is set: '$proxy_add_x_forwarded_for'
  proxy_redirect: # Default when proxy_pass is set: 'off'
  your_directive_here: # Will translate to "your_option_here <value>;".
- name: basicauthlocation
  location: /test_basicauth/ # uri
  proxy_pass: http://localhost:8000/ # the webapp running on localhost
  auth: basic
  htpasswd: myfile1 # which of the htpasswd files to use for auth, see the nginx_reverse_proxy_auth_info variable
- name: sramauthlocation
  location: /test_sramauth
  proxy_pass: http://localhost:8000/ # the webapp running on localhost
  auth: sram
- name: api
  location: /test_sramauth/api
  proxy_pass: http://localhost:8000/ # the webapp running on localhost
  auth: noauth # explicitly disables auth for the location -- useful to make exceptions for sublocations of otherwise protected locations
- name: default_basic_auth_credentials
  location: /test_default_credentials
  auth: basic
  # If you set a htpasswd file that is not defined in the nginx_reverse_proxy_auth_info variable, the file will be created with the default credentials (see below):
  htpasswd: not_defined_in_nginx_reverse_proxy_auth_info
```

- `htpasswd_location`: String. Where to store and look for `htpasswd` files. Default: `/etc/nginx/passwd`.
- `nginx_reverse_proxy_auth_info`: Optional. List of dict objects defining `htpasswd` files for use with HTTP basic auth. These files will be generated using the provided username/password combinations. Example:

```yaml
- name: myfile1 # will be stored under <htpasswd_location>/myfile1
  username: tester
  password: letmein
- name: myfile1
  username: tester2
  password: letmein
```

When you have defined a location with a `htpasswd` attribute in the `nginx_reverse_proxy_locations`, but this `htpasswd` file does not occur in the `nginx_reverse_proxy_auth_info` parameter, that htpasswd will be created with the default credentials:

- `nginx_reverse_proxy_default_username`: String. Standard username to add to an httaccess file if none is explicitly provided (see `nginx_reverse_proxy_auth_info`). Default: `''`.
- `nginx_reverse_proxy_default_passwrod`: String. Standard password to add to an httaccess file if none is explicitly provided (see `nginx_reverse_proxy_auth_info`). Default: `''`.


## See also

## History
2024 Written by Dawa Ometto (Utrecht University)


[back to index](../index.md#Roles)
