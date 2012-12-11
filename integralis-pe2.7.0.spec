Summary: An RPM to install pe-puppet and provide a default config
Name: integralis-pe-2.7.0
Version: 2.7.0
Release: 1
License: GPL
BuildArch: x86_64
Group: System Environment/Base
BuildRoot: /usr/src/redhat/SOURCES/%{name}-%{buildarch}-buildroot

%description
An RPM to provide the deps for installing the pe-puppet agent

%prep
exit 0

%build
exit 0

%install
exit 0

%clean
exit 0

%files
%defattr(-,root,root,-)
%dir /%{_destdir}
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/answers.txt
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/gpg
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/gpg/RPM-GPG-KEY-puppetlabs
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/puppet-enterprise-upgrader
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/supported_platforms
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/send_cert_request.rb.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/autosign.conf.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/database.yml.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/settings.yml.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/puppet.conf.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/console_auth_config.yml.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/puppetdashboard.conf.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/console_auth_db_config.yml.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/site.pp.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/puppetmaster.conf.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/receive_signed_cert.rb.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/databases.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/cas_client_config.yml.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/external_node.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/rubycas_config_upgrade_comments.txt
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/auth.conf.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/rubycas_config.yml.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/erb/config.ru.erb
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-mime-types-1.16-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-augeas-libs-0.10.0-3.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-fog-1.5.0-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-sinatra-1.2.6-0.2.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-ruby-devel-1.8.7.370-1.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-virtual-java-1.0-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-httpd-2.2.3-19.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-virtual-mysql-1.0-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-activemq-5.6.0-2.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-hiera-puppet-0.3.0-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-mod_ssl-2.2.3-19.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-console-auth-1.1.15-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-libevent-devel-2.0.13-3.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-builder-3.0.0-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-puppet-enterprise-release-2.7.0-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-ruby-mysql-2.7.3-7.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-stomp-doc-1.1.9-3.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-puppet-2.7.19-6.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-net-ssh-2.1.4-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-rack-1.1.3-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-libevent-2.0.13-3.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-live-management-1.1.22-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-certificates-0.1.0-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-httpd-devel-2.2.3-19.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-activesupport-2.3.14-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-puppet-server-2.7.19-6.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-stomp-1.1.9-3.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-guid-0.1.1-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-ruby-1.8.7.370-1.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-tanukiwrapper-3.5.9-5.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-ruby-hmac-0.4.0-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-cloud-provisioner-1.0.5-1.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-console-test-0.2.5-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-puppet-dashboard-baseline-2.0.6-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-ar-extensions-0.9.5-2.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-facter-1.6.10-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-net-scp-1.0.4-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-multi-json-1.0.3-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-certificate-manager-test-0.2.6-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-memcached-devel-1.4.7-2.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-certificate-manager-0.2.6-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-memcached-1.4.7-2.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-rake-0.8.7-3.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-console-0.2.5-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-ruby-shadow-1.4.1-8.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-mcollective-1.2.1-13.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-ruby-ldap-0.9.8-5.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-augeas-devel-0.10.0-3.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-hiera-0.3.0-333.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-httpd-passenger-2.2.11-15.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-ruby-irb-1.8.7.370-1.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-puppet-dashboard-1.2.10-13.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-activerecord-2.3.14-2.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-nokogiri-1.5.0-3.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-augeas-0.10.0-3.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-ruby-rdoc-1.8.7.370-1.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-ruby-ri-1.8.7.370-1.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-mcollective-common-1.2.1-13.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-excon-0.14.1-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-mcollective-client-1.2.1-13.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-tilt-1.3.3-0.2.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygems-1.5.3-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-ruby-libs-1.8.7.370-1.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-dalli-1.1.2-0.1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-trollop-1.16.2-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-ruby-augeas-0.4.1-1.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-json-1.7.5-1.pe.el5.x86_64.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-formatador-0.2.0-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64/pe-rubygem-rbvmomi-1.3.0-1.pe.el5.noarch.rpm
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/packages/el-5-x86_64-package-versions.yaml
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/LICENSE.txt
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/puppet-enterprise-installer
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/README.markdown
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/puppet-enterprise-uninstaller
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/util
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/util/pe-man
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/puppetlabs-stdlib-2.5.1.tar.gz
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/puppetlabs-auth_conf-0.0.5.tar.gz
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/puppetlabs-pe_mcollective-0.0.57.tar.gz
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/puppetlabs-mcollectivepe-0.0.2.tar.gz
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/ripienaar-concat-0.2.0.tar.gz
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/install_modules.txt
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/wrapper_modules.txt
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/puppetlabs-accounts-0.0.2.tar.gz
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/puppetlabs-baselines-0.0.4.tar.gz
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/puppetlabs-pe_compliance-0.0.8.tar.gz
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/upgrade_modules.txt
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/puppetlabs-request_manager-0.0.5.tar.gz
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/modules/puppetlabs-pe_accounts-1.1.0.tar.gz
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/support
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/answers
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/answers/upgrade_with_cloud.answer.sample
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/answers/full_suite_existing_remote_mysql.sample
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/answers/agent_with_cloud.answer.sample
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/answers/full_suite.answer.sample
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/answers/master_only.answer.sample
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/answers/upgrade_without_cloud.answer.sample
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/answers/console_only.answer.sample
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/answers/full_suite_existing_mysql.sample
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/answers/agent_no_cloud.answer.sample
/%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/VERSION

%post
%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/puppet-enterprise-installer -a /%{_destdir}/puppet-enterprise-2.7.0-el-5-x86_64/answers.txt
