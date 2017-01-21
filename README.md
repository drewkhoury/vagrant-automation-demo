# vagrant-automation-demo

This demo uses `vagrant` to run `ansible` which creates an `nginx` reverse proxy, that forwards traffic to the `python` web/app server, with a `postgres` backend.

If everything goes to plan you should see the app on `http://localhost:8080/` in your browser after you `vagrant up`.

## Example output
Example output when running `vagrant up`:

```
$ vagrant up
Bringing machine 'autodemodrew' up with 'virtualbox' provider...
==> autodemodrew: Importing base box 'hashicorp/precise64'...
...
==> autodemodrew: Mounting shared folders...
    autodemodrew: /vagrant => /Users/andrewkhoury/repos/vagrant-automation-demo
==> autodemodrew: Running provisioner: file...
==> autodemodrew: Running provisioner: file...
==> autodemodrew: Running provisioner: file...
==> autodemodrew: Running provisioner: ansible...

PLAY [Hello World] ************************************************************ 

GATHERING FACTS *************************************************************** 
ok: [autodemodrew]

TASK: [Installs nginx web server] ********************************************* 
changed: [autodemodrew]

TASK: [Move default nginx configs sites-available] **************************** 
changed: [autodemodrew]

TASK: [Move default nginx configs sites-enabled] ****************************** 
changed: [autodemodrew]

TASK: [Move our config file into place] *************************************** 
changed: [autodemodrew]

TASK: [Installs python and pip] *********************************************** 
changed: [autodemodrew] => (item=python,python-pip)

TASK: [Install tornado - python web server] *********************************** 
changed: [autodemodrew]

TASK: [start tornado] ********************************************************* 
changed: [autodemodrew]

TASK: [Install Postgresql] **************************************************** 
changed: [autodemodrew] => (item=postgresql,postgresql-contrib,python-psycopg2)

TASK: [Lets create a db] ****************************************************** 
changed: [autodemodrew]

TASK: [Create a table] ******************************************************** 
changed: [autodemodrew]

TASK: [I guess we should put some data in it] ********************************* 
changed: [autodemodrew]

TASK: [Lets see whats in the table] ******************************************* 
changed: [autodemodrew]

NOTIFIED: [start nginx] ******************************************************* 
changed: [autodemodrew]

PLAY RECAP ******************************************************************** 
autodemodrew               : ok=14   changed=13   unreachable=0    failed=0  
```
