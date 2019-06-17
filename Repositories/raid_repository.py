import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
#

import sys
sys.path.insert(0, '/Projects/raid_tracker/src/Models')
from raid import Raid

class RaidRepository:
    def GetAllRaids():
        try:
            connection = mysql.connector.connect(host='localhost',
                                     database='raids',
                                     user='root',
                                     password='Empire12')


            sql_select_query = 'select * from raid'
            cursor = connection.cursor()
            cursor.execute(sql_select_query)


            records = cursor.fetchall()
            print("Total number of rows in python_developers is - ", cursor.rowcount)
            print ("Printing each row's column values i.e.  developer record")
            for row in records:
                raid_new = Raid(row[1], row[2], row[3], row[4], row[0])
                print("Id = ", raid_new.id)
                print("Name = ", raid_new.name)
                print("IsActive = ", raid_new.is_active)
                print("Priority = ", raid_new.priority)
                print("ChatLinkUrl = ", raid_new.chat_link_url)
                cursor.close()


        except mysql.connector.Error as error :
            connection.rollback() #rollback if any exception occured
            print("Failed to select all from raid table {}".format(error))
        finally:
            #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")



    def CreateRaid(raid):
        try:
            connection = mysql.connector.connect(host='localhost',
                                     database='raids',
                                     user='root',
                                     password='Empire12')
            sql_insert_query = f" INSERT INTO raid (Name, IsActive, Priority, ChatLinkUrl) VALUES ('{raid.name}', {raid.is_active}, {raid.priority}, '{raid.chat_link_url}')"
            print(sql_insert_query)
            cursor = connection.cursor()
            result  = cursor.execute(sql_insert_query)
            connection.commit()
            raid.id = cursor.lastrowid
            print ("Record inserted successfully into raid table")
        except mysql.connector.Error as error :
            connection.rollback() #rollback if any exception occured
            print("Failed inserting record into raid table {}".format(error))
        finally:
            #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
