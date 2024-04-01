# automate the task of creating a custom HTTP header response, but with Puppet
## Ensure nginx package is installed


exec { 'update_system':
  command => '/usr/bin/apt-get -y update',
}

exec { 'install_nginx':
  command => '/usr/bin/apt-get -y install nginx',
  require => Exec['update_system'],
}

exec { 'add_custom_http_header':
  command => 'sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
  require => Exec['install_nginx'],
}

exec { 'restart_nginx':
  command => 'service nginx restart',
  require => Exec['add_custom_http_header'],
}
