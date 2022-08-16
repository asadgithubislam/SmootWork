class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.name}")
harrysApplication = RailwayForm()
harrysApplication.name = "Harry"
harrysApplication.train = "Ilama Iqbal Express"
harrysApplication.printData()