import mysql.connector
import os
from flask import Flask, jsonify

# Retrieve the database host and port from the ConfigMap
database_host = os.environ.get('DATABASE_HOST')
database_port = int(os.environ.get('DATABASE_PORT'))
database_user = os.environ.get('DATABASE_USER')
database_password = os.environ.get('DATABASE_PASSWORD')
database_name = os.environ.get('DATABASE_NAME')

# Create a connection pool
cnxpool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name='my_pool',
    pool_size=5,
    host=database_host,
    port=database_port,
    user=database_user,
    password=database_password,
    database=database_name
)

app = Flask(__name__)

@app.route('/api/records')
def get_records():
    # Acquire a connection from the connection pool
    cnx = cnxpool.get_connection()

    try:
        # Execute a query to fetch records
        cursor = cnx.cursor()
        query = 'SELECT * FROM Employees'
        cursor.execute(query)
        records = cursor.fetchall()

        # Format records into an HTML table
        table_html = '<h2>Employee Records</h2>'
        table_html += '<table>'
        table_html += '<tr><th>ID</th><th>Name</th><th>Age</th></tr>'
        for record in records:
            table_html += '<tr>'
            table_html += f'<td>{record[0]}</td>'
            table_html += f'<td>{record[1]}</td>'
            table_html += f'<td>{record[2]}</td>'
            table_html += '</tr>'
        table_html += '</table>'

        # Return the table HTML as the response
        return table_html

    finally:
        # Release the connection back to the connection pool
        cnx.close()

if __name__ == '__main__':
    # Run the Flask app on port 3010
    app.run(host='0.0.0.0', port=3010)
