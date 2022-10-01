# Install Nginx web server on a brand new ubuntu machine

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install nginx'],
}

exec {'install nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header']
  require  => Exec['update']
}

exec {'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc/nginx\/sites-enabled\/\*;\nadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart nginx'],
}

exec {'restart nginx':
  provider => shell,
  command  => 'sudo servive nginx restart',
}
