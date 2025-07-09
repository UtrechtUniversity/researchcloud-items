# Role nginx_reverse_proxy
[back to index](../index.md#Roles)

## Summary

This role is a convenience role for creating [reverse proxies](https://en.wikipedia.org/wiki/Reverse_proxy) on top of the nginx webserver that is installed by the standard [SRC-Nginx](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) component.

It does not implement any new functionality itself, and rather essentially wraps the [nginx_location](./nginx_location.md) role such that for every defined location block, the `include_reverse_proxy_defaults` option is set to `true`. This enables a few common reverse proxy settings and headers:

```
proxy_read_timeout 300;
proxy_connect_timeout 300;
proxy_send_timeout 300;
send_timeout 300;
client_max_body_size' 10G;
proxy_redirect off;


proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection $connection_upgrade;
proxy_set_header Host $host;

```

Note that you can still override each of these options:

```yaml
- name: mylocation
  location: /mylocation
  proxy_pass: http://localhost:8080 # NB: you must still set proxy_pass yourself!
  proxy_redirect: override
  send_timeout: '' # override the directive, setting to '' will ensure the directive is not printed at all
  proxy_set_header:
    X-Real-IP: override-the-default
```

For other settings, including how to set authentication for your reverse proxy using HTTP basic auth, or external authentication using SRAM, see the role [nginx_location](./nginx_location.md).

## Requires

- Debian/Ubuntu operating system.
- [SRC-Nginx](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) component installed

## See also

- Role [nginx_location](./nginx_location.md)

## History
2025 Written by Dawa Ometto (Utrecht University)


[back to index](../index.md#Roles)
