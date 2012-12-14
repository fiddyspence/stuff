class mco_puppetca {

  file { '/opt/puppet/libexec/mcollective/mcollective/agent/puppetca.rb':
    ensure => present,
    owner  => 'root',
    group  => 'root',
    mode   => '0644',
    source => "puppet:///modules/${module_name}/puppetca.rb",
  }
  file { '/opt/puppet/libexec/mcollective/mcollective/agent/puppetca.ddl':
    ensure => present,
    owner  => 'root',
    group  => 'root',
    mode   => '0644',
    source => "puppet:///modules/${module_name}/puppetca.ddl",
  }

  # this section to distribute the mcollective client configuration for ${provisioning} to use
  # to send the puppetca messages.  it's a static file at the moment, but templating it out
  # is probably a sensible move.  note that the file that shipped with this module was configured
  # to use PSK - avoid this in production, use ssl or aes plugins for better security - that way
  # you only need to ship client public keys, and keep the private portion safe and job's a goodun
  # the alternative is to manage the security out of band, and not do this.

  file { '/etc/cobbler':
    ensure => directory,
  }
  file { '/etc/cobbler/mcollective_config':
    ensure => file,
    owner  => 'root',
    group  => 'root',
    mode   => '0600',
    source => "puppet:///modules/${module_name}/mcollective_config",
  }
}
