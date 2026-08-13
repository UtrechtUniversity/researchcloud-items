# Role r_ubuntu_binaries
[back to index](../index.md#Roles)

## Summary
Sets up the [r2u](https://github.com/eddelbuettel/r2u) apt repository for installing precompiled R packages as apt packages.

## Requires
- Ubuntu == 24.04

## Description
This role enables the use of apt from within R to install CRAN packages that are precompiled for Ubuntu from the [r2u repository](https://github.com/eddelbuettel/r2u).

Used in combination with the `rstudio` and `r_bspm` roles. Installation in the following order:

- r_ubuntu_binaries
- rstudio
- r_bspm

## See also
- [rstudio](./rstudio.md)
- [r_bspm](./r_bspm.md)

## History
2026 Written by Jelle Treep (Universiteit Utrecht) 

[back to index](../index.md#Roles)
