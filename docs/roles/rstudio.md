# Role rstudio
[back to index](../index.md#Roles)

## Summary
Installs RStudio Desktop or Server.

## Requires
- Ubuntu >= 20.04
- Untested supported for RHEL-like Linux

## Description
Installation is done using apt and the debian package available [here](https://posit.co/download/rstudio-desktop/).

## Variables

- `rstudio_kind`: String. Whether to install the desktop or server version of RStudio.  Default: `desktop` (set to `server` alternatively).

## History
2022 Written by Sytse Groenwold (Universiteit Utrecht)  
2024 Updated by Jelle Treep (Utrecht University)
2025 Updated by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
