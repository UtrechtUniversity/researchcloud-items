# Role jupyterhub_standalone_proxy
[back to index](../index.md#Roles)

## Summary

Use JupyterHub's proxy to spawn and serve an arbitrary webapplication (instead of a Jupyter Notebook), running as any user that logs in to the hub. This allows you to e.g. serve an IDE running as user `foo` when `foo` logs in, and an IDE running as user `bar` when `bar` logs in. Effectively, *this role provides a generic way of serving apps to users running under their own user account.*

This role can also be called multiple times (e.g. by multiple components) to [serve multiple different standalone apps](#hosting-multiple-standalone-apps).

This role uses the [JupyterHub role](./jupyterhub.md), so it supports SRAM authentication.

The role uses the [`jupyter-server-proxy` standalone plugin](https://jupyter-server-proxy.readthedocs.io/en/latest/standalone.html), so that instead of getting the Hub webpage and having to select a web application, users are immediately served the desired webapplication after logging in.

## Requires

- Debian-family OS (tested on Ubuntu >= 22)
- SURF's [SRC-Nginx](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) component preinstalled

## Description

This role levarages JupyterHub's proxy to spawn and serve an arbitrary webapplication (instead of a Jupyter Notebook), running as a specific user. To see how you can determine which application should be spawned, see [the examples](#examples).

The role uses the [JupyterHub role](./jupyterhub.md), so it supports SRAM authentication. It modifies the JupyterHub to replace the default command that is spawned by the Hub: instead of running a notebook server, the [jupyter-standalone-proxy](https://jupyter-server-proxy.readthedocs.io/en/latest/standalone.html) command will be executed (via the `sudospawner` command), with the config file provided.

See the [examples](#examples) below for illustration of how to configure this role.

## Variables

- `jhsp_enable_notebook`: Boolean. Whether standard settings for Jupyter Notebook should be enabled on the hood. Default: `false`. May be useful to set to `true` if you want to also serve notebook servers using the hub created by this role.
- `jhsp_extra_pkgs`: List. Extra pypi packages that will be installed in jupyterhub's `venv` in addition the required base packages. Default: `[]`.
- `jhsp_standalone_proxy_config_dir`: String. Path to the directory containing standalone proxy config files. Default: `"/usr/local/etc/jupyter/standalone"`.
- `jhsp_standalone_proxy_config`:  String. Contents of a [traitlets config file](#configuration-option-2) to beplaced in `jhsp_standalone_proxy_config_dir`.  Default: `""`.
- `jhsp_app_name`: String. Name of the application, used to generate a filename for the traitles config file. Default: `standalone_app`.
- `jhsp_standalone_proxy_cmd`: String. The command that will be spawned when a user logs in. Default: `jupyter-standaloneproxy`.
- `jhsp_standalone_proxy_cmd_args`: List of command line args provided to `jhsp_standalone_proxy_cmd`. Default: `""`. When this is set to the default empty string, JupyterHub will instead look for configuration files as per [this scenario](#configuration-option-2).
- `jhsp_config_env_keep`: List of environment variables, the values of which will be passed along to each spawned webapplication. Overrides `env_keep` set by the [JupyterhHub role](./jupyterhub.md). Default: `['JUPYTERHUB_ACTIVITY_URL', 'JUPYTERHUB_SERVER_NAME', 'JUPYTERHUB_API_URL', 'JUPYTERHUB_API_TOKEN', 'JUPYTERHUB_SERVICE_URL', 'JUPYTERHUB_SINGLEUSER_APP', 'JUPYTERHUB_USER', 'JUPYTERHUB_GROUP', 'PYTHONPATH', 'PATH']`.
- `jhsp_jupyterhub_user`: String. The user the hub itself should run as. Default: `jupyter`.
- `jhsp_jupyterhub_allowed_users_group`: String. Name of the group, users in which will be able to use the hub.
- `jhsp_external_addr`: String. FQDN at which the service will be reached. Used to e.g. allowlist this FQDN for [CORS](#a-note-on-handling-cors) when a proxied stanadlone app uses websockets.
- `jhsp_allow_named_servers`: Boolean. Whether to allow a user to have multiple servers running in the hub simultaneously. See the [JupyterHub documentation for named servers](https://jupyterhub.readthedocs.io/en/stable/howto/configuration/config-user-env.html#named-servers). Default: `true`.
- `jhsp_config_extra`: String. Optional extra configuration that will be injected into the main JupyterHub configuration file. Default: `""`.

## Examples

There are two ways in which `jupyterhub-standaloneproxy` can be configured with this role:

- [Option 1](#configuration-option-1): set the command to be run by `jupyter-standaloneproxy` directly.
- [Option 2](#configuration-option-2): place a config file in the standalone config directory.
  * This option is recommended if you want to [host multiple standalone proxy apps on a single server](#hosting-multiple-standalone-apps).

### Configuration option 1

*Set the command to be run by `jupyter-standaloneproxy` directly.*

By setting the `jhsp_standalone_proxy_cmd_args` [variable](#variables), you can directly determine which arguments will be passed along to the `jupyter-standaloneproxy` command. 

These arguments will be specified in the `sudospawner-singleuser` script that the role places in the JupyterHub venv.

The following configuration, for example, would launch a simple HTTP fileserver as a standalone app:

```yaml
roles:
  - role: jupyterhub_standalone_proxy
    vars:
      jhsp_standalone_proxy_cmd_args:
        # - "--no-authentication" # optional arguments for jupyterhub-standaloneproxy here. See [here](https://jupyter-server-proxy.readthedocs.io/en/latest/standalone.html) for available options.
        - "--" # marks the end of options for jupyterhub-standaloneproxy, after this point we specify the command that should be launched as a standalone proxy.
        - "/usr/bin/python3"
        - "-m"
        - "http.server"
        - "{port}"
        # The above command will spawn the default python HTTP fileserver, running in the user's homedirectory.
```

With this method, you can serve only one app as a standalone proxy (i.e., the provided command).

### Configuration option 2

*Place a config file in the standalone config directory.*

Alternatively, you can configure `jupyter-standaloneproxy` through a Python configuration file with [traitlets](https://traitlets.readthedocs.io/en/stable/). Any files placed in the directory specified by the `jhsp_standalone_proxy_config_dir` [variable](#variables) **that end in the extension `.conf.py`** will be automatically detected by the JupyterHub configuration.

See [here](https://jupyter-server-proxy.readthedocs.io/en/latest/standalone.html#configuration-via-traitlets) for available configuration options.

This gives you two possibilities:

- Place only a single configuration file in `jhsp_standalone_proxy_config_dir`.
- Place multiple configuration files in that location. In this case, you will configure the Hub to use [multiple standalone apps](#hosting-multiple-standalone-apps).

You can place config files:

- Manually in your playbook.
- Use the `jhsp_standalone_proxy_config` variable to have this role create a config file for you.
- Use the [`jupyterhub_app` role](./jupyterhub_app.md) to place a standalone config.

Here is an example of a valid config file:

```python
# example.conf.py in /usr/local/etc/jupyter/standalone
c.StandaloneProxyServer.command = [
    "/usr/bin/python3", "-m", "http.server", "{port}"
]
```

Here is an example of how to install this configuration file by calling this role:

```yaml
roles:
  - role: jupyterhub_standalone_proxy
    vars:
      jhsp_standalone_proxy_config: |
        c.StandaloneProxyServer.command = [
          "/usr/bin/python3", "-m", "http.server", "{port}"
        ]
```

### Hosting multiple standalone apps

If you place [multiple traitlet config files in the appropriate directory](#configuration-option-2), the Hub is configured to allow the user to spawn any of the apps configured in this file. That is, given that both `example1.conf.py` and `example2.conf.py` are in the appropriate directory, when logging in to the Hub, the user will be presented with a choice to *either* spawn the app configured in `example1` or in `example2`.

This means multiple components can call this role and install their own configuration files, whereup the Hub will serve *both* apps.

The user can also spawn *both* servers, which will be served under different URLs, if `jhsp_named_servers` is enabled. By default, the user can access all the apps spawned by them (and spawn new ones) under the JupyterHub 'home' view (`http://myinstance.com/hub/home`).

In addition to letting the user choose which app to spawn (done by this role), you could provide your own logic (e.g. in a custom webpage) to conditionally serve different apps (e.g. depending on the URL path). At this point, this is not done by this role.

### A note on handling CORS

In a standard JupyterHub, the Hub will start JupyterLab, and JupyterLab will start various users' servers. `jupyter-standaloneproxy` removes the need for JupyterLab, but this can lead to some complications. One such complication is that JuptyerLab will normally ensure that [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) is properly configured for the servers it starts. This means that applications will know that requests from the users' browser, which accesses the server at the workspace's FQDN, should be allowed---even though the application runs on a different domain (namely, `localhost`).

In the case of standalone apps, we need to do some work to properly configure CORS ourselves---although this will not be a problem with all applications. Specifically, it will only be required for proxied apps that use [websockets](https://en.wikipedia.org/wiki/WebSocket) in the frontend. Just test out your app to see if you run into any frontend issues due to CORS. If so, you can use the following function from [`utils.py`](#utilspy) in your traitlet config file:

```python
from utils import * # import from utils.py, placed in the same directory as the config files (/usr/local/etc/jupyter/standalone by default)

custom_check_origin_patch() # apply monkeypatch for custom CORS allowlist for websockets from utils.py

# rest of your traitlets config here, e.g.:
#c.StandaloneProxyServer.command =  [
  # Your command here
#]
```

See the `custom_check_origin_patch()` function in `utils.py` for technical details.

## How it works

- JupyterHub is configured to use [sudospawner](#sudospawner).
- `sudospawner` will launch the script `sudospawner-singleuser` as a specific user.
- The role places a custom `sudospawner-singleuser` script in the JupyterHub venv.
  * Depending on the variables passed to the role, this script will call the `jupyterhub-standaloneproxy` command with various options.

### `sudospawner`

JupyterHub's [sudospawner](https://github.com/jupyterhub/sudospawner) is used to run the desired webapp as a specific user: when you login with user `foo` (usin e.g. SRAM), the hub (which runs as a dedicated service user itself) will use special `sudo` permissions to spawn the webapp running as user `foo` on the workspace. Since `sudospawner` by default launches the `jupyter-singleuser` command (used to start JupyterLab), we need to overwrite this command by placing a custom `sudospawner-singleuser` script in the Jupyter venv, as explained [here](https://github.com/jupyterhub/sudospawner?tab=readme-ov-file#custom-singleuser-launch-command). The custom script launches the `jupyter-standaloneproxy` instead of `jupyter-singleuser`.

Only users in the group specified by `jupyterhub_allowed_users_group` variable are allowed to use `sudospawner` in this way.

### utils.py

This role will create `utils.py` in the directory configured by `jhsp_standalone_proxy_config_dir`. `utils.py` contains helpful Python functions that can be called from the traitlet config files (see [above](#configuration-option-2)). This is to provide common functionality that is likely needed when configuring standalone apps, e.g.:

- a function to [handle CORS for webockets](#a-note-on-handling-cors).

`utils.py` also contains the `get_standalone_proxy_config` function, which is used in the JupyterHub configuration to detect the presence of one or multiple config files (see [above](#configuration-option-2)).

Since `utils.py` is by default placed in the same directory (=python package) as your traitlet config files, you can directly import it from your config file.

## See also

- Role [jupyterhub](./jupyterhub.md)
- Role [jupyterhub_app](./jupyterhub_app.md)
- Role [nginx_reverse_proxy](./nginx_reverse_proxy.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
