import time

class RecursiveNum:
    def __init__(self, value):
        assert isinstance(value, int), "value must be an integer"
        self.value = value

    def return_value(self):
        if self.value == 0:
            return 0
        else:
            return 1 + RecursiveNum(self.value - 1).return_value()

    def __add__(self, addition_value):
        if addition_value.value == 0:
            return RecursiveNum(self.value)
        elif addition_value.value > 0:
            return RecursiveNum(self.value + 1) + RecursiveNum(addition_value.value - 1)
        else:
            return RecursiveNum(self.value - 1) + RecursiveNum(addition_value.value + 1)
        
    def __mul__(self, multiply_value):
        # multiply_value must be positive int
        assert multiply_value.value 
        if multiply_value.value == 1:
            return RecursiveNum(self.value)
        else:
            # 3x = 2x + x 
            return RecursiveNum(self.value).__add__(
                RecursiveNum(self.value).__mul__(
                    RecursiveNum(multiply_value.value).__add__(
                        RecursiveNum(-1)
                    )
                )
            )

    def __repr__(self):
        return f"RecursiveNum({self.value})"


start_time = time.time()
result = RecursiveNum(200) * RecursiveNum(4)
end_time = time.time()
print(result)
print(f"Esoteric multiplication time: {end_time - start_time} seconds")

# Standard Multiplication Timing
start_time_standard = time.time()
standard_result = 200 * 4
end_time_standard = time.time()
print(standard_result)
print(f"Standard multiplication time: {end_time_standard - start_time_standard} seconds")