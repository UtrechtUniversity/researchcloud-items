# Playbook asreview_server
[back to index](../index.md#Playbooks)

## Summary
[ASReview](https://asreview.nl/) is an application that uses active learning to facilitate and predict the relevancy of papers during a systematic review.

This component installs the ASReview webapplication. Users in the collaboration will be able to login using SRAM Single Sign-on.

## Requires

- Ubuntu OS
- SURF's [SRC-Nginx](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) component preinstalled

## Variables

- `asreview_use_storage`: Boolean. When `true`, ASReview will utilize a storage unit if it is attached to the workspace. If multiple storages are attached, the first one (alphanumerically) will be used. Default: `true`.
- `asreview_extra_pkgs`: String. Comma-separated extra packages (in addition to `asreview`) that should be installed into ASReview's `venv`. Can be used to install ASReview extras such as the `asreview-dory` package.

## See also

- [asreview_server role](../roles/asreview_server.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
