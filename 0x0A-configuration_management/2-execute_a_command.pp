# Using Puppet, create a manifest that kills a process named killmenow.
# Must use the exec Puppet resource and must use pkill

exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/usr/bin',
  refreshonly => true,
}
