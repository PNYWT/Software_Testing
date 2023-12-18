class Power:
    def power(self, base, exp):
        result = 1
        if exp < 0:
            return -1
        for i in range(exp):
            result = result * base
        return result