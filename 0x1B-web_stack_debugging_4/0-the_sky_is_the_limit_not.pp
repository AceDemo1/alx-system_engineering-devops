# Increase traffic on server Nginx

exec { 'update_default_nginx':
  command => 'sed -i s/15/2000/ /etc/default/nginx',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
} ->

exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
