class TestResult:
    """The outcome of running a single test.

    Instance Attributes:
        test_name (str): Which test was run
        status (str): "pass" or "fail"
        duration_ms (float): How long it took
        error_message (str or None): Error details if failed
    """
    def __init__(self, test_name : str, status : str, duration_ms : float, error_message : str | None):
        self.test_name = test_name
        self.status = status
        self.duration_ms = duration_ms
        self.error_message = error_message
    
    def summary(self):
        """Return a one-line summary like: '✅ test_login (120ms)'"""
        return f"{"✅" if self.status == "pass" else "❌"} {self.test_name} ({self.duration_ms if self.status == "pass" else self.error_message})"