import urllib2

def get_web_file(path):
    """Gets a file over http.
    
    Args:
        path: string url of the desired file.

    Returns:
        The desired file as a string.        
    """
    response = urllib2.urlopen(path)
    return response.read()

def copy_web_file_to_local(file_path, target_path):
    """Copies a file from its location on the web to a designated 
    place on the local machine.

    Args:
        file_path: Complete url of the file to copy, string (e.g. http://fool.com/input.css).

        target_path: Path and name of file on the local machine, string. (e.g. /directory/output.css)

    Returns:
        None.

    """
    response = urllib2.urlopen(file_path)
    f = open(target_path, 'w')
    f.write(response.read()) 
    f.close()

def get_line_count(fname):
    """Counts the number of lines in a file.

    Args:
        fname: string, name of the file.

    Returns:
        integer, the number of lines in the file.

    """
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def indent_css(f, output):
    """Indentes css that has not been indented and saves it to a new file.
    A new file is created if the output destination does not already exist.

    Args:
        f: string, path to file.

        output: string, path/name of the output file (e.g. /directory/output.css).
    print type(response.read())

    Returns:
        None.
    """
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
