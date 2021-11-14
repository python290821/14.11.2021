import shelve

class Person:
    def __init__(self, id, name, mobile, address):
        self.id = id
        self.name = name
        self.mobile = mobile
        self.address = address

    def __repr__(self):
        return f'Person({self.id}, {self.name}, {self.mobile},'+ \
                    f'{self.address})'

    def __str__(self):
        return f'Person id:{self.id}, name:{self.name}, mobile:{self.mobile},'+\
                f' address:{self.address}'

moshe = Person(1, 'Moshe', '050-1234567', 'Tel Aviv')
print(moshe)
dana = Person(2, 'Dana', '050-7654321', 'Hertezlliya')
print(dana)

# persistence
sh = shelve.open('customers.db')
sh['moshe'] = 1
sh.close()
