#!/bin/bash
sudo apt-get update
sudo apt install python-django-common
sudo systemctl start google-startup-scripts.service

sudo apt install python3-pil
sudo pip3 install requests
sudo apt install stress

sudo chmod +x ~/download_drive_file.sh
./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
tar xf ~/supplier-data.tar.gz

touch changeImage.py
touch supplier_image_upload.py
touch run.py
touch reports.py
touch emails.py
touch report_email.py
touch health_check.py

sudo chmod +x ~/*.py