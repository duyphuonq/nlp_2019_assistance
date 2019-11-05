#!/usr/bin/env bash
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev
virtualenv venv
source env/bin/activate
pip install -r requirements.txt