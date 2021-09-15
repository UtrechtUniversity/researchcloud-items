# Role camunda-modeler
[back to index](../index.md#Roles)

## Summary
The Camunda modeler is part of the [Camunda](https://www.camunda.com) suite, 
an open source workflow engine to process business workflows specified 
in [Business Process Model and Notation (BPMN)](https://www.bpmn.org/) language. 

## Requires
Ubuntu operating system with desktop environment.

## Description
Installs the Camunda Modeler tool. The modeler is a desktop application that
facilitates busines process modeling by drawing process flows.  

The modeler can be installed stand-alone or the same machine as
the Camunda server.

## Variables
The following variables and defaults are available:
```
camunda_modeler_version: "4.10.0"
camunda_modeler_release: "4.10.0"
camunda_modeler_urldir: "https://downloads.camunda.cloud/release/camunda-modeler/{{ camunda_modeler_version }}"
camunda_modeler_urlfile_prefix: "camunda-modeler-{{ camunda_modeler_release }}-linux-x64"
camunda_modeler_dir: "/var/lib/camunda-modeler"
``` 

## See also
[camunda-server](camunda-server.md)

## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
