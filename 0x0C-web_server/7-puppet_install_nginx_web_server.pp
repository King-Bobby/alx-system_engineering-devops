# Using puppet, install and configure an Nginx server
# also include resources in your manifest to perform a 301 redirect when querying /redirect_me.

class nginx {
	package { 'nginx' :
		ensure => installed,
	}

	service { 'nginx' :
		ensure => running,
		enable => true,
		require => Package['nginx'],
	}

	file { '/var/www/html/index.html' :
		content => 'Hello World!',
		require => Package['nginx'],
	}

	file { '/etc/nginx/sites-available/default/' :
		ensure => present,
		source => 'puppet:///modules/nginx/default',
		notify => Service['nginx'],
	}
}

class nginx::redirect {
	file { '/etc/nginx/sites-available/redirect' :
		ensure => present,
		content => "server {\n  listen 80;\n  server_name _;\n  return 301 https://google.com;\n}\n",
		notify => Service['nginx'],
	}

	file { '/etc/nginx/sites-enabled/redirect':
    	ensure => link,
		target => '/etc/nginx/sites-available/redirect',
		require => File['/etc/nginx/sites-available/redirect'],
		notify => Service['nginx'],
	}
}

include nginx
include nginx::redirect
