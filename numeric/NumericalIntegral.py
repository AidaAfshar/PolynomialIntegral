def function(coefficients, x):
    degree = len(coefficients) - 1
    f = 0
    for i in range(degree + 1):
        y = x ** i
        f += y * coefficients[i]
    return f


def convertStringToIntegerList(coefficientsInString):
    coefficientsInChar = coefficientsInString.split(',')
    coefficients = []
    for coefficient in coefficientsInChar:
        coefficients.append(float(coefficient))
    return coefficients


def calculateIntegral(coefficients, initialPoint, finalPoint, accuracy):
    interval = finalPoint-initialPoint
    dx = interval/accuracy
    x = initialPoint
    y = 0
    for i in range(accuracy):
        y += function(coefficients, x+(dx/2))
        x += dx
    result = y*dx
    return result


print("enter polynomial coefficients:")
print("(for polynomial 4x^3 + 1x - 6 the input is 4, 0, 5, -6)")
coefficientsInString = input()
coefficients = convertStringToIntegerList(coefficientsInString)
coefficients.reverse()
print("enter initial point:")
initialPoint = float(input())
print("enter final point:")
finalPoint = float(input())
print("enter accuracy:")
accuracy = int(input())
integralResult = calculateIntegral(coefficients, initialPoint, finalPoint, accuracy)
print("result: "+str(integralResult))
