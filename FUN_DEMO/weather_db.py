#! /bin/python
# Name:        weather_db.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This module defines a Weather class for storing data
# in a sqlite3 database.
"""
    This module describes a Class of Weather objects which can create/drop tables
    and insert/delete rows in a weather database.
"""

import sys
import sqlite3
import pprint

class Weather_db:
    # Class variable storing location of DB
    # Could store this in an external file or environment variable.
    DB_LOC = "C:\labs\weather_db.sqlite"

    def __init__(self):
        try:
            self.__db_conn = sqlite3.connect(Weather_db.DB_LOC)
            self.cur = self.__db_conn.cursor()
        except Exception as err:
            raise ValueError
        # No return as not explicitly called.


    def create_table(self, table_name="weather"):
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}
                    ( id        INTEGER PRIMARY KEY
                    ,city       VARCHAR(30)                  
                    ,country    VARCHAR(30)
                    ,date       DATE DEFAULT CURRENT_DATE 
                    ,description VARCHAR(50)
                    ,temp       FLOAT
                    ,humidity   FLOAT
                    ,wind_speed FLOAT
                    ,wind_direction VARCHAR(2)
                    ) """)
        return None

    def drop_table(self, table_name="weather"):
        """ Drop table if exists """
        option = input(f"Are you sure you want to drop {table_name} (y/n)? ")
        if option.lower() == "y":
            self.cur.execute(f"""DROP TABLE IF EXISTS {table_name}""")
        return None

    def query_all(self, table_name="weather"):
        """ Query and return all rows in formatted str output """
        sql = f"SELECT * FROM {table_name}"
        try:
            self.cur.execute(sql)
            rows = self.cur.fetchall()
            for row in rows:
                print(row)
        except Exception as err:
            print(f"Error accessing {table_name}: [{err}]\n", file=sys.stderr)

        return None

    def insert_row(self, table_name="weather", **kwargs):
        """ Insert new row into weather db table """
        weather = {'id': None, 'city': None, 'country': None,
                   'date': 'DEFAULT', 'description': 'N/A', 'temp': None,
                   'humidity': None, 'wind_speed': None, 'wind_direction': None}
        weather.update(kwargs)
        pprint.pprint(weather)
        sql = f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

        try:
            self.cur.execute(sql, (weather['id'], weather['city'], weather['country'],
                                   weather['date'], weather['description'], weather['temp'],
                                   weather['humidity'], weather['wind_speed'], weather['wind_direction'] ))
        except Exception as err:
            print(f"Cannot insert row, {err}", file=sys.stderr)

        return None

    def delete_row(self, row_id, table_name="weather"):
        """ Delete new row into weather db table """
        try:
            sql = f"DELETE FROM {table_name} WHERE id={row_id}"
            self.cur.execute(sql)
        except Exception as err:
            print(f"Error accessing {table_name}: [{err}]\n", file=sys.stderr)
        return None

    def delete_all_rows(self, table_name="weather"):
        """ Delete all rows in the the table."""
        try:
            sql = f"DELETE FROM {table_name}"
            self.cur.execute(sql)
        except Exception as err:
            print(f"Error accessing {table_name}: [{err}]\n", file=sys.stderr)
        return None

    def commit(self):
        """ Commit changes to database """
        self.__db_conn.commit()
        return None

    def close(self):
        self.__db_conn.close()
        return None

    # Example of operator overloading.
    def __str__(self):
        """ Return status of DB connection a str """
        if self.__db_conn:
            return f"DB still connected"
        else:
            return f"DB not connected"

    def __del__(self):
        """ Close connection automatically when object is deleted """
        self.__db_conn.close()
        return None