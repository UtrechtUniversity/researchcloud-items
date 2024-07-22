# Playbook camunda
[back to index](../index.md#Playbooks)

## Summary
[Camunda](https://www.camunda.com) is an open source workflow engine to
process business workflows specified in [Business Process Model and Notation (BPMN)](https://www.bpmn.org/)
language.

## Requires
Ubuntu operating system with desktop environment (including nginx/tomcat).

## Description
Installs the Camunda Modeller and the Camunda BPMN Workflow Engine (camunda server). 
The Workflow service is accessible via the internet on endpoint `/camunda/...`. 
The modeler is accessed via the desktop menu.

## Variables
See variable definitions in roles [camunda_modeler](../roles/camunda_modeler.md)
and [camunda_server](../roles/camunda_server.md).

## See also
[camunda-modeler](camunda-modeler.md)

## History
2021 Written by Ton Smeele (Utrecht University)


[back to index](../index.md#Playbooks)
