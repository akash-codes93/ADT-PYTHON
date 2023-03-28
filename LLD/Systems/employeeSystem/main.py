
class Employee:
    ID = 1

    def __init__(self, name, manager):
        self.id = self._get_unique_id()
        self.name = name
        self.manager = manager

    def _get_unique_id(self):
        _id = Employee.ID
        Employee.ID += 1
        return _id

    def get_details(self):
        return f"Employee Id: {self.id} Name: {self.name}"


class System:

    def __init__(self):
        self.__employees = []

    def add_employee(self, employee):
        self.__employees.append(employee)

    def create_employee(self, name, manager):
        emp = Employee(name, manager)
        self.__employees.append(emp)
        return emp

    def find_employee_details(self, id=None, name=None):

        if id:
            for emp in self.__employees:
                if emp.id == id:
                    return emp.get_details()
        elif name:
            for emp in self.__employees:
                if emp.name == name:
                    return emp.get_details()

        return None

    def list_employee_subordinates(self, manager):
        sub_ordinates = []

        def print_subordinates():
            for i in sub_ordinates:
                print(i)

        for emp in self.__employees:
            if emp.manager == manager:
                sub_ordinates.append(emp.get_details())

        print_subordinates()

    def search_employee_subordinates(self, name):

        for emp in self.__employees:
            if name in emp.name:
                return emp.get_details()


system = System()

system.create_employee("emp1", "akash")
system.create_employee("emp2", "akash")
system.create_employee("emp3", "akash")
system.create_employee("emp4", "akash")

print(system.find_employee_details(1))

system.list_employee_subordinates("akash")
print("----")

print(system.search_employee_subordinates("emp"))

