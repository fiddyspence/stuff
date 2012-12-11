%define puppet_version 2.7.0
%define os_dist el
%define os_version 5
%define arch i386
%define release 1

Summary: Integralis installer for Puppet Enterprise Agent
Name: integralis-puppet-agent-installer
Version: %{puppet_version}
Release: %{release}
Group: System/Tools
License: Restricted
URL: http://puppetlabs.com
Source: puppet-enterprise-%{puppet_version}-%{os_dist}-%{os_version}-%{arch}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description

Integralis installer for Puppet Enterprise Agent


%prep
%{__rm} -rf %{buildroot}

%setup  -n puppet-enterprise-%{puppet_version}-%{os_dist}-%{os_version}-%{arch}

%install

mkdir -p %{buildroot}/opt/puppet
mkdir %{buildroot}/opt/puppet/.install
cp -r * %{buildroot}/opt/puppet/.install

%files
/opt/puppet

%post

if [ $PUPPETSERVER ]; then
  export PUPPETSERVER_REAL=$PUPPETSERVER
elif [ $(hostname -f | grep dev) ]; then
  export PUPPETSERVER_REAL=pe-puppet.a.dev.mss.ai.pri
elif [ $(hostname -f | grep prod) ]; then
  export PUPPETSERVER_REAL=pe-devpuppet.a.prod.mss.ai.pri
fi

cd /opt/puppet/.install

cat <<EOF > answers.txt
q_fail_on_unsuccessful_master_lookup=y
q_install=y
q_puppet_cloud_install=n
q_puppet_enterpriseconsole_install=n
q_puppet_symlinks_install=y
q_puppetagent_certname=`hostname -f`
q_puppetagent_install=y
q_puppetagent_server=$PUPPETSERVER_REAL
q_puppetca_install=n
q_puppetmaster_install=n
q_vendor_packages_install=y
q_verify_packages=y
EOF

./puppet-enterprise-installer -a answers.txt &

%clean

%{__rm} -rf %{buildroot}
