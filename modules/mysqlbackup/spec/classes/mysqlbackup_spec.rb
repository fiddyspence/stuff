require 'spec_helper'

describe 'mysqlbackup' do
  before :all do
    @facter_facts = {
      'osfamily'              => 'RedHat',
      'lsbmajdistrelease'     => '6',
      'puppetversion'         => '2.7.6 (Puppet Enterprise 2.0.0)',
      'fact_is_puppetmaster'  => 'true',
      'fact_is_puppetconsole' => 'true',
      'fact_is_puppetagent'   => 'true',
      'fact_stomp_server'     => 'testagent',
      'fact_stomp_port'       => '6163',
    }
  end

  let :facts do
    @facter_facts
  end

  it { should include_class('mysqlbackup') }

  it { should contain_file('/etc/automysqlbackup').with_ensure(:directory) }
  it { should contain_file('/etc/automysqlbackup/automysqlbackup.conf').with_replace(:false) }

end
