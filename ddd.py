class Canvas:
    degree_completion = 4
    def __init__(self, level, credit, loan_dept):
        self.level = level
        self.credit = credit
        self.loan_dept = loan_dept

    def first_method(self, credit):
        self.credit += credit

    def second_method(self, loan_amount):
        self.loan_dept += loan_amount

    def third_method(self, eligible):
        if eligible:
            return self.loan_dept - 100
        else:
            return self.loan_dept

    def fourth_method(self, year_passed):
        return Canvas.degree_completion - year_passed

    def fifth(self, level):
        self.level = level

    def sixth_method(self):
        return self.level

    def seventh(self):
        return self.credit


sam = Canvas("freshman", 12, 1000)
susan = Canvas("sophomore", 31, 1200)
james = Canvas("junior", 66, 1800)
julie = Canvas("junior", 66, 1800)

julie.first_method(12)
susan.second_method(1000)
james.fifth("senior")
sam.first_method(9)
sam.second_method(100)


print(julie.sixth_method())
print()
print(sam.seventh())
print()
print(sam.fifth("sophomore"))
print()
print(susan.third_method(True))
print()
print(james.fourth_method(2))
print()
print(sam.third_method(False))
print()
# print(julie.first_method(18)
# julie
# )
print()
print(susan.seventh())
print()
print(sam.sixth_method())
print()
print(Canvas)