from database.database import init_db
from ui.menu.login_menu import LoginMenu

from repositories.expense_repository import ExpenseRepository

if __name__ == "__main__":
    #init_db()
    
    #lm = LoginMenu()
    #lm.open()

    er = ExpenseRepository()
    print(er.get_expenses_from_user_id(1)[0])