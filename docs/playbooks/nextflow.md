# Plabyook nextflow
[back to index](../index.md#Roles)

## Summary

Installs the [Nextflow](https://www.nextflow.io/) workflow engine.

Nextflow is a scientific workflow system predominantly used for bioinformatic data analysis. It establishes standards for programmatically creating a series of dependent computational steps and facilitates their execution on various local and cloud resources.

## Requires

* Debian-based system
* RHEL-based system

## Description

The role will install the latest version of Nextflow by default. Nextflow is downloaded from Github, and placed in `/usr/local/bin/nextflow`. Nextflow will therefore be available on every user's path.

## Variables

- `nextflow_version`: String. If set, a specific version of Nextflow will be downloaded from Github (instead of the latest version). Default: `""`.
- `nextflow_java_version`: String. The version of Java that will be installed. Default: `"17"`.

## See also

- role [nextflow](../roles/nextflow.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
