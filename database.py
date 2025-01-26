import sqlite3

def create_table():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, info TEXT)''')
    conn.commit()
    conn.close()

def insert_data(info):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO data (info) VALUES (?)', (info,))
    conn.commit()
    conn.close()

def get_data():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Example usage
if __name__ == "__main__":
    create_table()
    insert_data('Sample data')
    data = get_data()
    for row in data:
        print(row)
