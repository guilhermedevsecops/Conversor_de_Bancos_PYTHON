import mysql.connector
import logging


logging.basicConfig(filename='script_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_tables(cursor):
    cursor.execute("SHOW TABLES")
    return [table[0] for table in cursor.fetchall()]


conn_origem = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senha',
    database='banco_origem'
)

conn_destino = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senha',
    database='banco_destino'
)

cursor_origem = conn_origem.cursor()

cursor_destino = conn_destino.cursor()

tabelas_origem = get_tables(cursor_origem)

for tabela in tabelas_origem:
    query_select = f"SELECT * FROM {tabela}"

    cursor_origem.execute(query_select)

    columns = cursor_origem.column_names

    create_table_query = f"CREATE TABLE IF NOT EXISTS {tabela} ("

    for i, column_name in enumerate(columns):
        if i != 0:
            create_table_query += ", "
        create_table_query += f"{column_name} VARCHAR(255)"

    create_table_query += ")"

    cursor_destino.execute(create_table_query)

    logging.info(f"Tabela de destino '{tabela}' criada com sucesso.")

    for registro in cursor_origem:
        query_insert = f"INSERT INTO {tabela} VALUES (" + ", ".join(["%s"] * len(registro)) + ")"
        cursor_destino.execute(query_insert, registro)

        logging.info(f"Registro inserido na tabela '{tabela}': {registro}")

        
conn_destino.commit()

cursor_origem.close()
cursor_destino.close()
conn_origem.close()
conn_destino.close()
