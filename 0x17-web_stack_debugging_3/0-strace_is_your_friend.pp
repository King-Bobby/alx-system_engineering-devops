# Apache returns 500; use this script to fix typo error in config

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => inline_template("<%= File.read('/var/www/html/wp-settings.php').gsub('.phpp', '.php') %>"),
  require => Package['apache2'],  # Adjust the package name if needed
}
