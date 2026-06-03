from TestCase import TestCase

class TestSuite:
    """A collection of test cases.

    Instance Attributes:
        name (str): Suite name
        tests (list): List of TestCase objects

    Methods:
        add_test(test): Add a TestCase
        remove_test(name): Remove by name
        get_by_priority(priority): Return tests matching the priority
        count(): Return number of tests
    """
    def __init__(self, name : str, tests : list[TestCase]):
        self.name = name
        self.tests = tests
    
    def add_test(self, test : TestCase):
        self.tests.append(test)
    
    def remove_test(self, name : str):
        for i, test in enumerate(self.tests):
            if test.name == name:
                self.tests.remove(test)
                return
    
    def get_by_priority(self, priority : str):
        priority_list = []
        
        for test in self.tests:
            if test.priority == priority:
                priority_list.append(test)
        
        return priority_list
    
    def count(self):
        return len(self.tests)