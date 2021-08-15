# Client configuration  file (w/ Puppet)

file { 'config Puppet  passwd':
    path => '~/.ssh/holberton',
    line => 'PasswordAuthentication no',
}

file { 'config Puppet':
    path => '~/.ssh/holberton',
    line => 'IdentityFile ~/.ssh/holberton',
}
