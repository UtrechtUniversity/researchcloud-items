# Role julia
[back to index](../index.md#Roles)

## Summary
Installs the [Julia](https://julialang.org/) programming language, along with [juliaup](https://github.com/JuliaLang/juliaup) (a version manager for Julia).

## Requires

- Linux OS

## Description

This role installs `juliaup`, the latest `julia`, and makes available a shared Julia packages depot for all users. The steps it takes are:

1. Installs `juliaup` for the `root` user only. *Note*: installing `juliaup` globally for all users currently (November 2025) does not work because of [this issue](https://github.com/JuliaLang/juliaup/issues/276).
2. `juliaup` will automatically install the latest stable version of `julia`.
3. We symlink the installed `julia` interpreter to `/usr/local/bin/julia` so all users can use it.
4. We set the `JULIA_DEPOT_PATH` and `JULIA_LOAD_PATH` variables for all users such that `julia` will detect the shared depot. However, the shared depot is read-only. When users install new packages, they will be installed into the user's own julia depot directory (`~/.julia` by default).

This role sets the fact `fact_julia_dir` to the value of the `julia_shared_env_path` [variable](#variables), so other roles in a playbook can access it.

## Variables

- `julia_shared_env_path`: String. Path to the shared `julia` package depot. Default: `/usr/local/uu/env/julia`

## History
2025 Written by Dawa Ometto

[back to index](../index.md#Roles)
