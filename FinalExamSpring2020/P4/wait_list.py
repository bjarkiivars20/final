
class Student:
    def __init__(self, id, name, phone, address):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address

    def __lt__(self, other):
        return self.name < other.name
    
    def __str__(self):
        return str(self.id) + " " + str(self.name) + " " + str(self.phone) + " " + str(self.address)


class FunCourse:
    def __init__(self, max_participants):
        self.max_participants = max_participants
        self.amount_of_students = 0
        self.student_list = []
        self.wait_list = []
        
        
    def add_student(self, student:Student):
        if self.amount_of_students < self.max_participants:
            self.student_list.append(student)
            self.amount_of_students += 1
            self.student_list.sort()
        else:
            self.wait_list.append(student)
    
    def get_participant_string(self):
        ret_str = ""
        for student in self.student_list:
            ret_str += str(student) + "\n"
        ret_str = ret_str.rstrip("\n")
        return ret_str

    def get_wait_list_string(self):
        ret_str = ""
        for student in self.wait_list:
            ret_str = str(student) + "\n"
        ret_str = ret_str.rstrip("\n")
        return ret_str


    def _remove_student_helper(self, id):
        index_count = 0
        for student in self.student_list:
            if student.id == id:
                self.student_list.pop(index_count)
                return True
            index_count += 1
        return False

    def remove_student(self, id):
        student_removed = self._remove_student_helper(id)
        if student_removed:
            self.add_student(self.wait_list[0])
            pass
        

if __name__ == "__main__":
    course = FunCourse(3)
    course.add_student(Student(123, "Kári Halldórsson", "1234567", "Heimahagar 57"))
    course.add_student(Student(176, "Guðni Magnússon", "87685", "Heimahlíð 2"))
    course.add_student(Student(654, "Jón Jónsson", "54321", "Heimaholt 54"))
    course.add_student(Student(12, "Holgeir Friðgeirsson", "2354456567", "Heimateigur 65"))
    course.add_student(Student(32, "Geir Friðriksson", "99875", "Heimageisli 12"))

    print()
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    rem_id = 654
    print("\nremoving participant with id: " + str(rem_id) + "\n")
    course.remove_student(rem_id)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    rem_id = 176
    print("\nremoving participant with id: " + str(rem_id) + "\n")
    course.remove_student(rem_id)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    rem_id = 12
    print("\nremoving participant with id: " + str(rem_id) + "\n")
    course.remove_student(rem_id)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())