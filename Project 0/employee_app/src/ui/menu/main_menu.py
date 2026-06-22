from ui.menu.menu import Menu
from ui.helper.menu_helper import MenuHelper
from models.user import User
from ui.menu.pending_submission_menu import PendingSubmissionMenu

class MainMenu(Menu):
    mh : MenuHelper
    user : User
    window_opened = False
    
    def __init__(self, user : User):
        self.mh = MenuHelper()
        self.user = user
    
    def open(self):
        self.window_opened = True
        
        while(self.window_opened):
            self.mh.display_header_2_with_menu("Main Menu", f"Hello, {self.user.username}!")
            self.mh.display_numbered_list(["Submit Expense", "View Expense History", "Open Pending Submission Menu", "Exit"])
            selection = input()
            
            match selection:
                case "1":
                    self._submit_expense()
                case "2":
                    self._view_expense_history()
                case "3":
                    self._open_pending_submission_menu()
                case "4":
                    self._exit()
                case _:
                    print("Unknown command.")
    
    
    def _submit_expense(self):
        pass
    
    def _view_expense_history(self):
        pass
    
    def _open_pending_submission_menu(self):
        psm = PendingSubmissionMenu(self.user)
        psm.open()
    
    
    def _exit(self):
        self.window_opened = False