# Playbook ray
[back to index](../index.md#Playbooks)

## Summary

Prepares a SURF ResearchCloud workspace to run [Ray](https://www.ray.io/), a framework for building and running Python applications across multiple CPU cores and machines. Use it to set up a distributed compute cluster, from a single head node to a cluster with workers that can be added manually or through autoscaling.

## Properties

Status: Supported

Suitability: Sensitive data

## Requires

- SURF ResearchCloud workspace running Ubuntu 22.04 (Jammy) or 24.04 (Noble)
- `uv` available on the workspace

## Description

Ray lets Python programs split work into tasks and actors and run that work in parallel. A Ray cluster has a **head node**, which coordinates the cluster and provides its dashboard, and one or more **worker nodes**, which contribute compute resources. Applications and users can submit work to the cluster through Ray's Python API, command-line tools, or dashboard.

This playbook installs Ray and the SURF ResearchCloud Ray provider on a workspace. It supports three ways to create and use a cluster:

### 1. Create a cluster with `ray up`

The end user uses `ray up` the [SURF ResearchCloud Ray provider](https://github.com/UtrechtUniversity/src-ray-provider) to have Ray create and manage the cluster from a cluster configuration. The autoscaler will set `do_setup: false` so the playbook installs Ray and the provider without starting its systemd service.

This is useful when you want Ray to manage cluster creation instead of provisioning each node yourself. The provider needs the appropriate ResearchCloud credentials and SSH key; protect these values as secrets.

**This kind of deployment requires setting the `src_token` parameter to a ResearchCloud personal API token. Store this token in a secure manner (in a ResearchCloud secret), and _give the token minimal (CO-specific, wallet-specific) scope_**. Cluster users can potentially access this token, so always ensure that anyone with access to the cluster is trusted with the permissions the token provides.

### 2. Provision the head and workers manually

Manually create workspaces that execute this component for a head workspace, and for each worker workspace. This requires setting `head_node: true` on the head and `head_node: false` on workers. Configure each worker with the head's address using `head_node_address`. Once the nodes can communicate over the required network ports, Ray workers join the head and make their resources available to jobs.

This mode gives you direct control over how many workspaces are created and when. It does not have the head automatically create additional workspaces.

### 3. Let the head autoscale workers

Create a head workspace with Ray autoscaling enabled and an autoscaling configuration (default SRC autoscaler config is provided). The head can then request worker nodes as the cluster needs additional resources. This mode resembles `ray up`, but you start the head workspace yourself and provide the autoscaling configuration to it.

Set `autoscale: true` and optionally override `autoscale_config`. Setting `src_token` is required. The configuration describes the worker resources and scaling limits. Configure any required ResearchCloud token and SSH public key as well. See the [Ray role documentation](../roles/ray.md#autoscaling) for role-level autoscaling and details.

## Variables

These are the main playbook inputs. For role-level settings and defaults, see the [Ray role documentation](../roles/ray.md).

| Variable | Default | Description |
|---|---|---|
| `head_node` | `false` | Set to `true` for the head workspace; leave `false` for a worker. |
| `head_node_address` | `""` | Address of the head, used by manually provisioned workers. |
| `head_node_port` | `"6379"` | Head node's cluster connection port. |
| `auth_token` | `""` | Optional token to protect cluster connections. Use the same token for the head and its workers. Treat it as a secret. |
| `src_token` | `""` | Optional ResearchCloud token used by the provider for autoscaling. Treat it as a secret. |
| `public_key` | `""` | Optional SSH public key used by the provider to access cluster nodes. |
| `do_setup` | `true` | Whether to create and start the Ray systemd service. Set to `false` for the `ray up` mode. |
| `autoscale` | `false` | Start the head with autoscaling enabled. Set `autoscale_config` as well. |
| `autoscale_config` | Not set | Path to the autoscaling configuration template; required when autoscaling is enabled. |
| `head_no_cpu` | `true` | Whether to reserve the head's CPUs from Ray tasks. |
| `dashboard_port` | `"8265"` | Ray dashboard port on the head. |
| `client_server_port` | `"10001"` | Ray Client server port on the head. |
| `packages` | `""` | Optional comma-separated Ray package extras. Empty uses the default and client extras. |
| `python_version` | `""` | Optional Python version for the Ray virtual environment. |
| `version` | `""` | Optional Ray version to install. |
| `env` | `""` | Optional comma-separated environment variables in `NAME=VALUE` form. |
| `fail_hard` | `false` | Fail the play if the Ray service is not active after restart. |
| `src_max_workers` | `6` | Maximum number of total nodes for the Ray SURF ResearchCloud autoscaler cluster definition. |
| `src_co_name` | `""` | CO name for the Ray SURF ResearchCloud autoscaler cluster definition. |
| `src_wallet_name` | `""` | Wallet name for the Ray SURF ResearchCloud autoscaler cluster definition. |
| `src_cloud_name` | `"SURF HPC Cloud"` | Cloud name for the Ray SURF ResearchCloud autoscaler cluster definition. |

Store tokens in ResearchCloud secrets or another suitable secret store rather than putting their values directly in a playbook or source control. The role creates a dedicated `ray` account and protects its stored authentication token.

## See also

- [Role ray](../roles/ray.md) for details about the installed service, ports, and role variables
- [Ray documentation](https://docs.ray.io/)
- [SURF ResearchCloud Ray provider](https://github.com/UtrechtUniversity/src-ray-provider)

## History
2026 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
