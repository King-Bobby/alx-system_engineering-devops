# Using Puppet, make changes to a configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => @(EOF),
Host <server_hostname_or_ip>
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
EOF
}
