# == Class: mysqlbackup
#
# Full description of class mysqlbackup here.
#
# === Parameters
#
# Document parameters here.
#
# [*sample_parameter*]
#   Explanation of what this parameter affects and what it defaults to.
#   e.g. "Specify one or more upstream ntp servers as an array."
#
# === Variables
#
# Here you should define a list of variables that this module would require.
#
# [*sample_variable*]
#   Explanation of how this variable affects the funtion of this class and if it
#   has a default. e.g. "The parameter enc_ntp_servers must be set by the
#   External Node Classifier as a comma separated list of hostnames." (Note,
#   global variables should not be used in preference to class parameters  as of
#   Puppet 2.6.)
#
# === Examples
#
#  class { mysqlbackup:
#    servers => [ 'pool.ntp.org', 'ntp.local.company.com' ]
#  }
#
# === Authors
#
# Author Name <author@domain.com>
#
# === Copyright
#
# Copyright 2011 Your name here, unless otherwise noted.
#
class mysqlbackup {

  file { '/usr/bin/automysqlbackup':
    ensure => file,
    source => "puppet:///modules/${module_name}/automysqlbackup",
  }

  file { '/etc/automysqlbackup':
    ensure => directory,
  }

  file { '/etc/automysqlbackup/automysqlbackup.conf':
    ensure  => file,
    source  => "puppet:///modules/${module_name}/automysqlbackup",
    replace => false,
  }

  cron { 'automysqlbackup':
    ensure  => present,
    command => '/usr/bin/automysqlbackup 2&> /dev/null',
  }

}
