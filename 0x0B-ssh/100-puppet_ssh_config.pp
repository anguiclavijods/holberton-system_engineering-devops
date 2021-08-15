#!/usr/bin/env bash
# Client configuration file (w/ Puppet)
file { 'Config Puppet  passwd'
    path => '~/.ssh/holberton'
    line => 'PasswordAuthentication no'
}
file { 'Config Puppet'
    path => '~/.ssh/holberton'
    line => 'IdentityFile ~/.ssh/holberton'
}
