# This Puppet manifest installs and configures Nginx with a 301 redirect

# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Configure Nginx site
file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => "server {
    listen 80;
    location / {
        echo 'Hello World!';
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}",
}

# Enable the site by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Reload Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
  require => [Package['nginx'], File['/etc/nginx/sites-enabled/default']],
  subscribe => File['/etc/nginx/sites-enabled/default'],
}

