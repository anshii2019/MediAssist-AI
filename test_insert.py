import psycopg2
from db_utils import DB_PARAMS

def test_insert():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (name, symptoms, location, diagnosis, user_id)
        VALUES (%s, %s, %s, %s, %s)
    """, ("TestName", "test symptoms", "test city", "test diagnosis", "testid123"))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Inserted test user into database.")

if __name__ == "__main__":
    test_insert()
