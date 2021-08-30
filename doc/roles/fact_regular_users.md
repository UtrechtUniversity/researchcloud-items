# Role <name>
[back to index](../index.md#Roles)

## Summary
Makes filtered information from /etc/passwd available as an Ansible variable
with usernames and other properties of regular users (excluding system process users).

## Requires
Linux flavor operating system.

## Description
The role sets the variable `{{fact_regular_users}}` to a json object list of users. 

Example content with just one user named "foo": 
` [   { user: "foo", 
        userid: 1000, groupid: 1000, 
        home: "/home/foo", 
        shell: "/bin/bash",
        description: "sample user foo"
      }  
  ]`

Example how to use in a playbook:
`- name: example
   copy:
     src: "info.txt"
     dst: "/{{ item.home }}/info.txt"
     owner: "{{ item.user }}"
     group: "{{ itemn.user }}"
     mode: 0644
   with_items: "{{ fact_regular_users }}"
`
## Variables
The variable `fact_regular_users` is filled/overwritten.

## See also
Role [runonce](runonce.md).


## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
