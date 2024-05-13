# Role tweet_collector
[back to index](../index.md#Roles)

## Summary
This role installs the [tweet-collector](https://github.com/UtrechtUniversity/tweet_collector).

## Requires
None.

## Description
The playbook installs poetry both system-wide for installation and additonally for each user individually to allow users to work in parallel without clashing dependencies.
The tweet-collector repository is cloned and installed through its documented command.
A function is added to catch the launch commands, and first activates the virtualenv the tweet_collector is installed in.

## Variables
Mention any variables that can be preset by the user, and their defaults

## See also
Role [poetry](./poetry.md) Dependency for installing the tweet-collector

## History
2022 Written by Sytse Groenwold (Utrecht University)

[back to index](../index.md#Roles)
