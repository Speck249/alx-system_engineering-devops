# Puppet manifest fixes failed HTTP requests
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT=\"-n 4096\"\n",
  notify  => Exec['nginx-restart'],
}

exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart',
  refreshonly => true,
}
