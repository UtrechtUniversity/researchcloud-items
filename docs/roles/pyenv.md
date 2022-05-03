# Role pyenv
[back to index](../index.md#Roles)

## Summary
Pyenv is a Python version management tool, which lets you change the global Python version, install multiple versions and create directory specific versions (Python environments).

## Requires
* Debian-based system
* RHEL-based system

## Description
This role will install pyenv for each user individually. 
For both yum and apt based package managers, all dependencies are first downloaded.
The installation is then done through the pyenv installer script which is ran once when the user logs in.

## Variables
None.

## See also


## History
2022 Written by Sytse Groenwold (Utrecht University)

[back to index](../index.md#Roles)
