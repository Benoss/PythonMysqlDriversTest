from time import time
import sys
import platform

use_mysqldb = True
try:
    import MySQLdb
except ImportError:
    use_mysqldb = False
 
use_mysql_connector = True 
try:  
    import mysql.connector
    from mysql.connector import version
except ImportError:
    use_mysql_connector = False
    
use_oursql = True 
try:  
    import oursql
except ImportError:
    use_oursql = False

use_pymysql = True 
try:  
    import pymysql
except ImportError:
    use_pymysql = False


print "- Compare python mysql drivers, don't forget to run it twice in order to warmup your db -"
print "*Python version: {} ".format(sys.version)
print "*Platform: {} ".format(platform.platform())
print "*Database: https://launchpad.net/test-db 1.0.6"
if use_mysqldb:
    print "*MySQLdb version: {} url:{}".format(MySQLdb.__version__, "https://github.com/farcepest/MySQLdb1")

if use_mysql_connector:
    print "*mysql.connector version: {} url:{}".format(".".join(str(x) for x in version.VERSION[:3]), "http://dev.mysql.com/downloads/connector/python/")
    
if use_oursql:
    print "*oursql version: {} url:{}".format(oursql.__version__, "https://launchpad.net/oursql")
    
if use_pymysql:
    print "*pymysql version: {} url:{}".format(pymysql.__version__, "https://github.com/petehunt/PyMySQL")


    
def conn(lib):
        return lib.connect(host="localhost", user="root", passwd="", db="employees")
 
def simpleSelect(steps, conn, formater='%s'):
        q = "Select SQL_NO_CACHE  * from employees where emp_no = {}".format(formater)
        start = time()
        for a in range(1,steps):
            cursor = conn.cursor()
            cursor.execute(q, [1001])
            result = cursor.fetchone()
            cursor.close()
        t= time()-start
        conn.close()
        return t
  
def select500(steps, conn, formater='%s'):
        steps = steps/10 
        q = "Select SQL_NO_CACHE * from employees limit 500".format(formater)
        start = time()
        for a in range(1,steps):
            cursor = conn.cursor()
            cursor.execute(q)
            rows = cursor.fetchall()
            for row in rows:
                b = row[0]
            cursor.close()
        t= time()-start
        conn.close()
        return t
  
def select500with500Args(steps, conn, formater='%s'):
        steps = steps/10 
        argsVals = range(1001, 1500)
        q = "Select SQL_NO_CACHE * from employees where emp_no in ({})".format(",".join([formater for x in argsVals]))
        start = time()
        for a in range(1,steps):
            cursor = conn.cursor()
            cursor.execute(q, argsVals)
            rows = cursor.fetchall()
            for row in rows:
                b = row[0]
            cursor.rowcount
            cursor.close()
        t= time()-start
        conn.close()
        return t
  
def select300kID(steps, conn, formater='%s'):
        steps = 5 
        q = "Select SQL_NO_CACHE emp_no from employees".format(formater)
        start = time()
        for a in range(1,steps):
            cursor = conn.cursor()
            cursor.execute(q)
            rows = cursor.fetchall()
            for row in rows:
                b = row[0]
            cursor.close()
        
        t= time()-start
        conn.close()
        return t
  
def select1M(steps, conn, formater='%s'):
        steps = 5 
        q = "Select SQL_NO_CACHE salary from salaries".format(formater)
        start = time()
        for a in range(1,steps):
            cursor = conn.cursor()
            cursor.execute(q)
            rows = cursor.fetchall()
            for row in rows:
                b = row[0]
            cursor.close()
        
        t= time()-start
        conn.close()
        return t
  
  
steps = 10000




print "-- Simple Select 1 record {}x --".format(steps)
if use_mysqldb:
    print simpleSelect(steps, conn(MySQLdb)), 'MySQLdb' 
if use_oursql:
    print simpleSelect(steps, conn(oursql), '?'), 'oursql'
if use_mysql_connector:
    print simpleSelect(steps, conn(mysql.connector)), 'mysql.connector'
if use_pymysql:
    print simpleSelect(steps, conn(pymysql)), 'pymysql'
print "-- Select 500 rows {}x--".format(steps/10)
if use_mysqldb:
    print select500(steps, conn(MySQLdb)), 'MySQLdb'
if use_oursql:
    print select500(steps, conn(oursql), '?'), 'oursql'
if use_mysql_connector:
    print select500(steps, conn(mysql.connector)), 'mysql.connector'
if use_pymysql:
    print select500(steps, conn(pymysql)), 'pymysql'
print "-- Select 500 rows with 500 args {}x--".format(steps/10)
if use_mysqldb:
    print select500with500Args(steps, conn(MySQLdb)), 'MySQLdb'
if use_oursql:
    print select500with500Args(steps, conn(oursql), '?'), 'oursql'
if use_mysql_connector:
    print select500with500Args(steps, conn(mysql.connector)), 'mysql.connector'
if use_pymysql:
    print select500with500Args(steps, conn(pymysql)), 'pymysql'
print "-- Select 300k id  {}x--".format(steps/2000)
if use_mysqldb:
    print select300kID(steps, conn(MySQLdb)), 'MySQLdb'
if use_oursql:
    print select300kID(steps, conn(oursql), '?'), 'oursql'
if use_mysql_connector:
    print select300kID(steps, conn(mysql.connector)), 'mysql.connector'
if use_pymysql:
    print select300kID(steps, conn(pymysql)), 'pymysql'
print "-- Simple Select 1M3 id  {}x--".format(steps/10000)
if use_mysqldb:
    print select1M(steps, conn(MySQLdb)), 'MySQLdb'
if use_oursql:
    print select1M(steps, conn(oursql), '?'), 'oursql'
if use_mysql_connector:
    print select1M(steps, conn(mysql.connector)), 'mysql.connector'
if use_pymysql:
    print select1M(steps, conn(pymysql)), 'pymysql'