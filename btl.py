import json

class Student:
    def __init__(self, id, name, age, phone, target_level, current_level, language, score):
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.target_level = target_level
        self.current_level = current_level
        self.language = language
        self.score = score

    def __str__(self):
        return f"{self.id} - {self.name} ({self.language}) - Hiện tại: {self.current_level}, Mục tiêu: {self.target_level}, Điểm: {self.score}"

    def update_score(self, new_score):
        self.score = new_score

    def has_reached_target(self):
        return self.score >= self.target_level


class ManageStudent:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.id != student_id]

    def find_student(self, name):
        return [s for s in self.students if name.lower() in s.name.lower()]

    def list_students(self):
        for s in self.students:
            print(s)

    def list_achievers(self):
        return [s for s in self.students if s.has_reached_target()]

    def sort_by_score(self):
        self.students.sort(key=lambda s: s.score, reverse=True)

    def save_to_file(self, filename="students.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([s.__dict__ for s in self.students], file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename="students.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.students = [Student(**s) for s in data]
        except FileNotFoundError:
            print("Không tìm thấy file dữ liệu. Bắt đầu với danh sách trống.")


def main():
    manager = ManageStudent()
    manager.load_from_file()
    
    while True:
        print("\nChọn chức năng:")
        print("1. Thêm người học")
        print("2. Xóa người học")
        print("3. Tìm kiếm người học")
        print("4. Hiển thị danh sách người học")
        print("5. Hiển thị người đã đạt mục tiêu")
        print("6. Sắp xếp theo điểm")
        print("7. Lưu dữ liệu")
        print("8. Thoát")

        choice = input("Nhập lựa chọn: ")
        
        if choice == "1":
            id = input("Nhập ID: ")
            name = input("Nhập tên: ")
            age = int(input("Nhập tuổi: "))
            phone = input("Nhập số điện thoại: ")
            language = input("Nhập ngôn ngữ học (English/Japanese/Korean): ")
            current_level = input("Nhập trình độ hiện tại: ")
            target_level = input("Nhập trình độ mục tiêu: ")
            score = float(input("Nhập điểm hiện tại: "))
            student = Student(id, name, age, phone, target_level, current_level, language, score)
            manager.add_student(student)
            print("✔ Người học đã được thêm!")
        
        elif choice == "2":
            student_id = input("Nhập ID người học cần xóa: ")
            manager.remove_student(student_id)
            print("✔ Người học đã được xóa!")
        
        elif choice == "3":
            name = input("Nhập tên người học cần tìm: ")
            results = manager.find_student(name)
            if results:
                for s in results:
                    print(s)
            else:
                print("Không tìm thấy!")
        
        elif choice == "4":
            print("\nDanh sách người học:")
            manager.list_students()
        
        elif choice == "5":
            print("\nDanh sách người học đạt mục tiêu:")
            for s in manager.list_achievers():
                print(s)
        
        elif choice == "6":
            manager.sort_by_score()
            print("✔ Danh sách đã được sắp xếp theo điểm!")
        
        elif choice == "7":
            manager.save_to_file()
            print("✔ Dữ liệu đã được lưu!")
        
        elif choice == "8":
            print("Thoát chương trình.")
            break
        
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
