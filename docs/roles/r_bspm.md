# Role r_bspm
[back to index](../index.md#Roles)

## Summary
Installs and enables the `bspm` R package so R can manage system-installed apt packages.

## Requires
- Ubuntu == 24.04

## Description
Installation of dependencies is done using apt and `bspm` is installed using R. This role enables the use of apt from within R to install CRAN packages that are precompiled for Ubuntu from the [r2u repository](https://github.com/eddelbuettel/r2u).

Used in combination with the `rstudio` and `r_ubuntu_binaries` roles. Installation in the following order:

- r_ubuntu_binaries
- rstudio
- r_bspm

## See also
- [rstudio](./rstudio.md)
- [r_bspm](./r_bspm.md)

## History
2026 Written by Jelle Treep (Universiteit Utrecht) 

[back to index](../index.md#Roles)
