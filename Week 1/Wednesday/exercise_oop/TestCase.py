class TestCase:
    """Represents a single test case.

    Class Attributes:
        total_created (int): Count of all TestCase objects ever created

    Instance Attributes:
        name (str): Test name (e.g., "test_login_valid")
        description (str): What this test verifies
        priority (str): "high", "medium", or "low" (default: "medium")
        tags (list): Labels like ["smoke", "regression"]
    """
    
    total_created = 0
    
    def __init__(self, name : str, description : str, priority : str, tags : list[str]):
        self.name = name
        self.description = description
        self.priority = priority
        self.tags = tags
    
    @classmethod
    def from_dict(cls, data):
        """Create a TestCase from a dictionary.
        Example: TestCase.from_dict({"name": "test_login", "priority": "high"})
        """
        return cls(data["name"], data["description"], data["priority"], data["tags"])
    
    def run(self):
        """Simulate running the test. Return True for pass, False for fail.
        For now, use: return "fail" not in self.name
        """
        return self.is_valid_name(self.name)

    @staticmethod
    def is_valid_name(name : str):
        """Check if name starts with 'test_' and has no spaces."""
        if name.startswith("test_") and name.find(" ") == -1:
            return True
        else:
            return False