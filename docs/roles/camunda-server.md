# Role camunda-server
[back to index](../index.md#Roles)

## Summary
[Camunda](https://www.camunda.com) is an open source workflow engine to
process business workflows specified in [Business Process Model and Notation (BPMN)](https://www.bpmn.org/)
language.

## Requires
Ubuntu operating system with desktop environment (including nginx/tomcat).

## Description
Installs the Camunda BPMN Workflow Engine behind a Tomcat application server. 
The service is accessible via the internet on endpoint `/camunda/...`. 

## Variables
The following variables and defaults are available:
```
camunda_version: "7.15"
camunda_release: "7.15.0"
camunda_war_urldir: "https://downloads.camunda.cloud/release/camunda-bpm/tomcat/{{ camunda_version }}"
camunda_war_urlfile: "camunda-webapp-tomcat-standalone-{{ camunda_release }}.war"
camunda_dir: "/etc/camunda "
camunda_context_name: "camunda"
catalina_home: "/var/lib/tomcat9"
``` 

## See also
Other roles will be added to install Camunda Modeler.

## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
