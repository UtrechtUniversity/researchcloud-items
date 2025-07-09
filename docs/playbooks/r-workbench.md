# Playbook r-workbench
[back to index](../index.md#Playbooks)

## Summary

This component installs `R` as well as optionally installing desired R packages.

## Requires

* OS: Ubuntu >= 18

## Description

Uses the external role `oefenweb.ansible-r` (see [here](https://github.com/Oefenweb/ansible-r)) to install R and dependencies.

## Variables

- `r_workbench_version`: Optional. String. Version of R to install. Default: `40` (install R > `4.0`).
- `r_workbench_cran_mirror`: Optional. String. URL to a CRAN mirror to use for installing packages. Default: `https://cran.rstudio.com/`.
- `r_workbench_packages`: Optional. String. A list of YAML objects defining R packages to be installed. For example:

```yaml
- { name: dplyr }
- { name: Biobase, type: bioconductor }
- { name: mangothecat/franc, type: github }
```

See the [external role](https://github.com/Oefenweb/ansible-r?tab=readme-ov-file#advanced) for more documentation.

## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
