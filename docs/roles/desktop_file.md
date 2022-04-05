# Role <name>
[back to index](../index.md#Roles)

## Summary
Explain the use case for this role in one or two sentences. 
This role can be used to easily install desktop items through the xdg-utils package.


## Requires
An environment that suports xdg-utils.

## Description
Elaborate on the purpose and functions of the role

## Variables

### Required variables
* `app_name`: String. The name of your application for which to install a desktop item.
* `sizes`: List of integers. The different pixel count sizes of your icons. Common sizes are 16, 22, 32, 48, 64 and 128.

### Required files
While not variables, the below files are assumed to exist in your playbook or roles `/files` or `/templates` folder.
* `app_name.desktop` file: The desktop file/template to use. Strict name convention based on the `app_name` required variable.
* `app_name-size-x-size.png` files: One file for each of your sizes of your icon. At least every `size` in the required variable `sizes` must have one representitive file. Strict name convention based on the `app_name` and `sizes` required variables.

### Optional variables
* `modules`: List. If defined, a desktop item is installed for each of the modules in the list. This is used when your application needs several desktop items. All the modules will share the same icon.

## See also
Are there any other related roles? Add a link here.

## History
2022 Written by Sytse Groenwold

[back to index](../index.md#Roles)
