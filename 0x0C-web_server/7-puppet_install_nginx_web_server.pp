package {'nginx':
   ensure => installed,
}

exec {'install':
   command  => 'sudo apt-get upgrade ; sudo apt-get install -y',
   provider => shell,
}

exec {'HelloWorld':
   command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
   provider => shell,
}

service {'nginx':
   ensure => running,
   enable => true,
}
