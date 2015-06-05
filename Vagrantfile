# -*- mode: ruby -*-
# vi: set ft=ruby :

env_name = "buildersrecords-env"

Vagrant.configure(2) do |config|
    config.vm.hostname = env_name

    config.vm.box = "ubuntu/trusty64"

    config.vm.provider :virtualbox do |v|
        v.name = env_name
    end

    config.vm.provision :shell, path: "vagrant/update.sh"
    config.vm.provision :shell, path: "vagrant/postgres.sh"
    config.vm.provision :shell, path: "vagrant/python.sh"
    config.vm.provision :shell, path: "vagrant/heroku.sh"
    config.vm.provision :shell, path: "vagrant/aws.sh"

    config.vm.network :forwarded_port, guest: 5432, host: 5432
    config.vm.network :forwarded_port, guest: 5555, host: 5555
end
