import platform
import subprocess
import psycopg2

operating_system = platform.system()

if operating_system == "Linux":
    commands = [
        "sudo apt-get update",
        "sudo apt-get install postgresql postgresql-contrib -y",
        "sudo -u postgres psql -c \"CREATE DATABASE mydatabase\"",
        "sudo -u postgres psql -c \"CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword'\"",
        "sudo -u postgres psql -c \"GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser\"",
    ]
    
elif operating_system == "Windows":
    commands = [
        "choco install postgresql",
        "psql -U postgres -c \"CREATE DATABASE mydatabase\"",
        "psql -U postgres -c \"CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword'\"",
        "psql -U postgres -c \"GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser\"",
    ]
    
elif operating_system == "Darwin":
    commands = [
        "brew update",
        "brew install postgresql",
        "pg_ctl -D /usr/local/var/postgres start",
        "createuser -s myuser",
        "createdb mydatabase",
    ]
    
else:
    print("This Operating System not supported.")

for command in commands:
    subprocess.run(command, shell=True)

conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

with conn.cursor() as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS mytable (id serial PRIMARY KEY, column_name text)")
    conn.commit()
    
    column_name = "new_column"
    column_definition = "'text'"
    
    query = f"ALTER TABLE mytable ADD COLUMN IF NOT EXISTS {column_name} {column_definition}"
    cursor.execute(query)
    conn.commit()
    
print("Database and table created successfully!")
