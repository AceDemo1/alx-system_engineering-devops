# Change OS configuration

exec { 'change_login':
  command => 'sed -i s/holberton/#holberton /etc/security/limits.conf',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
