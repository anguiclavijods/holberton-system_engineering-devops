# Execute a command
exec { 'pkill killmenow':
  path    => '/user/bin',
}
