# Playbook reverse_proxy
[back to index](../index.md#Playbooks)

## Summary

This component can be added to any configuration that contains a webapp that listens on localhost, and make that webapp approachable from the internet at the workspace's FQDN, optionally including SRAM authentication.

It builds on top a standard SRC [nginx](https://nginx.org/en/) environment to define [reverse proxies](https://en.wikipedia.org/wiki/Reverse_proxy), allowing one to:

* utilize the workspace's SSL certificate for its FQDN (e.g. https://myworkspace.myco.src.surf-hosted.nl) to serve webapplications behind a reverse proxy.
* easily utilize various kinds of authorization for webapplications running on a workspace
  * using SRAM
  * using HTTP basic auth.

When developing your own component for a webapp, it may be better to utilize the [reverse proxy role](../roles/nginx_reverse_proxy.md) in your own component directly, rather than adding this component to a separate component for your webapp in an SRC Catalog Item. However, this component may be useful when wanting to add reverse proxy capabilities to components that you don't control or can't customize further (such as docker or docker-compose components on SRC).

## Requires

* SRC Component: [SRC-Nginx Component](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) must be executed prior to this component.
* OS: Ubuntu or Debian.

## Description

This component allows you to configure a list of *locations* which will be turned into reverse proxies. You can configure the proxy proxy_pass, timeouts and limits, and authentication options, including SRAM authentication and HTTP basic auth.

When using HTTP basic auth, you must set the `htpasswd` attribute to refer to a file existing under the location `/etc/nginx/passwd/`. You can either:

1. Create this file yourself (e.g. in a different component).
2. Let this component create it for you. **In that case, you must set the relevant information in a CO secret.** See the `reverse_proxy_auth_info` variable below.

## Variables

`reverse_proxy_locations`: Required. String. A list of YAML dict objects defining reverse proxy locations. Example:

```yaml
- {name: test_noauth, location: /, proxy_pass: "http://localhost:8000"} # no authentication for /
- {name: test_basicauth, location: = /test_basicauth, auth: basic, htpasswd: myfile1, proxy_pass: "http://localhost:8000/" } # http basic auth using the file myfile1 (see below)
- {name: test_sramauth, location: /test_sramauth, auth: sram, proxy_pass: "http://localhost:8000/"} # sram auth for /test_sramauth
- {name: test_authoff, location: = /test_basicauth/api, auth: noauth, proxy_pass: "http://localhost:8000/bin/"} # turn off sram auth for sublocation /test_sramauth/api
```

You can add keys to these dicts corresponding to nginx configuration detectives. E.g. `alias: /bla` will add an `alias /bla;` directive to the configuraiton. See the relevant [role](../roles/nginx_reverse_proxy.md) for more documentation of options and defaults.

`reverse_proxy_auth_info`: Optional. String. A list of YAML objects defining authentication information that will be turned into valid htpasswd files. The name of the htpasswd file should correspond to the one set in the `reverse_proxy_locations` variable. Example:

```yaml
- {name: myfile1, username: test, password: letmein}
- {name: myfile1, username: test2, password: letmein} # second user for myfile1
- {name: myfile2, username: test3, password: letmein} # a second file myfile2
```
**This parameter should be [set as a CO secret](https://servicedesk.surf.nl/wiki/display/WIKI/Secrets+and+workspace+info%3A+special+parameter+source+types). By default, the secret that will be looked up is called `reverse_proxy_auth_info`, but you may change this in your Catalog Item.*

**If you want to use a single username/password for a reverse proxy location, you can leave the `reverse_proxy_auth_info` parameter empty, and instead use the default credentials, as described below.**

If one of the `htpasswd` files defined in `reverse_proxy_locations` is not found in `reverse_proxy_auth_info`, that htpasswd file will be created using the following default credentials, which can be overriden:

- `basic_auth_default_username`: Optional. String. The default username to be used if none is set in `reverse_proxy_auth_info`. Default: `''`.
- `basic_auth_default_password`: Optional. String. The default password to be used if none set in `reverse_proxy_auth_info`. Default: `''`.

## See also

- Role [nginx_reverse_proxy](../roles/nginx_reverse_proxy.md)
- Role [require_src_nginx](../roles/require_src_nginx.md)

## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
