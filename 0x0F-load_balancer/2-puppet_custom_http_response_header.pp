# Automate the task of creating a custom HTTP header response
#+ The name of the custom HTTP header must be X-Served-By
#+ The value of the custom HTTP header must be the hostname of the server Nginx is running on
#+ It configures a brand new Ubuntu machine to the requirements asked in this task

exec { 'update':
  command => 'sudo apt-get update',
  path    => '/usr/bin',
}

exec { 'upgrade':
  command => 'sudo apt-get -y upgrade',
  path    => '/usr/bin',
}

package { 'nginx':
  ensure  => present,
  name    => 'nginx',
  require => Exec['update'],
}

file_line { 'Add header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

service { 'nginx':
ensure  => running,
require => Package['nginx'],
}
