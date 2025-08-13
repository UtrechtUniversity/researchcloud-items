# Role jupyterhub_app
[back to index](../index.md#Roles)

## Summary

This role allows you to installs any arbritrary webapplication on an existing [JupyterHub](./jupyterhub.md) instance. The application can be either:

- Added to a standard JupyterHub, where the application will appear in JupyterLab and can be launched by the user from there.
- Added as a [standalone application](./jupyterhub_standalone_proxy.md), where JupyterHub directly launches the app (instead of going through JupyterLab).

In both cases, your application will be [spawned by JupyterHub](./jupyterhub.md#authentication-and-authorization), running as the user logged in to the Hub. This means every user can get their own instance of the app.

This role can be involed multiple time (also in multiple playbooks) to add multiple apps to the Hub.

*This role expects JupyterHub to be already installed. You need to tell the role where to find JupyterHub using the `jupyterhub_app_venv` [variable](#variables).*

## Description

This role:

1. Installs the `jupyter-server-proxy` extension for JupyterHub.
1. *Either* places a configuration file for a JupyterLab server extension wrapping your desired application, *or* it installs such an extension via `pip`.
  - If the `jupyterhub_app_pip` variable (see [below](#variables)) is set, the config file will be ommitted.
1. Places a configuration file for a '[standalone](./jupyterhub_standalone_proxy.md)' version of your desired application. The role will place this config file regardless of whether the Hub is running in standalone mode -- if it is not, it will simply be ignored.

Unless you are using `jupyterhub_app_pip`, you need to set the `jupyterhub_app_command` variable. Based on this variable, this role will generate a default configuration for both a JupyterLab server extension for your app, and a standalone version of your app.

*In most cases, `jupyterhub_app_pip` is the only variable you absolutely need to set: the role will take care of the rest. See an [example](#example-1) here.*

However, you can also further customize the configuration that wraps your app. See:

- [Configuring your app as a JupyterLab server extension](#configuring-your-app-as-a-jupyterlab-server-extension).
- [Configuring your app as a standalone server](#configuring-your-app-as-a-standalone-server).

### Configuring your app as a JupyterLab server extension

By default, this role will generate a default [traitlets](https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html#specifying-config-via-traitlets) configuration file for a [`jupyter-server-proxy`](https://jupyter-server-proxy.readthedocs.io/) app, based on a number of variables (see [below](#variables)):

- `jupyterhub_app_command` (required) *For a minimal configuration, this variable is all you need to configure -- the role will take care of the rest.*
- `jupyterhub_app_name` (optional, but recommended)
- `jupyterhub_app_icon_path` (optional)
- `jupyterhub_app_category` (optional)

However, if you want to override the default configuration, you have two choices:

- Override the `jupyterhub_app_server` variable. This is a dict that corresponds to the one illustrated [here](https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html#server-process-options).
- Override the `jupyterhub_app_server_config` variable. This is a string of python code that you can use to completely control the traitlets config (see [here](https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html#specifying-config-via-traitlets) for an example).

The generated config file will be placed in `jupyter_server_config.py` in `jupyterhub_app_config_dir`, where it will be auto-loaded by JupyterLab.

### Configuring your app as a standalone server

By default, this role will generate a default [traitlets](https://jupyter-server-proxy.readthedocs.io/en/latest/standalone.html#configuration-via-traitlets) configuration file for a [`jupyter-standaloneproxy`]((https://jupyter-server-proxy.readthedocs.io/en/latest/standalone.html/) app, based on the `jupyterhub_app_command` variable. *For a minimal configuration, that variable is all you need to configure -- the role will take care of the rest.*

However, you can override this default using the `jupyterhub_app_standalone_config` variable. See [here](./jupyterhub_standalone_proxy.md#configuration-option-2) for what a standalone config should look like.

This generated config will be placed into the directory `standalone` inside the directory specified by the `jupyterhub_app_config_dir` variable.

## Variables

### Variables the JupyterHub installation

- `jupyterhub_app_venv`: String. Path to the JupyterHub instance's `venv`. Default: `/usr/local/jupyterhub`. You can set this to the value `system` to not use a virtual environment.
- `jupyterhub_app_config_dir`: String. Path to the JupyterHub's instance config dir. Default: `/usr/local/etc/jupyter`.
- `jupyterhub_app_pip_executable`: String. Which command to use to install packages into the venv (can be set to `uv` when it is available). Default: `pip`.
- `jupyterhub_app_pip`: String. Optional. Which package to install into the hub's venv (if set). Default: `""`. If this is set, no traitles config file will be placed.

### Variables concerning the application

- `jupyterhub_app_name`: String. Name of the application, used to generate a filename for the standalone config file (if specified). Default: `app`.
- `jupyterhub_app_command`: List. Optional, but required when not setting `jupyterhub_app_pip`. Specifies the command that will launch your application. Each item in the list after the first one will be an argument to your command. Default: `""`. See [example](#example-1).
- `jupyterhub_app_icon_path`: String. Optional. Path to a `.svg` icon file that will be used in JupyterLab to represnt your application (when not in standalone mode).
- `jupyterhub_app_category`: String. Optional. JuypyterLab category this app wil be displayed under (when not in standalone mode). Default: `""` (this means the app will be placed in the `Notebook` category).
- `jupyterhub_app_server`: Dict. Settings for `juypyter-server-proxy`, as specified [here](https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html#server-process-options). See [example](#example-2-override-jupyterhub_app_server). By default, this dictionary will be generated by the role based on the variables `jupyterhub_app_command`, `jupyterhub_app_icon_path`, `jupyterhub_app_category` and `jupyterhub_app_name`.
- `jupyterhub_app_standalone_config`: String. Optional. Trailets configuration for a standalone app. See [example](#example-3-override-jupyterhub_app_server_config-and-jupyterhub_app_standalone_config). Default: `""`.
- `jupyterhub_app_server_config`: String. Optional. Trailets configuration for a non-standalone proxy server app. See [example](#example-2-override-jupyterhub_app_server). Will be added to `jupyter_server_config.py`, automatically loaded `jupyter-serverproxy` extension. **Note**: to allow multiple invocations of this role to add traitlets configuration in this way, see the [example](#jupyterhub_app_server_config).

## Examples

The three examples in this section effectively accomplish the same thing, wrapping a simple Python http server as a JupyterHub app.

For more complicated applications, you may need to do some additional work in the config files. See e.g. the [openvscodeserver playbook](../../playbooks/openvscodeserver.yml).

### Example 1

```yaml
- role: jupyterhub_app
  vars:
    jupyterhub_app_name: Example
    jupyterhub_app_venv: /path/to/jupyterhub/venv # Optional. Can also be set to 'system'
    jupyterhub_app_config_dir: /usr/local/etc/jupyter # Optional. Can be any path in which JupyterHub looks for config files.
    jupyterhub_app_pip_executable: pip #  Optional. Can also set to uv if it's available, for better performance.
    jupyterhub_app_icon_path: /path/to/my/icon.svg # Optional
    jupyterhub_app_category: 'Other' # Optional. Category under which the app will be displayed in JupyterLab
    jupyterhub_app_command:
      - /usr/bin/python3
      - -m
      - http.server
      - -p
      - "{port}" # magic variable that will be replaced by `jupyter-server-proxy` with the port on which the Hub will spawn the instance. See: https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html#server-process-options
```

The resulting config for a JupyterLab server extension will look as follows:

```python
settings = { "Example":
{'command': ['/usr/bin/python3', '-m' 'http.server', '-p', '{port}'], 'launcher_entry': {'icon_path': '/path/to/my/icon.svg', 'category': 'Other'}
}
c.ServerProxy.servers.update({
}) # use update instead of assignment so multiple apps can be added to the config.
```

The resulting config for a standalone app will look as follows:

```python
c.StandaloneProxyServer.command = ['/usr/bin/python3', '-m' 'http.server', '-p', '{port}']
```

### Example 2: override `jupyterhub_app_server`

```yaml
- role: jupyterhub_app
  vars:
    jupyterhub_app_server:
      command: ['/usr/bin/python3', '-m' 'http.server', '-p', '{port}']
      launcher_entry:
        title: MyExample
        icon_path: /path/to/icon.svg
        category: Notebook
```

### Example 3: override `jupyterhub_app_server_config` and `jupyterhub_app_standalone_config`

```yaml
- role: jupyterhub_app
  vars:
    jupyterhub_app_server_config: |
      # 'c' is a traitles object that is automatically available in the config file
      c.ServerProxy.servers.update({'command': ['/usr/bin/python3', '-m' 'http.server', '-p', '{port}']})
      # ... some more Python code here, do whatever you like
    jupyterhub_app_standalone_config: |
      # 'c' is a traitlets object that is automatically available in the config file
        c.StandaloneProxyServer.command = ['/usr/bin/python3', '-m' 'http.server', '-p', '{unix_socket}']
        c.StandaloneProxyServer.unix_socket = True
      # ... some more Python code here, do whatever you like
      # you can also use the provided convenience functions from `utils.py` here, see the docs for the jupyterhub_standalone_proxy role.
```

## See also

- Role [jupyterhub](./jupyterhub.md)
- Role [jupyterhub_standalone_proxy](./jupyterhub_standalone_proxy.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
