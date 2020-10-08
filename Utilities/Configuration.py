import configparser
from mysql.connector import Error

import mysql.connector


def getConfig():
    config = configparser.RawConfigParser(allow_no_value=True)

    config.read('D:\\PYTHON\\API_Testing\\Config\\properties.ini')

    return config


sql_config = {'user': getConfig()['SQL']['user'],
              'password': getConfig()['SQL']['password'],
              'host': getConfig()['SQL']['host'],
              'database': getConfig()['SQL']['database']

              }


def getSQLConnection():
    try:

        conn = mysql.connector.connect(**sql_config)

        if conn.is_connected():
            print('Connection successful')

            return conn

    except Error as e:

        print(e)


def getQuery(query):

    conn = getSQLConnection()

    cursor = conn.cursor()

    cursor.execute(query)

    row = cursor.fetchone()

    conn.close()

    return row
