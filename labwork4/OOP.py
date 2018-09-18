"""This is simulation of Student payment system in Univesity."""


class Student(object):

    def __init__(self, first, last, card, amount, discount=1):
        """student with default discount=1"""
        self.first = first
        self.last = last
        self.card = card
        self.email = first + '_' + last + '@epam.com'
        self.payment_state = 'Not paid'
        self.amount = amount
        self.discount = discount

    def print_student(self):
        """Prints all information about the student"""
        print(' First name: {} \n Last name: {} \n ID_card: {} \n Email: {} '
              '\n Payment state: {} \n Amount: {} \n '
              'Discount: {}'.format(self.first, self.last, self.card,
                                    self.email, self.payment_state,
                                    self.amount, self.discount))

    def fullname(self):
        """Create full name from two words"""
        return '{} {}'.format(self.first, self.last)

    def student_paid(self):
        """Changes the payment state from Not Paid on Paid"""
        self.payment_state = 'Paid'
        return self

    def set_discount(self, discount):
        """Set discount for the amount of the student"""
        self.discount = discount
        self.amount = self.amount * (100 - discount) / 100
        return self


stud_1 = Student('Veranika', 'Simanenka', 126483, 1500)
stud_2 = Student('Karina', 'Ivanova', 3847283, 1700)
stud_3 = Student('Mikita', 'Petrou', 385683, 3000, 50)


stud_1.print_student()
stud_1.student_paid()
print('-------------------------')
stud_1.print_student()

print('-------------------------')
print('Fullname of student 2 is: {}'.format(stud_2.fullname()))


# Setting discount for stud_1:
stud_1.set_discount(20)
stud_1.print_student()

# stud_2 without discount:
stud_2.print_student()
stud_2.set_discount(int(input('Enter the discount for this student in %: ')))
# stud_2 with discount:
stud_2.print_student()

stud_3.print_student()
