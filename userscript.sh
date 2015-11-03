#!/usr/bin/env bash
# Userscript for DigitalOcean VPS setup.

SSH_CRED_GZ_URL

sudo adduser easyctf
sudo apt-get install git
curl ${SSH_CRED_GZ_URL} > /tmp/sshcreds.gz
#untar
#clone
#deps.sh
#useradd user
echo 'easyctf ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/99-easyctf