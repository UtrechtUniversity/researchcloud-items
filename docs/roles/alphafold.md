# Role AlphaFold
[back to index](../index.md#Roles)

## Summary
Installs the Alphabet DeepMind AlphaFold inference pipeline for protein folding.

Note: the user has to acquire model parameters themselves, and place them on the workspace. See the [user manual](https://utrechtuniversity.github.io/vre-docs/docs/workspaces/utility/alphafold.html)

## Requirements

- Ubuntu workspace
- SURF [Docker Environment component](https://gitlab.com/rsc-surf-nl/plugins/plugin-external-docker) installed

## Description

- Gets the alphafold3 source
- Builds the docker image from that source
- Ensure the right directories for input, output, public databases, and model parameters exist.
- Places a convenience script `run_alphafold` to assist the user

## See also
[alphafold playbook](../playbooks/alphafold.md)

## History
2024-2025 Written by Almed Hamzah and Dawa Ometto (Utrecht University).

[back to index](../index.md#Roles)
