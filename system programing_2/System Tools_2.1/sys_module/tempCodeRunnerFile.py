]
        lines = lines[numlines:]
        for line in chunk: 
            print(line)
            if lines and input('More?') not in ['y', 'Y']: break

if __name__ == '__main__':