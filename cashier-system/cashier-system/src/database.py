import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection to the MySQL database."""
    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='responsi_5230411130'
        )
        if conn.is_connected():
            print("Connected to MySQL database")
        return conn
    except Error as e:
        print(f"Error: {e}")
    return conn

def create_tables():
    """Create tables for products and transactions if they do not exist."""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS produk (
                    id_produk INT AUTO_INCREMENT PRIMARY KEY,
                    nama_produk VARCHAR(255) NOT NULL,
                    harga DECIMAL(10, 2) NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transaksi (
                    id_transaksi INT AUTO_INCREMENT PRIMARY KEY,
                    id_produk VARCHAR(255) NOT NULL,
                    jumlah INT NOT NULL,
                    total_harga DECIMAL(10, 2) NOT NULL,
                    tanggal transaksi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            print("Tables checked/created successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()