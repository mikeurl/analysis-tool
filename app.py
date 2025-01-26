import gradio as gr
import sqlite3

def query_database(query):
    # Connect to the SQLite database
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def main():
    # Create a Gradio interface
    iface = gr.Interface(
        fn=query_database,
        inputs="text",
        outputs="text",
        title="SQLite Query Interface",
        description="Enter your SQL query to interact with the SQLite database."
    )
    iface.launch()

if __name__ == "__main__":
    main()
