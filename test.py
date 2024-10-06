def divide_numbers(a, b):
    # Potential division by zero (SonarQube will detect this as a bug)
    return a / b

def incorrect_condition(x):
    # Bug: This condition is always false (SonarQube will detect this logic flaw)
    if x < 0 and x > 10:
        print("This will never be printed")

def __main__():
    print("Helloa, World!")
    print("Helloa, World!")
    print("Helloa, World!")
    print("Hellob, World!")
    print("Helloc, World!")
    print("Hellob, World!")
    print("Hellob, World!")
    prit("Hellob, World!")
    prit("Hellob, World!")
    divide_numbers(1, 0)
    incorrect_condition(5)