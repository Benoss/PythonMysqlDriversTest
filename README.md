PythonMysqlDriversTest
======================

Python Mysql Drivers Benchmark


- Compare python mysql drivers -
*Python version: 2.7.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)] 
*Platform: Windows-7-6.1.7601-SP1 
*Database: https://launchpad.net/test-db 1.0.6
*MySQLdb version: 1.2.3 url:https://github.com/farcepest/MySQLdb1
*mysql.connector version: 1.0.10 url:http://dev.mysql.com/downloads/connector/python/
*oursql version: 0.9.3.1 url:https://launchpad.net/oursql
*pymysql version: 0.5.None url:https://github.com/petehunt/PyMySQL
-- Simple Select 1 record 10000x --
1.33500003815 MySQLdb
2.92000007629 oursql
4.75300002098 mysql.connector
6.37299990654 pymysql
-- Select 500 rows 1000x--
5.27799987793 MySQLdb
4.88400006294 oursql
35.1779999733 mysql.connector
45.4629998207 pymysql
-- Select 500 rows with 500 args 1000x--
2.97600007057 MySQLdb
3.20799994469 oursql
4.76099991798 mysql.connector
4.15899991989 pymysql
-- Select 300k id  5x--
1.84399986267 MySQLdb
1.62400007248 oursql
24.6400001049 mysql.connector
35.6339998245 pymysql
-- Simple Select 1M3 id  1x--
16.1340000629 MySQLdb
70.8839998245 oursql
247.088000059 mysql.connector
339.72300005 pymysql
