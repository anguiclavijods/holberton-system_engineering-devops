# Puppet that help a verify when server its failed
exec { 'fix-wordpress':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php && sudo service apache2 restart',
  provider => shell,
}
