import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="knowledge_db"
)

cursor = db.cursor()