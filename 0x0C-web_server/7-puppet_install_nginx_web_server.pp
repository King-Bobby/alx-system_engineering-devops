#Using puppet, install nginx and also include resources in your manifest
# to perform a 301 redirect when querying /redirect_me.

class nginx {
    package { 'nginx':
        ensure => installed,
    }

    service { 'nginx':
        ensure => running,
        enable => true,
        require => Package['nginx'],
    }

    file { '/var/www/html/index.html':
        content => 'Hello World!',
        require => Package['nginx'],
    }

    file { '/etc/nginx/sites-available/default':
        ensure => present,
        content => "
            server {
                listen 80;
                server_name _;
                root /var/www/html;
                
                location / {
                    return 200 'Hello World!';
                }
                
                location /redirect_me {
                    return 301 https://google.com;
                }
            }
        ",
        notify => Service['nginx'],
    }

    file { '/etc/nginx/sites-enabled/redirect':
        ensure => link,
        target => '/etc/nginx/sites-available/default',
        require => File['/etc/nginx/sites-available/default'],
        notify => Service['nginx'],
    }
}

include nginx
