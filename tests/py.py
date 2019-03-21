#Python test
import os

print("Hello world")

def getDir():
    return os.getcwd()

print(getDir())

tuple = (0, "hola")

print(tuple[0], " ", tuple[1])