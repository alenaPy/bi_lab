"""File with completed task 2 from labwork4.

The task is to create class. In my case it`ll be class Hospital.
"""


class Hospital(object):
    """Hospital class describe full information about visitors."""

    def __init__(self, first_name, last_name, age, sex):
        """Object initialization."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.hospital_department = []
        self.doctor = []
        self.diagnosis = []
        self.total_price = 0
        self.visits = 0

    def add_hospital_department(self, department_name):
        """Add information about visitors` hospital departments."""
        self.hospital_department.append(department_name)
        self.visits += 1

    def add_diagnosis(self, diagnosis):
        """Add visitors` diagnosis."""
        self.diagnosis.append(diagnosis)

    def add_doctor(self, doc_last_name, price):
        """Add visitors` doctors and calculate total price."""
        self.doctor.append(doc_last_name)
        self.total_price += price

    def display_visitor(self):
        """Print information about visitor."""
        print("First name: %s " % self.first_name)
        print("Last name: %s " % self.last_name)
        print("Age: %d " % self.age)
        print("Sex: %s \n" % self.sex)
        print("Number of visits: %d" % self.visits)
        print("Total price of all visits: %d \n" % self.total_price)
        print("Visited departments:")
        for i in self.hospital_department:
            print(str(i) + ", ")
        print("\nVisited doctors:")
        for i in self.doctor:
            print(str(i) + ", ")
        print("\nDiagnosis:")
        for i in self.diagnosis:
            print(str(i) + ", ")


v1 = Hospital("Nataliya", "Blashuk", 21, "f")
v1.add_hospital_department("therapeutic")
v1.add_hospital_department("otolaryngology")
v1.add_diagnosis("flue")
v1.add_diagnosis("genyantritis")
v1.add_doctor("Sharko", 250)
v1.add_doctor("Lampov", 145)
v1.display_visitor()
