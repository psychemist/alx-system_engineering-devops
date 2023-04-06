# automates the creation of a custom HTTP header response on web servers

exec { 'installation':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sudo sed -i "/server_name _;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
