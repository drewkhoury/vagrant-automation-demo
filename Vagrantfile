# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define "autodemodrew" do |autodemodrew|

    autodemodrew.vm.box = "hashicorp/precise64"

    autodemodrew.vm.provision :ansible do |ansible|
      ansible.playbook = "playbook.yml"
      ansible.verbose  = true
    end

  end

end
