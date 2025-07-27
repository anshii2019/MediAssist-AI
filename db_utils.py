import psycopg2

# Adjust these credentials
DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

def create_table():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            symptoms TEXT,
            location TEXT,
            diagnosis TEXT,
            user_id VARCHAR(20) UNIQUE
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Table ensured.")

def save_user(name, symptoms, location, diagnosis, user_id):
    print(f"--> Going to insert: {name}, {symptoms}, {location}, {diagnosis}, {user_id}")
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (name, symptoms, location, diagnosis, user_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, symptoms, location, diagnosis, user_id))
    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ User {name} saved.")
   

def get_user(user_id):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

def update_user(user_id, symptoms, location, diagnosis):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("""
        UPDATE users
        SET symptoms = %s, location = %s, diagnosis = %s
        WHERE user_id = %s
    """, (symptoms, location, diagnosis, user_id))
    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ User {user_id} updated.")
