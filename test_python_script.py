#!/usr/bin/env python

import testinfra

print("Testing Python")

def test_passwd_file(host):
    passwd = host.file("/etc/passwrd")
    assert passwd.containes("root")

host = testinfra.get_host("localhost")

test_passwd_file(host)
