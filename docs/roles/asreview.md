# Role <name>
[back to index](../index.md#Roles)

## Summary
Automatic Systematic Review (ASReview) is an application that uses active machine learning to facilitate and predict relevancy of papers during a systematic review process. 
For more information, visit the [official website](https://asreview.nl/).

## Requires
* Desktop environment
* Has been tested on Ubuntu 20.04

## Description
This role installs ASReview through pip, as recommended by the documentation.
It also adds an entry in the Application menu, and the application is run automatically when a user logs in.

## Variables
The default location projects are stored can be supplying the `asreview_path` variable to this role.
Defaults to `~/.asreview` when not set.

## See also
[asreview playbook](../playbooks/asreview.md)

## History
2022 Written by Sytse Groenwold (Utrecht University)



[back to index](../index.md#Roles)
