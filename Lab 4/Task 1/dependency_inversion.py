# logic must work with abstractions not with concrete realizations

class GoogleDriver:
    def start(self):
        print("Connecting to Google web driver")

class Parser:
    def __init__(self):
        self.driver: GoogleDriver = GoogleDriver()

    def load_data(self):
        self.driver.start()

# right variant

from abc import ABC, abstractmethod

class WebDriver(ABC):
    @abstractmethod
    def start(self) -> None:
        pass

class RightGoogleDriver(WebDriver):
    def start(self) -> None:
        print("Connecting to Google web driver")

class RightParser:
    def __init__(self, driver: WebDriver):
        self.driver:  WebDriver = driver

    def load_data(self):
        self.driver.start()