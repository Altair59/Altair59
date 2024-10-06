def example_no_file_closing():
    f = open('example1.txt', 'r')
    data = f.read()  # SonarQube: Resource (file) should be properly closed
    return data

def __main__():
    x = 10 / 0
    int s = new int[5];