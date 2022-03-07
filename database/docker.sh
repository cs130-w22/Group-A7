#!/bin/bash
docker run -it -v ${pwd}:/home/cs143/shared -p 8888:80 --name mysql-130 junghoo/mysql-apache
cd shared
echo "password" | sudo mysql class_db < maketables.sql


