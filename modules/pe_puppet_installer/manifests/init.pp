class pe_puppet_installer {

  $minute = fqdn_rand('30')
  $minute_two = fqdn_rand('30','30')

  if ! $::fact_is_puppetmaster {

    package { 'integralis-puppet-agent-installer':
      ensure => present,
    } ->
    service { 'pe-puppet':
      enable => false,
      ensure => stopped,
    } ->
    cron { 'pe-puppet-agent':
      ensure  => present,
      command => '/opt/puppet/bin/puppet agent -t --noop --logdest syslog 2>&1 /dev/null',
      minute  => [$pe_puppet_installer::minute,$pe_puppet_installer::minute_two]
    }
  }
  }
}
