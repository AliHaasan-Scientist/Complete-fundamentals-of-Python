class Machine:
    def __init__(self, inputType, outputTupe, processing):
        self.inputType = inputType
        self.outputTupe = outputTupe
        self.processing = processing

    def show(self):
        return self.inputType, self.outputTupe, self.processing

    pass


class Program:
    def __init__(self, programLang, translator):
        self.programLang = programLang
        self.translator = translator

    def mahineCode(self):
            return self.programLang, self.translator


class Robote(Machine,Program):
    RoboteName = "Alfa"



Alfa1 = Robote("Raw data", "Image", "Lambda calculas")
print(Alfa1.show())