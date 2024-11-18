def cyclic_sequence(sequence):
    while True:
        for item in sequence:
            yield item

if __name__ == "__main__":

    sequence = [1, 2, 3]
   
    count = int(input("Enter quantity of numbers: "))
    if count <= 0:
        print("wrong quantity of numbers")
    else:
        generator = cyclic_sequence(sequence)
        for _ in range(count):
            print(next(generator), end=" ")
