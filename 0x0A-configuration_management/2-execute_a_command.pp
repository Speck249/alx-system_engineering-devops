# Kill a process using exec Puppet resource

exec { 'kill_process':
  command => 'pkill killmenow',
  provider => shell,
  onlyif  => 'pgrep killmenow'
}
