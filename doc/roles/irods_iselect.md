# Role irods_iselect
[back to index](../index.md#Roles)

## Summary
Installs the iselect tool as a means to configure commandline access to iRODS zones.
 

## Requires
Linux distribution, also depends on role [irods_icommands](./irods_icommands.md)

## Description
The iselect Linux shell command allows the user to select an iRODS zone from a list,
then configures the user's iRODs environment so that she can connect to that zone. 
Finallly, `iinit` is called to allow to user to 
add individual settings such as username/password.

Example use iselect:
```
    iselect
    iselect uu
```
Without arguments, iselect will present a list of all known zones. An argument
can be used to filter the list on zones that partially match the argument.

Known zones are maintained as json key/value structures in a file 
located at `/etc/irods_zones.json`.
This file is formatted as follows:
```
     { "<name>": { "description": "some text to describe the zone here...",
                        "config": { <content for .irods_environment file> },
       "<name>": ...
     }
```

## Variables
```
    irods_iselect_file: "zones-uu.json"
```
The default value may be overridden to select an alternative source file
containing a list of iRODS zones. 
The file needs to exist in the `files` section of this role.


## See also
- [irods_repo](./irods_repo.md)  
- [irods_icommands](./irods_icommands.md)  
- [irods_skel](./irods_skel.md)


## History
2021 Written by Ton Smeele (Utrecht University)


[back to index](../index.md#Roles)
