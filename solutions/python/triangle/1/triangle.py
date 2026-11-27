def valid(sides):
    return (
        sides[0] + sides[1] > sides[2]
        and sides[2] + sides[1] > sides[0]
        and sides[0] + sides[2] > sides[1]
    )

def equilateral(sides):
    return valid(sides) and len(set(sides)) == 1

def isosceles(sides):
    return valid(sides) and len(set(sides)) <=2


def scalene(sides):
    return valid(sides) and len(set(sides)) == 3
