import sqlite3
import bcrypt
from models.user import User

class LoginService:
    db_con : sqlite3.Connection
    
    def __init__(self, db_con : sqlite3.Connection):
        self.db_con = db_con
    
    def attempt_login(self, username : str, password : str):
        db_cur = self.db_con.cursor()
        db_cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        
        raw_usr_data = db_cur.fetchone()
        psw_bytes = password.encode('utf-8')
        
        if bcrypt.checkpw(psw_bytes, raw_usr_data[2]):
            return User.from_str_role(raw_usr_data[0], raw_usr_data[1], raw_usr_data[3])
        else:
            return None
        
        