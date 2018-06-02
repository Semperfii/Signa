#!/usr/bin/env bash

cd back/
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cp config/dev.json config/config.json
cd ../front
npm install
