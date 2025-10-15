import tkinter as tk
from tkinter import messagebox
import mysql.connector
import logging

# Configuração de logs
logging.basicConfig(
    filename='script_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def migrar():
    host_origem = entry_host_origem.get()
    port_origem = int(entry_port_origem.get())
    banco_origem = entry_db_origem.get()
    host_destino = entry_host_destino.get()
    port_destino = int(entry_port_destino.get())
    banco_destino = entry_db_destino.get()
    user = entry_user.get()
    senha = entry_senha.get()

    try:
        conn_origem = mysql.connector.connect(
            host=host_origem,
            port=port_origem,
            user=user,
            password=senha,
            database=banco_origem
        )
        cursor_origem = conn_origem.cursor()

        conn_destino = mysql.connector.connect(
            host=host_destino,
            port=port_destino,
            user=user,
            password=senha,
            database=banco_destino
        )
        cursor_destino = conn_destino.cursor()

        cursor_origem.execute("SHOW TABLES")
        tabelas = [t[0] for t in cursor_origem.fetchall()]

        for tabela in tabelas:
            cursor_origem.execute(f"SELECT * FROM `{tabela}`")
            registros = cursor_origem.fetchall()
            colunas = cursor_origem.column_names

            if not registros:
                logging.info(f"Nenhum dado na tabela '{tabela}', pulando...")
                continue

            # Cria tabela se não existir
            cursor_destino.execute(f"SHOW TABLES LIKE '{tabela}'")
            if cursor_destino.fetchone() is None:
                cursor_origem.execute(f"SHOW CREATE TABLE `{tabela}`")
                create_sql = cursor_origem.fetchone()[1]
                cursor_destino.execute(create_sql)
                logging.info(f"Tabela '{tabela}' criada no destino.")

            # Ignorar coluna 'id' se existir e for auto_increment
            colunas_sem_id = [c for c in colunas if c.lower() != 'id']
            placeholders = ", ".join(["%s"] * len(colunas_sem_id))
            insert_sql = f"INSERT INTO `{tabela}` ({', '.join(colunas_sem_id)}) VALUES ({placeholders})"
            registros_sem_id = [
                [row[colunas.index(c)] for c in colunas_sem_id]
                for row in registros
            ]

            cursor_destino.executemany(insert_sql, registros_sem_id)
            conn_destino.commit()
            logging.info(f"{len(registros_sem_id)} registros inseridos em '{tabela}'.")

        cursor_origem.close()
        cursor_destino.close()
        conn_origem.close()
        conn_destino.close()
        messagebox.showinfo("Sucesso", "Migração concluída!")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Falha na migração: {err}")
        logging.error(f"Erro na migração: {err}")

# ----------------- Interface Tkinter -----------------
root = tk.Tk()
root.title("Migrador MySQL")
root.geometry("400x720")
root.configure(bg="#2c3e50")

label_font = ("Arial", 11, "bold")
entry_font = ("Arial", 11)

frame = tk.Frame(root, bg="#34495e", padx=20, pady=20)
frame.pack(padx=20, pady=20, fill="both", expand=True)

def cria_campo(texto, valor_padrao="", show=None):
    label = tk.Label(frame, text=texto, font=label_font, bg="#34495e", fg="white")
    label.pack(anchor="w", pady=(5,0))
    entry = tk.Entry(frame, font=entry_font, show=show)
    entry.pack(fill="x", pady=(0,5))
    entry.insert(0, valor_padrao)
    return entry

tk.Label(frame, text="--- Banco Origem ---", font=("Arial", 12, "bold"), bg="#34495e", fg="#1abc9c").pack(pady=(0,10))
entry_host_origem = cria_campo("Host:", "127.0.0.1")
entry_port_origem = cria_campo("Porta:", "3307")
entry_db_origem = cria_campo("Banco:", "banco_origem")

tk.Label(frame, text="--- Banco Destino ---", font=("Arial", 12, "bold"), bg="#34495e", fg="#e67e22").pack(pady=(10,10))
entry_host_destino = cria_campo("Host:", "127.0.0.1")
entry_port_destino = cria_campo("Porta:", "3308")
entry_db_destino = cria_campo("Banco:", "banco_destino")

tk.Label(frame, text="--- Credenciais ---", font=("Arial", 12, "bold"), bg="#34495e", fg="#9b59b6").pack(pady=(10,10))
entry_user = cria_campo("Usuário:", "root")
entry_senha = cria_campo("Senha:", "senha", show="*")

btn_migrar = tk.Button(frame, text="Migrar", font=("Arial", 12, "bold"), bg="#1abc9c", fg="white", command=migrar)
btn_migrar.pack(pady=20, fill="x")

root.mainloop()
