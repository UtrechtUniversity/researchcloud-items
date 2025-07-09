# Playbook iRODS Sync
[back to index](../index.md#Playbooks)

## Summary

This component will sync one or more collections (directories) from an iRODS (or Yoda) server to the workspace when the workspace is created.

Under the hood this component uses the [Ansible module](https://github.com/UtrechtUniversity/ibridges-ansible/) for [iBridges](https://github.com/UtrechtUniversity/ibridges), an iRODS client library written in Python. The main advantages of this is security: the password you pass to the component is never stored on disk, as it directly calls the iBridges Python API.

The protocol used is the iRODS data transfer protocol, which is fast and suitable for transfer of large files. Keep in mind that  copying (very) large datasets will impact workspace creation time.

You can configure a target directory on the workspace under which each requested collection will created (see [below](#variables)).

The component will sync and not simply download files, meaning that iBridges will perform a comparison of the target folder and the iRODS path: only changed files on iRODS will be downloaded.

### File ownership

If the target directory is under a user's homedirectory (for instance, `/home/testuser` or `/home/testuser/synced_from_yoda`), file ownership of the downloaded collections will automatically be set to that user (e.g. `testuser`). If the target directory is not in a home directory, the files will by default be owned by `root`. You can always override this using the `ibridges_user` and `ibridges_group` [variables](#variables).

### Credentials

This component requires a CO secret (default name: `irods_password`) to be defined containing the password used for the connection. The username should be part of the `ibridges_env` parameter, which should contain a JSON object defining connection details (see [below](#variables)).

**Security Note**: after you add the CO secret containing the iRODS password, it then cannot be read by users in the portal. However, **users in the same CO can still create a component and catalog item that references the CO secret, and in that way gain access to it**. The component should therefore only be used in controlled environments.

## Requires

- Linux operating system

## Source

The source for this component is currently in a different repository: [https://github.com/UtrechtUniversity/ibridges-ansible/](https://github.com/UtrechtUniversity/ibridges-ansible/)

This is because the component uses a custom Ansible module that we want to distribute independently of the component. In the near future, we'll make the module available on Ansible Galaxy, so that the component playbook can be moved to our [default repository](https://github.com/UtrechtUniversity/researchcloud-items).

## Description

The playbook:

* installs the latest iBridges version from `pip` under `/usr/local/pip` if it doesn not exist yet.
* syncs the requested collections to the target directory.
* updates ownership for the synced directories.

## Variables

* `ibridges_irods_path`: *Required*. String. Comma-separated list of iRODS paths to be downloaded. For example: `~/my-collection1,~/my-collection2`. See [here](https://github.com/UtrechtUniversity/iBridges/blob/develop/tutorials/01-iRODS-paths.ipynb) for how to understand iRODS paths.
* `ibridges_target_path`: *Required*. String. Path to which the downloaded collections should be saved. For instance: `/home/testuser/` will sync `my-collection1` to `/home/testuser/my-collection-1`. If the target directory does not exist yet, it will be created.
* `ibridges_env`: *Required*. String. Paste the contents of a valid iRODS environment file (JSON format) here. See example below:
* `ibridges_password`: *Required*. String. The name of the CO secret containing the password to be used for the connection. Default: `{"key": "irods_password"}`.
* `ibridges_user`: String. The username of the user that should own the downloaded collections. Default: `root`.
* `ibridges_group`: String. The name of the group that should own the downloaded collections. Default: `root`.

Below is an example of a valid JSON value for the `ibridges_env` parameter (see [here](https://www.uu.nl/en/research/yoda/guide-to-yoda/i-am-using-yoda/using-icommands-for-large-datasets) for a list of environments for Utrecht University Yoda servers):

```json
{  
"irods_host": "i-lab.data.uu.nl", 
"irods_port": 1247,  
"irods_home": "/nluu5p/home",  
"irods_user_name": "exampleuser@uu.nl",  
"irods_zone_name": "nluu5p",  
"irods_authentication_scheme": "pam",  
"irods_encryption_algorithm": "AES-256-CBC",  
"irods_encryption_key_size": 32,  
"irods_encryption_num_hash_rounds": 16,  
"irods_encryption_salt_size": 8,  
"irods_client_server_policy": "CS_NEG_REQUIRE",
"irods_client_server_negotiation": "request_server_negotiation"
}
```

## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
