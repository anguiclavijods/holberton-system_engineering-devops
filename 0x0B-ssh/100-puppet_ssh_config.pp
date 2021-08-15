# Client configuration  file (w/ Puppet)
file_line { 'config Puppet  passwd':
    path => 'bin/ssh/holberton',
    line => 'PasswordAuthentication no',
}
