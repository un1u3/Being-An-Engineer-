class Employee:
     
     num_of_emps = 0
     raise_amt = 1.04 
     
     
     def __init__(self,first, last, pay):
          self.first = first 
          self.last = last 
          self.pay = pay 
          
          Employee.num_of_emps +=1 
          
     def fullName(self):
          return '{} {}'.format(self.first,self.last)
     
     def apply_raise(self):
          self.pay = int(self.pay * self.raise_amt)
          
          def set_raise_amt(cls, amount):
               pass 
          
emp1= Employee('Uniqe')
              