# executes a pkill command

exec { 'pkill -f killmenow':
  command => 'pkill -f killmenow',
  path    =>  [ '/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/' ]
}
