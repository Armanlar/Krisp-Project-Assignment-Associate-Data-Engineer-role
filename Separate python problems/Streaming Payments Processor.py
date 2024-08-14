import os
from io import BufferedWriter, RawIOBase
class Checksum(BufferedWriter):
    def __init__(self, raw: RawIOBase) -> None:
        super().__init__(raw)
        self.checksum = 0
    def write(self, data):
        super().write(data)
        self.checksum += sum(data)
    
    
    # Here print the check sum of al
    # l of the bytes written by
    # `stream_payments_to_storage()`
def get_payments_storage():
    return open(os.devnull, 'wb')

def stream_payments_to_storage(storage):
    for i in range(10):
        storage.write(bytes([1, 2, 3, 4, 5]))

def process_payments():
    checksum = Checksum(get_payments_storage())
    stream_payments_to_storage(checksum)
    print(checksum.checksum)
process_payments()