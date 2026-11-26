# Role <name>
[back to index](../index.md#Roles)

## Summary

This role installs [goose](https://goose-docs.ai/), an open source AI agent, and configures it to use either SURF's AI hub or a local vLLM endpoint.

## Requires

* Debian-based system
* SRC Component: [SRC-Nginx Component](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) must be executed prior to this component.
* A JupyterHub installation is optional. When present, the role forwards the Willma API key to spawned servers.

## Description

The role:

- Creates config files for all users based on templates
- Installs goose
- Installs goose desktop for desktop workspaces
- Uses a component secret in Research Cloud to establish the optional AI hub connection
- Falls back to a vLLM provider when the AI hub is disabled or its default API key is used

## Variables

- `WILLMA_API_KEY`: AI hub API key; the default `mock-key` disables the AI hub
- `goose_use_willma`: explicitly enable or disable the AI hub provider
- `goose_vllm_model`: model name used by the vLLM provider
- `goose_vllm_base_url`: OpenAI-compatible vLLM endpoint

## See also

- role [jupyterhub](../roles/jupyterhub.md)

## History
2026 Written by Jelle Treep (Utrecht University)

[back to index](../index.md#Roles)
