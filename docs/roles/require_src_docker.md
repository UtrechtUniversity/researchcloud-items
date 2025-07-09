# Role require_src_nginx
[back to index](../index.md#Roles)

## Summary

A simple role that applies some heuristics to determine if one of the following components (all hosted in [this repository]()) has been run before the current one:

* SRC External Docker
* SRC External Docker Compose
* Docker Environment

You can check either for a rootful (default) installation of Docker, or a rootless. Heuristics applied are as follows:

* rootful: is the service `docker.service` running? (*note* this will also be true if docker was installed in some other way)
* rootless: is the script `/etc/rsc/cron_rootless_docker.sh` present? (*note* if rootless Docker was installed via some other route than the SURF components, this heuristic will fail)

If these checks fail, the role will fail.


## Variables

- `docker_rootless`: Boolean. Check for presence of rootless Docker? Default: `false`.

## Usage

Include the role like usual:

```yaml
roles:
  - role: require_src_docker
    vars:
      docker_rootless: true # optional
```

...or add it to another role's `meta/main.yml`, in the `dependencies` section:

```yaml
---
dependencies:
  - require_src_docker # will check for rootful installation, since no variables are set
```

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
