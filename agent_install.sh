#!/bin/bash
echo "Updating..."
sudo apt -y update
sudo apt -y upgrade
echo "Installing snort..."
sudo apt -y install snort
echo "Install complete."
echo "Finding configuration file..."
snortConf=$(sudo find / -type f -name 'snort.conf' 2>/dev/null)
echo "$snortConf"

if [ -n '$snortConf' ]; then
	echo "Config file found."
	echo "Testing snort."
	sudo snort -T -i enp0s3 -c $snortConf
else
	echo "No config file found. Create a config file to test snort"
fi

echo "Starting snort service..."

sudo snort -d -i enp0s3 -A unsock
#start snort service here
