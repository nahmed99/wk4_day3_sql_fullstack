# BEFORE RUNNING THIS PROGRAM, MAKE SURE THAT YOU HAVE CREATED THE REQUIRED DATABASE (using: createdb database_name):
# createdb music_library

# CREATE THE TABLES (using: psql -d database_name -f filename.sql):
# psql -d music_library -f db/music_library.sql
#
# Then run this file as a normal python program...
#
#
# Any issues, then you could type in the following commands (in terminal):
# psql  (to launch psql terminal)
# \c database_name  (to connect to the db)
# select * from table;  (or any other sql commands...)
#




import pdb
from models.task import Task
from models.user import User

import repositories.task_repository as task_repository
import repositories.user_repository as user_repository

task_repository.delete_all()
user_repository.delete_all()

user1 = User("Jack", "Jarvis")
user_repository.save(user1)
user2 = User("Victor", "McDade")
user_repository.save(user2)

user_repository.select_all()

task_1 = Task("Plant seeds", user1, 30)
task_repository.save(task_1)

task_2 = Task("Go for a run", user1, 30, True)
task_repository.save(task_2)


pdb.set_trace()
