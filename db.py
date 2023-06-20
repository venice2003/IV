from typing import List, Optional,Union
import warnings
import mysql
import mysql.connector
from texts import mainWindowTexts, emergencyScreenTexts,medicHistoryTexts
columns = [*mainWindowTexts,*emergencyScreenTexts,*medicHistoryTexts]
"""
    Class responsible for database connection, disconnection and returning data from the database
"""

class db:
    def __init__(self):
        warnings.warn("Database  class initiated, call the connect() function to use.")
        pass
    
    def connect(self,host:str, username:str,password:str,databaseName :str):
        """
        connects to the database

        Args:
            host (str):host
            username (str): username
            password (str): password
            databaseName (str): name of the database
        Raises:
            Exception: if there is double calls, or connection error
        """        
        try:
            if(hasattr(self,"db")):     
                raise Exception("Database connected twice check for double calls")
            self.db = mysql.connector.connect(host=host, user=username, password=password, database=databaseName)
            print("Database connected")
        except mysql.connector.Error as error:
            # An error occurred during the connection attempt
            print(f"Error connecting to the database: {error}")
        except Exception as error :
            print(f"Error connecting to the database: {error}")  
    def create(self, column_names: List[str], data: List[str],tableName:str):
        """
        adds data to the table
        Args:
            column_names (List[str]): The names of the columns you wish to add data.
            data (List[str]): The data  that would be added to the column.
            tableName (str):  table name of where to save the data.

        Raises:
            Exception: errors on query or connections

        Returns:
            boolean: if the operation is succesfull
        """
        if len(column_names) != len(data):
            warnings.warn("Column names and data provided do not match")
        if not hasattr(self, "db"):
            raise Exception("No connected database. Use connect() first before doing operations")
        try:
            print(data)
            cursor = self.db.cursor()
            placeholders = ', '.join(['%s'] * len(data))  # Generate placeholders for the values
            query = f"INSERT INTO {tableName} ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, data)  
            self.db.commit()
            cursor.close()
            print("Data added to the database")
            return True
        except mysql.connector.Error as error:
            print(f"Error adding data to the database: {error}")
            return False
    def read(self,tableName:str, column_names: Union[str, List[str]] = "*",condition: Optional[str] = None, extraQuery: Optional[str] = None ):
        """
        reads rows in the database
        Args:
            tableName (str): tablename
            column_names (Union[str, List[str]], optional): columns you want to read. Defaults to "*".
            condition (Optional[str], optional): extra sql query to add. Defaults to None.

        Raises:
            Exception: When  ther's an error reading the data base or connection problem

        Returns:
            data: an array or group of data.
        """        
        if not hasattr(self, "db"):
            raise Exception("No connected database. Use connect() first before doing operations")
        try:
            cursor = self.db.cursor()
            if isinstance(column_names, str) and column_names == "*":
                select_list = "*"
            else:
                select_list = ", ".join(column_names)
            query = f"SELECT {select_list} FROM {tableName}"
            if condition is not None:
                query += f" WHERE {condition}"
            if extraQuery is not None:
                query += f" {extraQuery}"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except mysql.connector.Error as error:
            print(f"Error reading data from the database: {error}")
            return []
    def update(self, table_name: str, column_values: dict, condition: Optional[str] = None):
        """
        Updates the columns in the database

        Args:
            table_name (str): Name of the table you want to edit
            column_values (dict): the column name with it's values example :  {"NAME": "John","AGE": 35,"CITY": "New York"}
            condition (Optional[str], optional): Extra conditions to further be specific. Defaults to None.

        Returns:
            affected_rows: number of data affected by the update
        """        
        if not hasattr(self, "db"):
            raise Exception("No connected database. Use connect() first before doing operations")
        try:
            cursor = self.db.cursor()
            set_values = ", ".join([f"{column} = %s" for column in column_values.keys()])
            query = f"UPDATE {table_name} SET {set_values}"
            
            if condition is not None:
                query += f" WHERE {condition}"
            cursor.execute(query, list(column_values.values()))
            self.db.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"Updated {affected_rows} rows  of data successfully")
            return affected_rows
        except mysql.connector.Error as error:
            print(f"Error updating data in the database: {error}")
            return 0
    def delete(self, args):
        # since ako mostly gumawa nito, ikaw na mag tapos ng delete. kaya niyo na yan
        #remove pass when you finished your  code
        pass
    def createDatabase(self,host:str, username:str,password:str):
        
        if( hasattr(self,"db")):     
            raise Exception("Database connected twice check for double calls")
        self.db = mysql.connector.connect(host=host, user=username, password=password)
        cursor =self.db.cursor()
        cursor.execute(f"DROP DATABASE IF EXISTS medicalForms")
        cursor.execute(f"CREATE DATABASE medicalForms")
        cursor.close()
        self.db.close()
        print("Database created successfully")
        self.db = mysql.connector.connect(host=host, user=username, password=password, database="medicalForms")
        cursor = self.db.cursor()

        # Join the column definitions into a comma-separated string with proper formatting
        columns_str = ', '.join([f'{column} VARCHAR(64)' for column in columns])

        # Create the CREATE TABLE query
        query = f"CREATE TABLE formData ({columns_str})"

        # Execute the CREATE TABLE query
        cursor.execute(query)
        print("Table created successfully")
       # have this always at the last part of the code
        cursor.close()
        self.db.close()
        del self.db 
        # this is just to make your life easier na kahit saang pc ka pumunta, 
        # i c call mo na lang tong function na to para ma create yung database automatically, 
        # if gusto mo i complete ko to, libre mo ko ;p
        pass
    def close(self):
        """closes the database connection
        """        
        self.db.close()
        del self.db

        return