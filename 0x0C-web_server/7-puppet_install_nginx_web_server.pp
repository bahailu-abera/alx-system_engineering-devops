# install and configure nginx web server
include nginx

class nginx {
  package { 'apache2.2-common':
    ensure => absent,
  }
  package { 'nginx':
    ensure  => installed,
    require => package['apache2.2-common'],
  }
  service { 'nginx':
    ensure  => running,
    require => package['nginx'],
  }
}
