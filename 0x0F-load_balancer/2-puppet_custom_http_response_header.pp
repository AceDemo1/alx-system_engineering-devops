#automation

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

file_line { 'header':
  ensure => 'present',
  path => '/etc/nginx/sites-available/default',
  after => 'server_name_;',
  line => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure => 'running',
  require => Package['nginx'],
}
