class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be appended")
        if integer % 2:
            raise ValueError("Only even numbers can be appended")
        super().append(integer)
