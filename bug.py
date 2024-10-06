def example_no_file_closing():
    f = open('example123.txt', 'r')
    data = f.read()
    isYes = 1 <> 2 # SonarQube: Resource (file) should be properly closed
    return data

def __main__():
    x = 10 / 0
    int s = new int[5];