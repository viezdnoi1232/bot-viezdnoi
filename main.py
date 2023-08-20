import mysql.connector

from mysql.connector import Error


def part_definition(text):

    def create_connection(host_name, user_name, user_password, db_name):
        connection = None

        try:
            connection= mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            #print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e} occurred")

        return connection


    def execute_ready_query(connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}'occurred")


    connection=create_connection("localhost", "root", "PASSWORD", "phone")
    detal = f"SELECT * FROM price_list_phone WHERE model_phone LIKE '%{text}%' LIMIT 3;"
    do = execute_ready_query(connection, detal)

    return do