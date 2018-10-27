sudo docker run --name mysql -e MYSQL_USER=sqluser -e MYSQL_PASSWORD=123456 -e MYSQL_DATABASE=greetingsdb -p 3306:3306 -d mysql/mysql-server:5.7
mysql --protocol=TCP -u sqluser -p123456
