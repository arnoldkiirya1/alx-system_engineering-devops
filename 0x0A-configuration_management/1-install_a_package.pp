# Puppet manifest to install Flask package

package { 'python3-pip':
  ensure => 'installed',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

