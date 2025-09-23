# Playbook jupyter_rtc
[back to index](../index.md#Playbooks)

## Summary

This playbooks adds [Real-time Collaboration](https://jupyterlab-realtime-collaboration.readthedocs.io/en/latest/) functionality to an existing [JupyterHub](./jupyterhub.md) instance. This allows users to login to a single JupyterLab instance on the Hub and simultaneously edit documents.

Two modes are supported:

- (*Recommended*, *Default*) 'Shared user' mode: a special user `shared` is added to the Hub. All users on the Hub can open `shared`'s JupyterLab server, and edit collaboratively on the server. All users can also *start* `shared`'s server, if it is not running already
    * In this mode, users also have the rights to share their own server with other users at will. However, as of September 2022, JupyterHub does not yet have a UI to handle sharing of servers. The functionality is only available in the API. However, it is already activated by this role for when the UI becaomes available. In this case, this role will allow users to *either* use the `shared` server, or share their own server. 
- (*Warning*) 'All users' mode: all users get access to each other user's JupyterLab instance (although they do no have the rights to start others' servers if they are not already running). This means all users get access to potentially personal information in users' homedirectories. For this reason, *this mode is only recommended on fully trusted instances*. 

When using the playbook in the recommended 'shared user' mode, you might want to configure your Catalog Item such that the 'Access' button points to the URL required to launch the `shared` user's server: `https://==REVERSE_PROXY==/hub/spawn/shared`

## Variables

- `jupyter_rtc_share_all_users`: Boolean. Whether to enable 'all users mode' (see [above](#summary)). Default: `false`.
- `jupyter_rtc_venv`: String. Location of the virtual environment in which the target JupyterHub is installed. Can also be set to the magic value `system` to use the system python installation, instead of a venv. Default: `/usr/local/jupyterhub`.
- `jupyter_rtc_config_path`: String. Location of the main JupyterHub config file. Default: `/usr/local/etc/jupyter/jupyterhub_config.py`.

## See also

- Playbook [jupyterhub](./jupyterhub.md)
- Role [jupyterhub_rtc](../roles/jupyterhub_rtc.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
