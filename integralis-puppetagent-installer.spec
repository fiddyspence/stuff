%define puppet_version 2.7.0
%define os_dist el
%define os_version 5
%define arch x86_64
%define release 1

Summary: Integralis installer for Puppet Enterprise Agent
Name: wp-puppet-agent-installer
Version: %{puppet_version}
Release: %{release}
Group: System/Tools
License: Restricted
URL: http://puppetlabs.com
Source: puppet-enterprise-%{puppet_version}-%{os_dist}-%{os_version}-%{arch}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description

WorldPay installer for Puppet Enterprise Agent


%setup -q -n puppet-enterprise-%{puppet_version}-%{os_dist}-%{os_version}-%{arch}

%install

mkdir -p %{buildroot}/opt/puppet

%files
/opt/puppet

%post

cat <<EOF > answers.txt
q_fail_on_unsuccessful_master_lookup=y
q_install=y
q_puppet_cloud_install=n
q_puppet_enterpriseconsole_install=n
q_puppet_symlinks_install=y
q_puppetagent_certname=`hostname -f`
q_puppetagent_install=y
q_puppetagent_server=puppet
q_puppetca_install=n
q_puppetmaster_install=n
q_vendor_packages_install=y
q_verify_packages=y
EOF

./puppet-enterprise-installer -a answers.txt
