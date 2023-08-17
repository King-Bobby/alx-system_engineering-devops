# Fixing error "accept4() failed (24: Too many open files)"

exec {'increasing nginx file limit':
  command => 'sed -i "s/15/12000" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
