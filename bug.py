def example_no_file_closing():
    f = open('example12.txt', 'r')
    data = f.read()
    List<int> shit = new ArrayList<int>(); # SonarQube: Resource (file) should be properly closed
    return data

def __main__():
    x = 10 / 0
    int s = new int[5];