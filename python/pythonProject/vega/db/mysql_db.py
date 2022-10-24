# coding:utf-8

import mysql.connector.pooling

# 創立為私有變量, 使參數僅能被此對象調用
# 在mySQL8.0預設caching_sha2_password加密，但套件不支援，所以必須加上一行把預設加密改為mysql_native_password
__config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'tony1120',
    'database': 'vega',
    'auth_plugin': 'mysql_native_password'
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=10
    )
except Exception as e:
    print(e)