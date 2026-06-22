from ui.menu.menu import Menu
from ui.helper.menu_helper import MenuHelper
from models.user import User

class PendingSubmissionMenu(Menu):
    mh : MenuHelper
    user : User
    window_opened = False
    
    def __init__(self, user : User):
        self.mh = MenuHelper()
        self.user = user
    
    def open(self):
        self.window_opened = True
        
        while(self.window_opened):
            self.mh.display_header_2_with_menu("Pending Submission Menu", f"Make your selection.")
            self.mh.display_numbered_list(["View Pending Submissions", "Edit Pending Submission", "Delete Pending Submission", "Exit"])
            selection = input()
            
            match selection:
                case "1":
                    self._view_pending_submissions()
                case "2":
                    self._edit_pending_submission()
                case "3":
                    self._delete_pending_submission()
                case "4":
                    self._exit()
                case _:
                    print("Unknown command.")
    
    
    def _view_pending_submissions(self):
        pass
    
    def _edit_pending_submission(self):
        pass
    
    def _delete_pending_submission(self):
        pass
    
    
    def _exit(self):
        self.window_opened = False