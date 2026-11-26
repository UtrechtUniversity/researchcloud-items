# Role vllm
[back to index](../index.md#Roles)

## Summary

This role installs [vLLM](https://docs.vllm.ai/) in a dedicated Python virtual environment and runs its OpenAI-compatible server as a systemd service.

## Requires

* Debian-based system with Python 3
* A model supported by vLLM

## Variables

* `vllm_model`: model identifier to serve; required when enabled
* `vllm_host`: listen address, default `127.0.0.1`
* `vllm_port`: listen port, default `8000`
* `vllm_extra_args`: additional arguments passed to `vllm serve`
* `vllm_enabled`: install and run the service, default `true`

The role is independent of Goose and JupyterHub and can be included directly in another playbook.

## History
2026 Written by Jelle Treep (Utrecht University)

[back to index](../index.md#Roles)
