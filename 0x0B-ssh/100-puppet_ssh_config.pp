#!/usr/bin/env bash
# Client configuration file (w/ Puppet)
file { 'Config Puppet'
    path => '~/.ssh/holberton'
    line => 'PasswordAuthentication no'
}
