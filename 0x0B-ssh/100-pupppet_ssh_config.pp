# client ssh configuration

$str = "
Include /etc/ssh/ssh_config.d/*.conf
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
"
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => $str
}
