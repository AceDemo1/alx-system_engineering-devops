#install nginx
package { 'nginx':
  ensure => 'installed',
}

file_line { 'redirect':
  ensure => 'present',
  path => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line => 'location /redirect { return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4; }',
}

file { 'helloword!':
  ensure => 'present',
  path => '/var/www/html/index.html',
  content => 'Hello World!',
}

service { 'nginx':
  ensure => 'running',
  require => Package['nginx'],
}
