# A Quick Introdction To TestInfra

## Introduction
### Ansible -> Molecule -> TestInfra
Ansible and Molecule work hand in hand, as Molecule is a testing framework built to specifically test Ansible roles and playbooks in isolation by launching a docker image that will run your Ansible playbooks over and test to verify everything is build correctly.

### TestInfra 
Once your server has been created and is running, TestInfra can then run against the host and test the actual server state.
With Testinfra you can write unit tests in Python to test your servers configured by management tools like Salt, Ansible, Puppet, Chef and so on.

"""Testinfra aims to be a Serverspec equivalent in python and is written as a plugin to the powerful Pytest test engine."""

## Installation

```
python3 -v

pip3 install testinfra
```

## Example Code
```
def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644
    
def test_system_os(host):
    assert host.system_info.type == "linux"
    assert host.system_info.distribution == "ubuntu"
    assert host.system_info.release == "20.04"
    
def test_internet_access(host):
    google = host.addr("google.com")
    assert google.is_resolvable
    assert google.is_resolvable
    
def test_finding_ls(host):
    ls_command = host.find_command("ls")
    assert ls_command == "/usr/bin/ls"
    
def test_run_listing(host):
    run_ls = host.run("ls -l /")
    assert run_ls.succeeded

def test_python_is_installed(host):
    python = host.package("python3")
    assert python.is_installed, "Python should be install on image"
    #assert python.version.startswith("2"), "Python should be version 2"
```

## Important Modules
- addr - Test remote addresses
- block_device - Test if a block device has been created
- docker - Test if docker is running on system
- file - Test various files attributes have been created
- interface - Test if network interfaces exist(eth0)
- package - Test the package status and version
- pip - Test pip package manager and packages
- process - Test process attributes
- service  - Test services are available and status
- sysctl - Test kernel parameters
- system_info - Test for system specific information
- user/group - Test if users or groups have been created
- find_command - Return the path for a specific command
- run - Run given commands and test against results

## Connecting To Your Host
- local
- paramiko
- docker
- ssh
- salt
- ansible
- kubectl
- winrm
- LXC/LXD


