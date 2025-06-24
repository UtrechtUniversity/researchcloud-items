# Role asreview_server
[back to index](../index.md#Roles)

## Summary

[ASReview](https://asreview.nl/) is an application that uses active learning to facilitate and predict the relevancy of papers during a systematic review.

This role installs the ASReview webapplication. Users in the collaboration will be able to login using SRAM Single Sign-on.

## Requires

- Ubuntu OS
- SURF's [SRC-Nginx](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) component preinstalled

## Description

This role installs the ASReview webapplication. It utilizes the [nginx_reverse_proxy](./nginx_reverse_proxy.md) to activate support for Single Sing-on using SRAM.

## Variables

- `asreview_server_remote_user_header`: String. HTTP header that set by the external authentication provider (SRAM) to authenticate a user. Default: `REMOTE_USER`.
- `asreview_server_remote_user_email_header`: String. HTTP header set by the external authentication provider (SRAM) that containts the authenticated user's email address. Default: `""`.
- `asreview_server_remote_user_name_header`: String. HTTP header set by the external authentication provider (SRAM) that containts the authenticated user's name. Default: `""`.
- `asreview_server_remote_user_affiliation_header`: String. HTTP header set by the external authentication provider (SRAM) that containts the authenticated user's affiliation. Default: `""`.
- `asreview_server_remote_user_default_affiliation`: String. Default affiliation for an authenticated user, if no affiliation was set in an HTTP header. Default: `""`.
- `asreview_server_default_email_domain`: String. Default email domain that will be used to generate an authenticated user's email address, if no email address was set in an HTTP header. Default: `localhost`.
- `asreview_server_auth`: String. What kind of authentication to enable: `basic` or `sram`. See [here](./nginx_location.md#variables). Default: `sram`.
- `asreview_server_http_password`: String. If using `basic` auth, what password to use. Default: `""`.
- `asreview_server_http_username`: String. If using `basic` auth, what username to use. Default: `""`.
- `asreview_server_use_storage`: Boolean. When `true`, ASReview will utilize a storage unit if it is attached to the workspace. If multiple storages are attached, the first one (alphanumerically) will be used. Default: `true`.
- `asreview_server_group`: String. Name of the group for the webserver that should have access to ASReview data. Default: `www-data`.
- `asreview_server_cron_users`: Boolean. If true, periodically (every 15 mins) check for new users from SRAM and add them to ASReview. Default: `true`.
- 
## See also

- Role [flask_app](./flask_app.md)
- Role [nginx_reverse_proxy](./nginx_reverse_proxy.md)
- Playbook [asreview_server](../playbooks/asreview_server.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
