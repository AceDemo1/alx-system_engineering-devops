#automation
package { 'nginx':
  ensure => 'installed',
}

file_line { 'header':
  ensure => 'present',
  path => '/etc/nginx/sites-available/default',
  after => 'server_name_;',
  line => 'add_header X-Served-By $hostname;',
}

service { 'nginx':
  ensure => 'running',
  require => Package['nginx'],
}
