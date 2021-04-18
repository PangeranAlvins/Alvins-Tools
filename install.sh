#!/bin/bash
pkg install git php openssh python3 python -y
pip install -r requirements.txt
pip install bs4 requests mechanize
pip2 install -r requirements.txt
pip2 install bs4 requests mechanize
git clone https://github.com/PangeranAlvins/Alvins-Tools
cd Alvins-Tools
python3 Alvins-Tools.py
exit 0
