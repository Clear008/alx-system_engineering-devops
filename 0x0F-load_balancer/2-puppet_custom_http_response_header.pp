# automate the task of creating a custom HTTP header response, but with Puppet
## Ensure nginx package is installed
package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

file_line { 'add_custom_http_header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
