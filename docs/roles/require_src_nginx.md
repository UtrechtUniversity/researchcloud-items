# Role require_src_nginx
[back to index](../index.md#Roles)

## Summary

A simple role that applies some heuristics to determine if the [SRC-Nginx component](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) is installed, and Nginx is active. If not, this role will fail and exit the playbook with a message to the user explaining that SRC-Nginx is required.

This is useful for roles that depend on the specific Nginx configuration provided by that component: for instance, the [nginx_reverse_proxy](./nginx_reverse_proxy.md) role relies on the presence of the configuration that allows for SRAM authentication.

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
