#!/usr/bin/env python

import testinfra

print("Testing Python")

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

def test_python_is_installed(host):
    python = host.package("python3")
    assert python.is_installed, "Python should be install on image"
    #assert python.version.startswith("2"), "Python should be version 2"
