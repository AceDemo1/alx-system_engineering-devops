# Resolve Apache returning a 500 error

exec { 'fix phpp':
  command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
