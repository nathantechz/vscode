import mysql.connector

# Connect to MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Salus2016$",
    database="BLOOOMVALUE"
)

# Check if connection is successful
if connection.is_connected():
    print("Connected to MySQL server")


import csv
# Perform data manipulation operations here

# Function to insert data from CSV into MySQL table
def insert_data_from_csv(connection, csv_file, table_name):
    cursor = connection.cursor()
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row if it exists
        for row in csv_reader:
            # Construct the SQL INSERT statement
            sql = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(row))})"
            cursor.execute(sql, row)
    connection.commit()
    cursor.close()

# Main function
def main():
  
        # Path to your CSV file
        csv_file = '/Users/naganathan/Library/CloudStorage/Dropbox/Data_Science/VSCODE/vscode/BloomValue/healthcare_dataset.csv'

        # Name of the MySQL table to insert data into
        table_name = 'patient_records'

        # Insert data from CSV into MySQL table
        insert_data_from_csv(connection, csv_file, table_name)


if __name__ == "__main__":
    main()

# Close connection
connection.close()
