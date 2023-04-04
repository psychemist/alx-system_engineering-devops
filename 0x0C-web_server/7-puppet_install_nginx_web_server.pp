# installs and configures an nginx server using puppet

exec { 'update':
  command => '/usr/bin/apt-get update'
  before  => Package['nginx']
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update']
}

exec { 'root':
  command => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  
}

exec { 'redirect':
  command => 'sudo sed -i "s/server_name _;/server_name _;\\n\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/google.com;\\n\\t}\\n/" /etc/nginx/sites-available/default'

exec { 'start':
  command => 'sudo service nginx restart'
  require Package['nginx']
}
