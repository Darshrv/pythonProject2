class BaseTest:
    def open_browser(self):
        print("Starting the browser")

class TestCase1(BaseTest):
    def test_1(self):
        self.open_browser()
        print("Test case 1 executed")
        self.close_browser()

class TestCase2(BaseTest):
    def test_2(self):
        self.open_browser()
        print("Test case 2 executed")
        self.close_browser()

