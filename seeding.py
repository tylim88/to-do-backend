from src.models.toDoList import ToDoTable
from src import db

# delete all row
ToDoTable.query.delete()

test1 = ToDoTable("meow", "meow@gmail.com", "secret123",'{"todo":[{"text":"1","done":false},{"text":"10","done":true},{"text":"jgj","done":true},{"text":"hhh","done":false}],"filter":"Active","stat":[4,2,2]}')
test2 = ToDoTable("woof", "woof@gmail.com", "longpass")
test3 = ToDoTable("roar", "roar@gmail.com", "secret123")

db.session.add_all([test1,test2,test3])
db.session.commit()

print(ToDoTable.query.all())
