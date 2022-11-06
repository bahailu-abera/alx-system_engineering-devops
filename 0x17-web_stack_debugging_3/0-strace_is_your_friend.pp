# pupper manifest to edit a file content
exec { 'sed':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => ['usr/bin:/usr/sbin:/bin']
}
