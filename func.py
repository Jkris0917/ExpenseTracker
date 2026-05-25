from datetime import datetime
import json

class Expense:
    def __init__(self,category,amount,note=None,expense_id=None,date=None):
        self.id = expense_id
        self.category = category
        self.amount = amount
        self.note = note
        self.date = date or datetime.now().strftime("%d-%m-%Y. %H:%M:%S")
        
    def to_dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "amount": self.amount,
            "note": self.note,
            "date": self.date
        }
    
    def __str__(self):
        return f"[{self.id}] {self.category}: ¥{self.amount} ({self.date})"
    
class ExpenseManager:
    def __init__(self,FILENAME="ExpenseTracker/data.json"):
        self.filename = FILENAME
        self.expenses = []
        self.load()
        
    def _next_id(self):
        return max((e.id for e in self.expenses), default=0) + 1
    
    def add(self,category, amount, note=None):
        expense = Expense(category, amount,note,expense_id=self._next_id())
        self.expenses.append(expense)
        self.save()
        print(f"Added: {expense}")
        
    def delete(self,expense_id):
        original_count = len(self.expenses)
        self.expenses = [e for e in self.expenses if e.id != expense_id]
        if len(self.expenses) < original_count:
            self.save()
            print("Deleted successfully.")
        else:
            print("Expense not found.")
            
    def search(self, keyword):
        keyword = keyword.lower()
        return [e for e in self.expenses
                if keyword in e.category.lower() or (e.note and keyword in e.note.lower())]
        
    def total(self):
        return sum(int(e.amount) for e in self.expenses)
    
    def by_category(self):
        result = {}
        for e in self.expenses:
            result[e.category] = result.get(e.category, 0) + int(e.amount)
        return result
        
    def display_all(self):
        if not self.expenses:
            print(" No expenses.")
            return
        for e in self.expenses:
            print(e)
    
    def save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([e.to_dict() for e in self.expenses], f, ensure_ascii=False, indent= 2)
            
    def load(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.expenses = [
                    Expense(d['category'], d["amount"], d.get("note"), expense_id=d["id"], date=d["date"]) for d in data
                ]
        except FileNotFoundError:
            self.expenses = []
            