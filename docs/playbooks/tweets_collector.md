# Playbook tweets_collector
[back to index](../index.md#Playbooks)

## Summary
This playbook has been made for the "Waysdorf" project to gather tweets.
This playbook (for now) only installs certain dependencies and requirements, not the actual tweet collector.

## Requires
A Linux-based OS.

## Description
The playbook installs pip system-wide and pyenv and poetry for each user individually, allowing them to work in parallel without clashing dependencies.
Additonally, the playbook runs the git_clone role, which clones reposiories, if supplied as arguments.

## Variables
* repositories: A string of semi-colon (`;`) seperated URLs to git respositories (`HTTPS` format). Defaults to `default`, which aborts the playbook run.
* git_dir: The directory to clone the repositories into. Defaults to `/git/var/`.

## History
2022 Written by Sytse Groenwold (Utrecht University)

[back to index](../index.md#Playbooks)
