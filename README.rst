Dependencies
------------

Installing virtualbox and vagrant::

    sudo apt-get install ruby rubygems virtualbox nfs-common nfs-kernel-server  
    sudo gem install vagrant

Usage
-----

Go to your git repo.

Run vagrant to start a devel vm and get into it using ssh::

    vagrant up
    vagrant ssh


Create an virtualenv::

    virtualenv venv


Activate the environment::

    . venv/bin/activate
    cd /vagrant/


Install development packages::

    cd www/
    sudo pip install -r requirements.txt
