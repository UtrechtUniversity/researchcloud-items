# Playbook goose
[back to index](../index.md#Playbooks)

## Summary
This playbook installs [goose](https://goose-docs.ai/), an open source AI agent, on jupyterhub workspaces. It contains configuration files to connect with SURFs AI hub as custom provider. Furthermore, the playbook installs [Jupyter AI](https://jupyter-ai.readthedocs.io/en/stable/), a chat interface within jupyter that can use goose as a provider.

## Requires

* Debian-based system
* SRC Component: [SRC-Nginx Component](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) must be executed prior to this component.
* A JupyterHub installation.

## Description

The playbook:

- Creates config files for all users based on templates
- Installs goose
- Installs goose desktop for desktop workspaces
- Installs jupyter-ai
- Uses a component secret in Research Cloud to establish API connection

## Variables

- API key, to be set by admins

## See also

- role [jupyterhub](../roles/jupyterhub.md)

## History
2026 Written by Jelle Treep (Utrecht University)

[back to index](../index.md#Playbooks)
