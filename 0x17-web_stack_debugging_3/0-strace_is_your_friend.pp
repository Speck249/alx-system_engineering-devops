# Puppet manifest resolves 500 error
file { '/var/www/html/wp-settings.php':
  ensure => present,
}

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin'],
  onlyif  => "grep -q 'phpp' /var/www/html/wp-settings.php",
  require => File['/var/www/html/wp-settings.php'],
}
