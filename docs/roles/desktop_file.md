# Role desktop_file
[back to index](../index.md#Roles)

## Summary
Explain the use case for this role in one or two sentences. 
This role can be used to easily install desktop items through the xdg-utils package.


## Requires
An environment that suports xdg-utils.

## Description
The purpose of this role is to make the code to install desktop file menu items through xdg-utils reusable.
This role cannot be a role on itself, due to the requirement of icon files. It has to be called from inside another role that holds the icon files in their respective `files` or `templates` folder. See below example:

```
# File structure of using this role

researchcloud-items > roles
└─── application_role
│   └───files
│       │   app_name-XX-x-XX.png
│       templates
│       │   app_name.desktop.j2
|       tasks
│       │   main.yml
│   
└─── desktop_file
    │   ...
```

The actual role can be called and passed variables as follows:

```
#researchcloud-items > roles > application_role > tasks > main.yml

[...]
- name: Create desktop menu items through role
  include_role:
    name: desktop_file
  vars:
    app_name: <app_name>
    sizes:
      - <size1 int>
      - <size2 int>
      ...
    modules:
      - <desktop item>
      - <desktop item>
    var_required_for_app_name.desktop.j2: value
    ...
[...]
```

Elaborate on the purpose and functions of the role

## Variables

### Required variables
* `app_name`: String. The name of your application for which to install a desktop item.
* `sizes`: List of integers. The different pixel count sizes of your icons. Common sizes are 16, 22, 32, 48, 64 and 128.

### Required files
While not variables, the below files are assumed to exist in your playbook or roles `/files` or `/templates` folder. See the file structure example above.
* `app_name.desktop` file: The desktop file/template to use. Strict name convention based on the `app_name` required variable.
* `app_name-size-x-size.png` files: One file for each of your sizes of your icon. At least every `size` in the required variable `sizes` must have one representitive file. Strict name convention based on the `app_name` and `sizes` required variables.

### Optional variables
* `modules`: List. If defined, a desktop item is installed for each of the modules in the list. This is used when your application needs several desktop items. All the modules will share the same icon.
* If your `app_name.desktop` file is a Jinja2 template that holds variables, ensure that those variables are passed to this role as well.

## See also
Are there any other related roles? Add a link here.

## History
2022 Written by Sytse Groenwold

[back to index](../index.md#Roles)
