from TestCase import TestCase
from TestSuite import TestSuite
from TestRunner import TestRunner


def main():
    test_login = TestCase("test_login", "check if login works", "high", ["user"])
    test_logout = TestCase("test_logout", "check if logout works", "medium", ["user"])
    test_submit_form = TestCase("test_Submit Form", "check if submit form works", "high", ["form"])
    test_change_directory = TestCase("Testchange_directory", "check if user can change directory", "low", ["directory"])
    test_access_form = TestCase.from_dict({"name" : "test_access_form", 
                                           "description" : "see if forms are accessible", 
                                           "priority" : "medium", 
                                           "tags" : ["form"]})
    test_create_directory = TestCase.from_dict({"name" : "test_create_directory", 
                                           "description" : "attempt to create directory", 
                                           "priority" : "low", 
                                           "tags" : ["directory"]})
    
    suite = TestSuite("Basic Tests", [test_login, test_logout, test_submit_form, test_change_directory, 
                                      test_access_form, test_create_directory])
    
    high_priority_tests = suite.get_by_priority("high")
    
    print("High Priority Tests: ")
    for test in high_priority_tests:
        print(test.name)
    
    print("")
    
    results = TestRunner.run(suite)
    TestRunner.summary(results)
    

if __name__ == "__main__":
    main()