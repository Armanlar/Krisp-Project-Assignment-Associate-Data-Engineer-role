import io

# This is a library function, you can't modify it.
def stream_payments(callback_fn):
    for i in range(10):
        callback_fn(i)

# This is a library function, you can't modify it.
def store_payments(amount_iterator):
    for i in amount_iterator:
        print(i)
# I couldn't find a solution with calling the store_payments once while not storing the data.
def count_amount(amount):
    yield amount

def callback(amount):
    amount_iter = count_amount(amount)
    store_payments(amount_iter) 


def process_payments_2():
    stream_payments(callback)

process_payments_2()
