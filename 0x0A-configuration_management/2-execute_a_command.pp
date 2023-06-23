# Kill a process using exec Puppet resource

exec { 'kill_process':
  command  => 'pkill killmenow',
  path     => '/usr/bin',
  provider => shell,
  onlyif   => 'pgrep killmenow'
}
