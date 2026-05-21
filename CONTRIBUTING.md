# Contributing

We are very happy with any suggestions or contributions to improve the contents. Feel free to add Issues e.g. for feature requests or submit a pull request to add ansible scripts for Research Cloud plugins. When adding a research cloud plugin, read the [documentation guidelines](https://utrechtuniversity.github.io/researchcloud-items/).

## Issues
The easiest way to contribute is to submit an [issue](https://github.com/UtrechtUniversity/researchcloud-items/issues), and make your suggestions about new features, plugins or other issues.

## Pull requests
If you are comfortable with git and pull requests, you can also submit a pull request where you directly suggest changes to the contents of this repository. Read more about how pull requests work [here](https://app.egghead.io/playlists/how-to-contribute-to-an-open-source-project-on-github).

In short:

1. Fork the repository and clone it locally.
1. Create a new branch in your desktop copy of this repository.
1. Commit the change in that branch.
1. [Update version](#versioning) if required.
1. Push that branch to your fork of this repository on GitHub
1. Submit a pull request from that branch to the main branch of the master repository. 
1. If you receive feedback, make changes on your desktop and push to your branch on GitHub: the pull request will update automatically.

**Note**: in order not to needlessly trigger test workflows, please convert your PR to a draft while you are still working on it. When ready, mark your PR as "ready for review". This will ensure tests are run.

## Versioning Policy

This repository contains an Ansible collection, and its version is defined in the `galaxy.yml` file at the root of the repository. Ansible Galaxy requires **full semantic versioning**, so we use the format **`X.Y.Z`**:

- **Major (`X`)** — increment when making backwards‑incompatible changes  
- **Minor (`Y`)** — increment when adding new features in a backwards‑compatible way  
- **Patch (`Z`)** — increment for bugfixes or internal improvements  

When a pull request that modifies `galaxy.yml` is merged into `main`, our CI workflow automatically creates three Git tags:

- **`vX.Y.Z`** — an immutable tag representing the exact release  
- **`vX.Y`** — a floating minor tag that always points to the latest patch release within that minor series  
- **`vX`** — a floating major tag that always points to the latest release within that major series  

Users of the collection can depend on the exact version (`vX.Y.Z`) for reproducibility, or use the floating minor (`vX.Y`) or major (`vX`) tags to automatically track the latest compatible releases.

**If you do not change the patch-level release for small changes, no new tags will be produced. Maintainers may also choose to 'collect' patch-level releases over a small period of time, and update the version afterwards.**

## Style guides

### Branch naming conventions

When creating a new branch to base a PR on, please try to use the following naming convention:

1. If your PR fixes an issue (for example issue `#123`), give your branch the name `fix/123`, `feat/123`, or `chore/123` depending on whether the issue involves a **bug** (fix), **new feature** (feat), or a **chore** (such as updating dependencies, workflow files, or fixing styling).
2. If your PR does not fix an existing issue (preferably it should!), use descriptive naming such as `doc-add_myrole` (adding documentation), or `feat-new_rstudio`.

### Commit messages

Give commits clear and concise messages. Since this is a monorepo, it helps to indicate what role or playbook your commit touches. For example:

1. `role fact_regular_users: use faster module to get existing users`
2. `playbook rstudio: support Ubuntu 22`

If your commit addresses a **chore** (see above), start the message with `chore: ...`. If it involves documentation, use `docs: ...`.

### Documentation

Use an editorial style guide when writing documenation, preferably the [Google developer documentation style guide](https://developers.google.com/style). 
