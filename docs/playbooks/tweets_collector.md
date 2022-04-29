# Playbook tweets_collector
[back to index](../index.md#Playbooks)

## Summary
This playbook installs the tweet-collector. The documentation of that can be found here: https://github.com/UtrechtUniversity/tweet_collector.

## Requires
A Linux-based OS.

## Description
The playbook installs poetry both system-wide and for each user individually, allowing them to work in parallel without clashing dependencies.
Then the tweet-collector repository is cloned and installed through its documented command.

## See also
Role [poetry](../roles/poetry) Dependency for installing the tweet-collector

## History
2022 Written by Sytse Groenwold (Utrecht University)

[back to index](../index.md#Playbooks)
