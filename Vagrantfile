# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
    env_name = "buildersrecords-env"

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

    config.vm.provision :shell do |sh|
        sh.inline = <<-EOF
            cd ../../
            mkdir uploads
            chmod 777 uploads
        EOF
    end

    config.vm.network :forwarded_port, guest: 5432, host: 5432
    config.vm.network :forwarded_port, guest: 5555, host: 5555
end
