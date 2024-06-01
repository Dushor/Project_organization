class Department:
    def speak(self):
        pass


class Staff:
    @staticmethod
    def bark():
        print("Hi, my name is Maxim, I am 25 years old and I am a programmer from the 195 department")


# Adapter
class StaffAdapter(Department):
    def __init__(self, staff):
        self.staff = staff

    def speak(self):
        self.staff.bark()


# Client
def main():
    staff = Staff()
    staff_adapter = StaffAdapter(staff)
    staff_adapter.speak()


if __name__ == "__main__":
    main()
