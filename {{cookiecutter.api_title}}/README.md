## {{cookiecutter.api_title}} API

{{cookiecutter.api_description}}


## Install requirements

```bash
sudo apt update
sudo apt install python3 python3-pip nodejs -y
sudo npm install -g pm2
```


## Deploy application

Application can be launched with the launch script:
```bash
sudo bash launch.sh
```
Or using PM2:
```bash
sudo pm2 start pm2.json
```
Note: if the script `launch.sh` doesn't works, you can use `launch2.sh` instead.


## Run application

For running directly the application in a "raw" way:
```bash
sudo python3 -m pip install pip --upgrade
sudo python3 -m pip install . --upgrade
sudo {{cookiecutter.package_name}}
```


## Disclaimer

API developed by {{cookiecutter.author}} (@{{cookiecutter.author_github}} on GitHub) on {% now 'local', '%Y' %} for {{cookiecutter.organization}}.
For manteinance and bug reports please contact the developer at {{cookiecutter.email}}.
Copyright {{cookiecutter.organization}} {% now 'local', '%Y' %}. All rights reserved. See license for details.