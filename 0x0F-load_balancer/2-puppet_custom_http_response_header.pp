# Ensure nginx package is installed
package { 'nginx':
  ensure => 'installed',
}

# Create index.html file
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

# Add custom HTTP header to nginx configuration
# Add custom HTTP header to nginx configuration
exec {'HTTP header':
  command  => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell'
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
