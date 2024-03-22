# create a file school in /tmp

file { '/tmp/school':
  ensure  => present,
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  groupe  => 'www-data',
  content => 'I love Puppet',
}
