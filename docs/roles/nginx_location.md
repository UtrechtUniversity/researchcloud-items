# Role nginx_location
[back to index](../index.md#Roles)

## Summary

This role can be used to generate [nginx](https://nginx.org/en/) location blocks that will be served by the nginx webserver running on a workspace. This way, you can serve pages to the internet (reachable at the workspace's FQDN), create a [reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy) that exposes an application running on localhost, easily add authentication, and anything else you can do with nginx! In particular, it allows you to:

* utilize the workspace's SSL certificate for its FQDN (e.g. https://myworkspace.myco.src.surf-hosted.nl) to serve webapplications behind a reverse proxy.
* easily utilize various kinds of authorization for webapplications running on a workspace
  * using SRAM
  * using HTTP basic auth.

The role does not install nginx, and instead assumes that it is installed by the standard [SRC-Nginx](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) component.

Please see the examples below to understand the syntax for location block configuration, including for SRAM authentication.

## Requires

- Debian/Ubuntu operating system.
- [SRC-Nginx](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) component installed

## Description

1. Adds location definitions to `/etc/nginx/app-location-conf.d/` that define reverse proxies
2. Optionally generates `htpasswd` files for HTTP basic auth.
3. Restarts nginx.
 
## Variables

- `nginx_location_locations`: Required. List of dict objects defining the locations. Examples:

```yaml
# first location
- name: root # required
  location: / # required
  proxy_pass: http://localhost:8000/ #  the webapp running on localhost -- not required! you can instead use e.g. 'alias' as well.
  auth: noauth # Special key, see the other location blocks below for auth examples.
  include_reverse_proxy_defaults: false # Special key. Set to true to include some sane default proxy configurations regarding timeouts etc. See the [nginx_reverse_proxy](./nginx_reverse_proxy.md) role. Default: false
  # The options below are example of common nginx options
  # Any "key: value" pair you add will be translated to a "key value;" directive in the nginx config
  client_max_body_size: 10G
  send_timeout: 300
  # You can also use nested dicts
  proxy_set_header:
    header1: foo
    header2: bar
  # will yield:
  # proxy_set_header header1 foo;
  # proxy_set_header header2 bar;
  add_header: # headers that nginx will add to the response
    foo: bar
    bar: foo
  # will yield:
  # add_header header1 foo;
  # add_header header2 bar;
  #since Jinja dictionaries are unordered, the order in which directives are rendered cannot be guaranteed.
  # if order needs to be preserved, you can use a list, with each list item an arbitrary dict. For example:
  _foo: # starting key with a _ means they key will not be rendered as part of the directive
   - foo_enabled: true
   - foo_setting: bar
  # ...will render foo_enabled true; foo_setting bar;
- name: basicauthlocation # second location, with http basic auth
  location: /test_basicauth/ # uri
  auth: basic
  htpasswd: myfile1 # which of the htpasswd files to use for auth, see the nginx_location_auth_info variable
- name: sramauthlocation # third location, with SRAM auth
  location: /test_sramauth
  auth: sram
  auth_sram_header: REMOTE_USER # Special key. Optionally specify which header should be filled with the name of the externally authenticated user. Default: REMOTE_USER
- name: api # fourth location, without auth
  location: /test_sramauth/api
  auth: noauth # explicitly disables auth for the location -- useful to make exceptions for sublocations of otherwise protected locations
- name: default_basic_auth_credentials # fifth location, http basic auth with default credentials
  location: /test_default_credentials
  auth: basic
  # If you set a htpasswd file that is not defined in the nginx_location_auth_info variable, the file will be created with the default credentials (see below):
  htpasswd: not_defined_in_nginx_location_auth_info
```

- `nginx_location_htpasswd_path`: String. Where to store and look for `htpasswd` files. Default: `/etc/nginx/passwd`.
- `nginx_location_auth_info`: Optional. List of dict objects defining `htpasswd` files for use with HTTP basic auth. These files will be generated using the provided username/password combinations. Example:

```yaml
- name: myfile1 # will be stored under <htpasswd_location>/myfile1
  username: tester
  password: letmein
- name: myfile1
  username: tester2
  password: letmein
```

When you have defined a location with a `htpasswd` attribute in the `nginx_location_locations`, but this `htpasswd` file does not occur in the `nginx_location_auth_info` parameter, that htpasswd will be created with the default credentials:

- `nginx_location_default_username`: String. Standard username to add to an httaccess file if none is explicitly provided (see `nginx_location_auth_info`). Default: `''`.
- `nginx_location_default_password`: String. Standard password to add to an httaccess file if none is explicitly provided (see `nginx_location_auth_info`). Default: `''`.


## See also

- Role [nginx_reverse_proxy](./nginx_reverse_proxy.md)

## History
2024-2025 Written by Dawa Ometto (Utrecht University)


[back to index](../index.md#Roles)
