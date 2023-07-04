#!/usr/bin/env bash
class nginx {
      package { 'nginx':
       ensure => present
      }

      file { '/etc/nginx/conf.d/custom.conf':
       ensure => present
       content => 'server {
         listen 80;
         server_name _;
         add_header X-Served-By ${::hostname};
       }'
     }
}
