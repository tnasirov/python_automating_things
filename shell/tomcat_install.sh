#!/bin/bash
echo "Downloading Tomcat"
sleep 3
wget https://apache.mirrors.tworzy.net/tomcat/tomcat-9/v9.0.43/bin/apache-tomcat-9.0.43.tar.gz
echo "Unzipping"
sleep 3
tar -xzvf apache-tomcat-9.0.43.tar.gz
rm -rf apache-tomcat-9.0.43.tar.gz
mv apache-tomcat-9.0.43/ tomcat9