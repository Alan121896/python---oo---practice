"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    """
    
    Attributes:
    - start: The starting number for the serial generator.
    - next_num: The next sequential number to be generated.
    """
    
    def __init__(self, start):
        """
        Initialize the SerialGenerator with a start number.
        
        Args:
        - start: The starting number for the serial generator.
        """
        self.start = start
        self.next_num = start
    
    def generate(self):
        """
        Generate the next sequential number and return it.
        
        Returns:
        - The next sequential number.
        """
        num = self.next_num
        self.next_num += 1
        return num
    
    def reset(self):
        """
        Reset the serial generator back to the original start number.
        """
        self.next_num = self.start

