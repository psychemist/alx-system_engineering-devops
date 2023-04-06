# automates the creation of a custom HTTP header response on web servers

exec { 'get update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'present',
}

file_line { 'add_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

exec { 'start':
  command => 'usr/sbin/service nginx restart',
}
