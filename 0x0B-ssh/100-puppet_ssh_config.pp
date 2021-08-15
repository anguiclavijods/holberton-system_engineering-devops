# Client configuration  file (w/ Puppet)

file_line { 'config Puppet':
    path => 'etc/ssh/ssh_config':
    line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'config Puppet  passwd':
    path => 'etc/ssh/holberton',
    line => 'PasswordAuthentication no',
}