#!/usr/bin/env python

import testinfra

print("Testing Python")

def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644

def test_python_is_installed(host):
    python = host.package("python3")
    assert python.is_installed
    assert python.version.startswith("2")
