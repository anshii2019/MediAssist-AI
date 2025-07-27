import psycopg2
from rich.console import Console
from rich.table import Table

DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",  # <-- put your real password here
    "host": "localhost",
    "port": "5432"
}

def print_all_users():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("SELECT id, name, symptoms, location, diagnosis, user_id FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    console = Console()

    if not rows:
        console.print("[bold red]📭 No users found in the database.[/]")
        return

    table = Table(title="📋 Users Table", show_lines=True)

    table.add_column("ID", justify="right")
    table.add_column("Name", style="cyan")
    table.add_column("Symptoms", style="magenta")
    table.add_column("Location", style="green")
    table.add_column("Diagnosis", style="yellow")
    table.add_column("UserID", style="white")

    for row in rows:
        id_, name, symptoms, location, diagnosis, user_id = row
        table.add_row(
            str(id_),
            name or "",
            (symptoms or "")[:30],
            location or "",
            (diagnosis or "")[:30],
            user_id or ""
        )

    console.print(table)

if __name__ == "__main__":
    print_all_users()
