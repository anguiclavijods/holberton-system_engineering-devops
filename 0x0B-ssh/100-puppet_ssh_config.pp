# Client configuration  file (w/ Puppet)
file { 'config Puppet':
    path => '~/.ssh/holberton',
    line => 'IdentityFile ~/.ssh/holberton',
}
file { 'config Puppet  passwd':
    path => '~/.ssh/holberton',
    line => 'PasswordAuthentication no',
}
