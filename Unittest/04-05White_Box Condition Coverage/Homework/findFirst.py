class FindFirst:

    def __init__(self) -> None:
        pass
    
    def find_first(self, array, x):
        for count, value in enumerate(array):
            if value == x:
                return count
        return -1
    
# if __name__ == "__main__":
#     abc = FindFirst()
#     print(abc.find_first([],1))