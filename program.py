import shelve

class Person:
    def __init__(self, id=0, name='', mobile='', address=''):
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

#moshe = Person(1, 'Moshe', '050-1234567', 'Tel Aviv')
#print(moshe)
#dana = Person(2, 'Dana', '050-7654321', 'Hertezlliya')
#print(dana)

# persistence
sh = shelve.open('customers.db')
# longer
#sh['moshe'] = moshe.__dict__
moshe_from_db_dict = sh['moshe'] # dictionary
moshe_object1 = Person()
moshe_object1.id = moshe_from_db_dict['id']
moshe_object1.name = moshe_from_db_dict['name']
moshe_object1.mobile = moshe_from_db_dict['mobile']
moshe_object1.address = moshe_from_db_dict['address']

# quicker
print(moshe_object1)
moshe_object2 = Person()
moshe_object2.__dict__ = moshe_from_db_dict
print(moshe_object2)
#sh['1'] = (1,2) # can also save tuple
#sh['top ten'] = [('danny', 230), ('rani', 1000)]
#top_ten = sh['top ten']
print(sh['1'])
sh.close()