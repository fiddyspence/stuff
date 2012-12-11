class soe {

  #include pe_puppet_installer
  class { 'pe_puppet_installer':
    #    cron   => hiera('pe_puppet_installer::cron',true),
    cron   => false,
    daemon => true,
  }



}
