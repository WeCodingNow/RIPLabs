from LabPythonOOP.circle import Circle
from LabPythonOOP.rectangle import Rectangle
from LabPythonOOP.square import Square

if __name__ != "__main__":
    quit(0)

testrec = Rectangle(width=3, height=2, colour="Blue")
print(testrec)
testcir = Circle(radius=5, colour="Green")
print(testcir)
testsquare = Square(side=5, colour="Red")
print(testsquare)