from database import Database
from teacherCRUD import TeacherCRUD

db = Database("bolt://35.174.155.82:7687", "neo4j", "mates-tablets-blanks")

teacher_db = TeacherCRUD(db)

teacher_db.create_teacher("Chris Lima", 1956, "189.052.396-66")
print(teacher_db.read_teacher("Chris Lima"))
teacher_db.update_teacher("Chris Lima", "162.052.777-77")

db.close()
