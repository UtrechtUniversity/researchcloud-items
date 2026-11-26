# Playbook goose
[back to index](../index.md#Playbooks)

## Summary
This playbook installs [goose](https://goose-docs.ai/), an open source AI agent, with Jupyter AI. It uses SURF's AI hub when configured and otherwise installs a local vLLM server.

## Requires

* Debian-based system
* SRC Component: [SRC-Nginx Component](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) must be executed prior to this component.
* A JupyterHub installation, installed by the preceding JupyterHub playbook

## Description

The playbook:

- Creates config files for all users based on templates
- Installs goose
- Installs goose desktop for desktop workspaces
- Installs jupyter-ai
- Uses a component secret in Research Cloud to establish the optional AI hub connection
- Installs vLLM when the AI hub is unavailable or disabled

## Variables

- `WILLMA_API_KEY`: AI hub API key
- `goose_use_willma`: explicitly enable or disable the AI hub provider
- `goose_vllm_model`: model served by vLLM when the AI hub is disabled

## See also

- role [jupyterhub](../roles/jupyterhub.md)

## History
2026 Written by Jelle Treep (Utrecht University)

[back to index](../index.md#Playbooks)
