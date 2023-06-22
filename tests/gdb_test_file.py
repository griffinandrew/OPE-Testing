import pdb

def divide(x, y):
    result = x / y
    print(f"The result is: {result}")

# Set a breakpoint
pdb.set_trace()

divide(10, 0)
