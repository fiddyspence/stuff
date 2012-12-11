class pe_puppet_installer ($daemon = false, $cron = true) {

  $minute = fqdn_rand('30')
  $minute_two = fqdn_rand('30','30')

  if $daemon == true {
    $service_ensure = running
    $service_enable = true
  } else {
    $service_ensure = stopped
    $service_enable = false
  }
  if $cron == true {
    $cron_ensure = present
  } else {
    $cron_ensure = absent
  }

  notify {$::fact_is_puppetmaster:}
  case $::fact_is_puppetmaster {

    'false': {

    package { 'integralis-puppet-agent-installer':
      ensure => present,
    } ->
    service { 'pe-puppet':
      enable    => $service_enable,
      ensure    => $service_ensure,
      hasstatus => false,
      pattern   => '/\/opt\/puppet\/bin/puppet\ agent/',
    } ->
    cron { 'pe-puppet-agent':
      ensure  => present,
      command => '/opt/puppet/bin/puppet agent -t --noop --logdest syslog 2>&1 /dev/null',
      minute  => [$pe_puppet_installer::minute,$pe_puppet_installer::minute_two]
    }
    }
  }
}
