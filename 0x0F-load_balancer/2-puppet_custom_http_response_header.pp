# automate the task of creating a custom HTTP header response, but with Puppet
package { 'nginx':
  ensure => 'installed',
}

# Create index.html file
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

# Add custom HTTP header to nginx configuration
file_line { 'add_custom_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => '    add_header X-Served-By $hostname;',
  match  => '^[\s\t]*listen 80 default_server;$',
}

# Configure redirection
file_line { 'configure_redirection':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require => Package['nginx'],
}

# Ensure nginx service is running and restart if needed
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
