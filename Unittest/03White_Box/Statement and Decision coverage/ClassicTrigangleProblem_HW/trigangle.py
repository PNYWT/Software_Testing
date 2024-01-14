class Trigangle:
    def __init__(self):
        return

    def get_triangle_type(self,a, b, c) -> str:
        if (a <= 0) or (b <= 0) or (c <= 0):
            return "Invalid"
        type = 0
        if a == b:
            type = type + 1
        if a == c:
            type = type + 2
        if b == c:
            type = type + 3
            
        if type == 0:
            if ((a + b) < c) or ((a + c) < b) or ((b + c) < a):
                return "Invalid"
            else:
                return "Scalene"

        if type > 3:
            return "Equilateral"

        if type == 1 and (a + b) > c :
            return "Isosceles"
        elif type == 2 and (a + c) > b :
            return "Isosceles"
        elif type == 3 and (b + c) > a :
            return "Isosceles"
        return "Invalid"
    