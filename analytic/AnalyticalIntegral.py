def function(coefficients, x):
    degree = len(coefficients) - 1
    f = 0
    for i in range(degree + 1):
        y = x ** i
        f += y * coefficients[i]
    return f


def getAntiDerivative(coefficients):
    antiDerivative = [0]
    for i in range(len(coefficients)):
        antiDerivative.append(coefficients[i] / (i + 1))
    return antiDerivative


def calculateIntegral(coefficients, initialPoint, finalPoint):
    antiDerivative = getAntiDerivative(coefficients)
    finalValue = function(antiDerivative,finalPoint)
    initialValue = function(antiDerivative, initialPoint)
    integralResult = finalValue-initialValue
    return integralResult


def convertStringToIntegerList(coefficientsInString):
    coefficientsInChar = coefficientsInString.split(',')
    coefficients = []
    for coefficient in coefficientsInChar:
        coefficients.append(int(coefficient))
    return coefficients


print("enter polynomial coefficients:")
print("(for polynomial 4x^3 + 1x - 6 the input is 4, 0, 5, -6)")
coefficientsInString = input()
coefficients = convertStringToIntegerList(coefficientsInString)
coefficients.reverse()
print("enter initial point:")
initialPoint = int(input())
print("enter final point:")
finalPoint = int(input())
integralResult = calculateIntegral(coefficients, initialPoint, finalPoint)
print("result: "+str(integralResult))
