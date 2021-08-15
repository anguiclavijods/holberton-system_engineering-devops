# Client configuration file (w/ Puppet)
file { 'Config Puppet  passwd'
    path => '~/.ssh/holberton',
    line => 'PasswordAuthentication no',
}
