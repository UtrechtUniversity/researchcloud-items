# Role fact_regular_users
[back to index](../index.md#Roles)

## Summary
Makes filtered information from /etc/passwd available as an Ansible variable
with username and other properties of regular users (excluding system process users).

## Requires
Linux flavor operating system.

## Description
The role sets the Ansible variable `fact_regular_users` to a list of users json object. 
Information from /etc/cpasswd is filtered on: 1) userid >= 1000 and 
2) user has a home directory located underneath /home/

Example content with just one user named "foo": 
```
    [   { user: "foo", 
          userid: 1000, 
          groupid: 1000, 
          home: "/home/foo", 
          shell: "/bin/bash",
          description: "sample user foo"
        }  
    ]
```
Example use in a playbook task:
(assumes fact_regular_users is listed as a dependency for this role) 
```
    - name: copy file info.txt to home directory, for all existing users
      copy:
        src: "info.txt"
        dst: "/{{ item.home }}/info.txt"
        owner: "{{ item.user }}"
        group: "{{ item.user }}"
        mode: 0644
      with_items: "{{ fact_regular_users }}"
```

## Variables
The variable `fact_regular_users` is filled/overwritten.

## See also
Role [runonce](./runonce.md).


## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
