import urllib2

def get_web_file(path):
    response = urllib2.urlopen(path)
    return response.read()

def copy_web_file_to_local(file_path, target_path):
    response = urllib2.urlopen(file_path)
    f = open(target_path, 'w')
    f.write(response.read()) 
    f.close()

def get_line_count(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def indent_css(f, output):
    line_count = get_line_count(f)
    f = open(f, 'r+')
    output = open(output, 'w')
    for line in range(line_count):
        string = f.readline().rstrip()
        if len(string) > 0:
            if string[-1] == ";":
                output.write("    " + string + "\n")
            else:
                output.write(string + "\n")
    output.close()
    f.close()
