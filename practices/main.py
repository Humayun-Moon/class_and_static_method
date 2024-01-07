import os
import csv
class Person :
    all_items = []
    def __init__(self,name,id,month, salary):
        self.name = name
        self.id = id
        self.month = month
        self.salary = salary
        Person.all_items.append(self)
    def info(self):
        print(f"Person name is {self.name} and id number {self.id} salary of {self.month} is : {self.salary} TK")    
    def get_salary (self):
        return self.salary
    def get_overtime (self,ot,ot_rate ):
        total_ot = ot * ot_rate
        return total_ot 
    def total_salary (self,get_salary,get_overtime):
        get_total_salary = get_salary + get_overtime
        return get_total_salary 
    @classmethod    
    def imoprt_from_csv(cls):
        script_path = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_path, 'persons.csv')

        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        created_items = []
        for item in items:
            
            name = item.get('name')
            id_str = item.get('id')
            month= item.get('month')
            salary_str = item.get('salary')
             
            if name is not None and id_str is not None and month is not None and salary_str is not None:
                try:
                    id =int(id_str)
                    month =str(month)
                    salary = float(salary_str)

                    created_item= Person(
                        name= name,
                        id = id,
                        month = month,
                        salary = salary
                    )
                    created_items.append(created_item)
                except ValueError as e :
                    print(f"Error creating items{name}: {e} ")    
        return created_items        



    def __repr__(self):
        return f"Person({self.name}, {self.id}, {self.month}, {self.salary})"
creted_item = Person.imoprt_from_csv()
print(creted_item)
# p1 = Person("Humayun", 902868, "December", 13550)
# p1.info()
# salary = p1.get_salary()
# overtime = p1.get_overtime(16, 71.15)    
# print(f"Total overtime value is : {overtime}") 
# total_salary = p1.total_salary(salary, overtime)
# print(f"The total salay of {p1.month} of {p1.name} is : {total_salary}") 
# print()

# p2 = Person("Khusbu", 902870, "November", 18900)
# p2.info()
# salary = p2.get_salary()
# overtime = p2.get_overtime(16, 99.99)    
# print(f"Total overtime value is : {overtime}") 
# total_salary = p2.total_salary(salary, overtime)
# print(f"The total salay of {p2.month} of {p2.name} is : {total_salary}") 
# print()

# p3 = Person("Moon", 902845, "June", 23989)
# p3.info()
# salary = p3.get_salary()
# overtime = p3.get_overtime(30, 87.15)    
# print(f"Total overtime value is : {overtime}") 
# total_salary = p3.total_salary(salary, overtime)
# print(f"The total salay of {p3.month} of {p3.name} is : {total_salary}") 



# get_all_items = Person.all_items
# print(get_all_items)
    
    
