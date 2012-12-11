Facter.add("location") do
  setcode do
     Facter::Util::Resolution.exec("cat /etc/location")
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
