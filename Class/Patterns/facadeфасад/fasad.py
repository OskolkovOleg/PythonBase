# FIXME

class Builder:
    def build(self):
        print("Building...")


class Vendor:
    def give(self):
        print("Giving the materials...")
    

class Investor:
    def invest(self):
        print("Investing...")


class Facade:
    def __init__(self) -> None:
        self.investor = Investor()
        self.vendor = Vendor()
        self.builder = Builder()

    def start_project(self):
        for i in range(3):
            investor = Investor()
            investor.invest()

        for i in range(30):
            vendor = Vendor()
            vendor.give()

        for i in range(50):
            builder = Builder()
            builder.build()
        
        print("proect finished")

if __name__ == "__main__":   
    facade = Facade()
    facade.start_project()
