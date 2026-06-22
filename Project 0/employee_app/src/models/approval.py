from enums.status_enum import Status
from datetime import datetime

class Approval:
    id : int
    expense_id : int
    status : Status
    reviewer : int | None
    comment : str | None
    review_date : datetime | None
    
    def __init__(self, id : int, expense_id : int, status : Status, reviewer : int = None, comment : str = None, review_date : datetime = None):
        self.id = id
        self.expense_id = expense_id
        self.reviewer = reviewer
        self.comment = comment
        self.review_date = review_date
    
    @classmethod
    def from_date_iso_8601_str(cls, id : int, expense_id : int, status : Status, reviewer : int = None, comment : str = None, review_date : str = None):
        if review_date != None:
            review_date = datetime.fromisoformat(review_date)
            
        return cls(id, expense_id, status, reviewer, comment, review_date)