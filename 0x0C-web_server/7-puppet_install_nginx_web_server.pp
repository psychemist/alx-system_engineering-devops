# installs nginx on a new server using puppet

package { 'nginx':
  ensure => 'present',
}

exec { 'update and install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'hello world':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec { 'redirect':
  command  => 'sudo sed -i "s/server_name _;/server_name _;\\n\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/google.com;\\n\\t}\\n/" /etc/nginx/sites-available/default',
  provider => shell,
}

exec { 'start':
  command  => 'sudo service nginx restart',
  provider => shell,
}
