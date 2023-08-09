# Puppet manifest resolves 500 error
$target_file = '/var/www/html/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${target_file}",
  path    => ['bin', 'usr/bin'],
  onlyif  => "grep -q 'phpp' ${target_file}",
  require => File[target_file],
}
