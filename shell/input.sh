#!/bin/bash
read -p "Enter your service name: " service
status=$(systemctl status $service | awk 'NR==3{print $2}')
echo -e "The current status of your $service is: \033[31m$status\033[0m"