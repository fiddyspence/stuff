Facter.add("location") do
  hostname = Facter(:fqdn).split('.')
  setcode do
    hostname[1] if hostname[1] =~ /^(a|b)$/
  end
end
Facter.add("environment") do
#  Facter.value(:hostname)
  setcode do
     if Facter.value(:hostname) =~ /dev/
       "dev"
     else
       "production"
     end
  end
end
