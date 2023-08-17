# Puppet manifest logs in with holberton user
exec { 'replace_nofile_limit_1':
  command => '/usr/bin/sudo /bin/sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before  => Exec['replace_nofile_limit_2'],
}

exec { 'replace_nofile_limit_2':
  command => '/usr/bin/sudo /bin/sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
