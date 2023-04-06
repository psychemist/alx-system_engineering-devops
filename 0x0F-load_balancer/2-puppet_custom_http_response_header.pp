# automates the creation of a custom HTTP header response on web servers

exec { 'get update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'present',
}

exec { 'add_header':
  command  => 'sudo sed -i "s/server_name _;/server_name _;\\n\\n\\t add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default'
  provider => shell,
}

exec { 'start':
  command => 'usr/sbin/service nginx restart',
}
