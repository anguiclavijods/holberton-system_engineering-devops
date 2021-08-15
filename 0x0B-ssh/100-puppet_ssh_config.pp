# Client configuration  file (w/ Puppet)

file_line { 'config puppet':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'config puppet passwd':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}