# Role ray
[back to index](../index.md#Roles)

## Summary

Installs [Ray](https://www.ray.io/) on a server as either a Ray cluster head or worker. The role creates a dedicated `ray` account by default and can run Ray as a system service. Set `ray_user` to use a different account; the role uses `/home/<ray_user>` as that account's home directory.

## Requires

- Ubuntu 22.04 (Jammy) or 24.04 (Noble)
- `uv` available on the target system

## Description

Ray is a framework for running Python applications across multiple processes or machines. Use this role to prepare a machine to join a Ray cluster:

- A **head node** starts a cluster and provides its coordination and dashboard services.
- A **worker node** connects to an existing head node and contributes resources.

There are three ways to use this role:

- *With `ray up`*: using the [SRC Ray Autoscale Provider](https://github.com/UtrechtUniversity/src-ray-provider), and end user can create a cluster with `ray up`.
- *Manually*: the end user can start a ResearchCloud workspace for a head node and worker nodes manually.
- *With autoscaler*: the end user can manually start a ResearchCloud workspace with a head node that includes an autoscaler config. Worker nodes will then be automatically created by the head node. This mimics the behavior of `ray up`. See [Variables](#variables) for variables that allow configuring the cluster.

The role installs Ray and the SURF ResearchCloud Ray provider in a Python virtual environment owned by the `ray` user. By default, it also creates and starts a systemd service for the selected node type. Configure a head node and its workers with matching connection details so that the workers can reach the head.

For clusters using the SURF ResearchCloud autoscaler, enable `ray_autoscale` on the head and provide an autoscaling configuration. Configure any required SSH key and ResearchCloud token as described below.

### Example usage

Set e.g. these variables on the head and worker roles in your playbook:

```yaml
# Head node
ray_head_node: true
ray_auth_token: "{{ vault_ray_auth_token }}"
```

```yaml
# Worker node
ray_head_node: false
ray_head_node_address: "ray-head.internal"
ray_auth_token: "{{ vault_ray_auth_token }}"
```

Store the token securely (for example, as a ResearchCloud secret) and use the same value on the head and its workers.

## Variables

| Variable | Default | Description |
|---|---|---|
| `ray_user` | `"ray"` | Name of the dedicated account used to run Ray. The role uses `/home/<ray_user>` as its home directory. |
| `ray_head_node` | `true` | Whether this machine runs the cluster head (`true`) or a worker (`false`). |
| `ray_head_node_address` | `""` | Address of the head node. On a worker, set this to a hostname or IP address; the role appends `ray_head_node_port` if no port is included. When empty, the head uses its private IP and a worker uses Ray's automatic address discovery. |
| `ray_head_node_port` | `"6379"` | Port used by the head node for cluster connections. |
| `ray_dashboard_host` | `"127.0.0.1"` | Address on which the head node's dashboard listens. Use care before binding it to a network-accessible address. |
| `ray_dashboard_port` | `"8265"` | Dashboard port on the head node. |
| `ray_client_server_port` | `"10001"` | Ray Client server port on the head node. |
| `ray_head_no_cpu` | `false` | On a head node, set this to `true` to report zero CPUs as available for Ray tasks. |
| `ray_auth_token` | `""` | Optional token used to protect Ray connections. When set, the role stores it in a file accessible only to the `ray` user and configures Ray to use token authentication. Use the same token when connecting clients and workers. |
| `ray_autoscale` | `false` | Start the head node with Ray's autoscaling configuration. |
| `ray_autoscale_config` | Not set | Template path for the autoscaling configuration. Required when `ray_autoscale` is `true`. |
| `ray_public_key` | `""` | Optional SSH public key added to the `ray` user's authorized keys and written to the location expected by the ResearchCloud provider. |
| `ray_src_token` | `""` | Optional SURF ResearchCloud token. When set, it is exported as `RESEARCH_CLOUD_TOKEN` in the `ray` user's shell configuration for the autoscaler. |
| `ray_python_version` | `""` | Python version for the virtual environment. Empty uses the system Python available to `uv`. |
| `ray_version` | `""` | Optional pip version specifier appended to the Ray package name, for example `==2.40.0`. |
| `ray_user_packages` | `""` | Optional comma-separated Ray package extras. Empty installs the `default` and `client` extras. |
| `ray_env` | `""` | Optional comma-separated environment variables in `NAME=VALUE` form, added to the Ray environment. |
| `ray_setup` | `true` | Create and start the systemd service. Set to `false` to install and configure Ray without creating that service -- this is the behavior required when creating a Ray cluster with `ray up`. |
| `ray_fail_hard` | `false` | When `true`, fail the role if the Ray status check after a service restart does not report the cluster as active. |
| `ray_service_prefix` | `""` | Optional prefix for the systemd service name, allowing multiple Ray services on one machine. |
| `ray_log_to_stderr` | `false` | Add the explicit `RAY_LOG_TO_STDERR=1` setting to the systemd service environment. |
| `ray_src_max_workers` | `6` | Maximum number of total nodes for the Ray SURF ResearchCloud autoscaler cluster definition. |
| `ray_src_co_name` | `""` | CO name for the Ray SURF ResearchCloud autoscaler cluster definition. |
| `ray_src_wallet_name` | `""` | Wallet name for the Ray SURF ResearchCloud autoscaler cluster definition. |
| `ray_src_cloud_name` | `"SURF HPC Cloud"` | Cloud name for the Ray SURF ResearchCloud autoscaler cluster definition. |
| `ray_src_cluster_name` | `"ray<random_string>-cluster"` or `<ray_service_prefix>-cluster` if service name is set | Cluster name for the Ray SURF ResearchCloud autoscaler cluster definition. |


## Technical details

The role creates the virtual environment under `/opt/` and runs the service as the user configured by `ray_user`. The default service names are `ray_head` and `ray_worker`; `ray_service_prefix` is added to the name when set. The service logs to `/var/log/<service-name>.log`.

The head uses ports 6379, 8265, and 10001 by default for cluster connections, the dashboard, and Ray Client, respectively. Ensure the required ports are reachable between cluster nodes and client machines. The dashboard binds to loopback by default; changing `ray_dashboard_host` may expose it to other machines, so restrict network access accordingly.

The role also grants the configured user passwordless permission to start, restart, and stop its systemd service.

### Autoscaling

When autoscaling is enabled, the role copies a default autoscaling configuration using the SRC Ray provider to `/home/<ray_user>/ray_bootstrap_config.yaml` and starts the head with that configuration. By default, this configuration will use the ResearchCloud API to lookup information about the current workspace. It will configure the cluster to use the same CO, Cloud type (e.g. SURF HPC Cloud), and Wallet as the current workspace. These values can be overriden with the variables mentioned above.

**`ray_src_token` must be set when using autoscaling.**

## See also

- [Ray documentation](https://docs.ray.io/)
- [SURF ResearchCloud Ray provider](https://github.com/UtrechtUniversity/src-ray-provider)

## History
2026 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
