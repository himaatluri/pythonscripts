#!/bin/sh

printf "[INFO]  Installing virtualenv python package.. make sure python version is 3 and up..\n"
pip3 install virtualenv

printf "\n[INFO] Enabling virtual env...."
virtualenv pythonscripts

printf "\n[INFO] Activating virtual env...."
source pythonscripts/bin/activate

printf "\n[INFO] Installing requirements...."
pythonscripts/bin/pip install -r requirements.txt

printf "\n[INFO] env is setup...."