Facter.add("location") do
  setcode do
    if Facter.value(:fqdn) =~ /#{Facter.value(:hostname)}\.a/
      "a"
    elsif Facter.value(:fqdn) =~ /#{Facter.value(:hostname)}\.b/
      "b"
    end
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
