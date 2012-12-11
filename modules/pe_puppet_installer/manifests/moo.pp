    service { 'pe-puppet':
            enable                    => false,
                  ensure              => stopped,
                        hasstatus     => false,
                              pattern => "/opt/puppet/bin/puppet agent",
                                  } 
