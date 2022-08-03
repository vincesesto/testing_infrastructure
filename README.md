# A Quick Introdction To TestInfra

## Introduction
### Ansible -> Molecule -> TestInfra
Ansible and Molecule work hand in hand, as Molecule is a testing framework built to specifically test Ansible roles and playbooks in isolation by launching a docker image that will run your Ansible playbooks over and test to verify everything is build correctly.

### TestInfra 
Once your server has been created and is running, TestInfra can then run against the host and test the actual server state.
With Testinfra you can write unit tests in Python to test your servers configured by management tools like Salt, Ansible, Puppet, Chef and so on.

"""Testinfra aims to be a Serverspec equivalent in python and is written as a plugin to the powerful Pytest test engine."""

