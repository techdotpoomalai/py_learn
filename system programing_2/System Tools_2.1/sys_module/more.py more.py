# C:\...\PP4E\System> python more.py more.py
def more(text, numlines=15):
    lines = text.splitlines() # like split('\n') but no '' at end
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: 
            print(line)
            if lines and input('More?') not in ['y', 'Y']: break

if __name__ == '__main__':
    import sys # when run, not imported
    more(open(sys.argv[0]).read(), 10) # page contents of file on cmdline