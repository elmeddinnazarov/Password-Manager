import platform
import subprocess
import psycopg2

operating_system = platform.system()

db_name = input("Enter the Database name: ")
db_username = input("Enter the username: ")
db_password = input("Enter the password: ")

if operating_system == "Linux":
    commands = [
        "sudo apt-get update",
        f"sudo apt-get install postgresql postgresql-contrib -y",
        f"sudo -u postgres psql -c \"CREATE DATABASE {db_name}\"",
        f"sudo -u postgres psql -c \"CREATE USER {db_username} WITH ENCRYPTED PASSWORD {db_password}\"",
        f"sudo -u postgres psql -c \"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO{db_username}\"",
    ]
    
elif operating_system == "Windows":
    commands = [
        "choco install postgresql",
        f"psql -U postgres -c \"CREATE DATABASE {db_name}\"",
        f"psql -U postgres -c \"CREATE USER {db_username} WITH ENCRYPTED PASSWORD {db_password}\"",
        f"psql -U postgres -c \"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_username}\"",
    ]
    
elif operating_system == "Darwin":
    commands = [
        "brew update",
        "brew install postgresql",
        "pg_ctl -D /usr/local/var/postgres start",
        f"createuser -s {db_username}",
        f"createdb {db_name}",
    ]
    
else:
    print("This Operating System not supported.")

for command in commands:
    subprocess.run(command, shell=True)

conn = psycopg2.connect(
    host="localhost",
    database=f"{db_name}",
    user=f"{db_username}",
    password=f"{db_password}"
)


with conn.cursor() as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, first_name VARCHAR(500) NOT NULL, last_name VARCHAR(500) NOT NULL, email VARCHAR(500) NOT NULL, password VARCHAR(500) NOT NULL, key VARCHAR(500) NOT NULL, phone VARCHAR(500) NOT NULL)")
    conn.commit()
    
    # column_name = "new_column"
    # column_definition = "'text'"
    
    # query = f"ALTER TABLE mytable ADD COLUMN IF NOT EXISTS {column_name} {column_definition}"
    # cursor.execute(query)
    # conn.commit()
    
print("Database and table created successfully!")
