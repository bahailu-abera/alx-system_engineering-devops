# Puppet manifest to set ULIMIT variable in /etc/default/nginx

# Set ULIMIT value
$ulimit_value = '-n 1048576'

# Define file path
$file_path = '/etc/default/nginx'

# Ensure the file exists
file { $file_path:
  ensure => present,
}

# Set the content of the file
file_line { 'set_ulimit':
  path   => $file_path,
  line   => "ULIMIT=${ulimit_value}",
  match  => '^ULIMIT=',
  notify => Exec['reload_nginx'],
}

# Reload Nginx service when the file is updated
exec { 'reload_nginx':
  command     => '/usr/sbin/service nginx reload',
  refreshonly => true,
  subscribe   => File[$file_path],
}
