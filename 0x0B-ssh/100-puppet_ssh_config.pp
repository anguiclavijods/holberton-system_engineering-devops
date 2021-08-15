# Client configuration  file (w/ Puppet)
file_line { 'config Puppet  passwd':
    path => '~/.ssh/holberton',
    line => 'PasswordAuthentication no',
}
