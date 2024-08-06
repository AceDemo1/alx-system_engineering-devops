#config_file
include stdlib

file_line {'password':
  ensure => present;
  path => ~/etc/ssh/ssh_config',
  line => 'PasswordAuthentication',
}

file_line {'Indentity_file':
  ensure => pesent,
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}
