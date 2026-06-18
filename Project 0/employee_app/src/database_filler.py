from database.database import get_connection
import bcrypt

def fill_database():
    db_con = get_connection()
    db_cur = db_con.cursor()
    
    usr = "codykrause"
    psw = "123"
    psw_bytes = psw.encode('utf-8')
    salt = bcrypt.gensalt()
    psw_hash = bcrypt.hashpw(psw_bytes, salt)
    
    db_cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (usr, psw_hash, "EMPLOYEE"))
    db_con.commit()
    
    db_con.close()
    print("Database filled.")
    

if __name__ == "__main__":
    fill_database()