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

This component allows you to configure a list of *locations* which will be turned into reverse proxies. You can configure the proxy backend, timeouts and limits, and authentication options, including SRAM authentication and HTTP basic auth. When using HTTP basic auth, you must set the `htpasswd` attribute to refer to a file defined in the `reverse_proxy_auth_info` variable.
## Variables

`reverse_proxy_locations`: String of YAML dict objects (one on every newline) defining reverse proxy locations. Example:

```yaml
- {name: test_noauth, location: /, backend: "http://localhost:8000"} # no authentication for /
- {name: test_basicauth, location: = /test_basicauth, auth: basic, htpasswd: myfile1, backend: "http://localhost:8000/" } # http basic auth using the file myfile1 (see below)
- {name: test_sramauth, location: /test_sramauth, auth: sram, backend: "http://localhost:8000/"} # sram auth for /test_sramauth
- {name: test_authoff, location: = /test_basicauth/api, auth: noauth, backend: "http://localhost:8000/bin/"} # turn off sram auth for sublocation /test_sramauth/api
```

For location attributes allowing you to configure standard nginx reverse proxy options, see the [role documentation](../roles/nginx-reverse_proxy.md).

`reverse_proxy_auth_info`: String of YAML dict objects (one on every newline) defining authentication information that will be stored in an htpasswd file. The name of the htpasswd file should correspond to the one set in the `reverse_proxy_locations` variable. **This parameter should be set as a CO secret.** Example:

```yaml
- {name: myfile1, username: test, password: letmein}
- {name: myfile1, username: test2, password: letmein} # second user for myfile1
- {name: myfile2, username: test3, password: letmein} # a second file myfile2
```

## See also

Role [nginx-reverse_proxy](../roles/nginx-reverse_proxy.md)

## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)