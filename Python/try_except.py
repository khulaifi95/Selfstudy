## Try/except for error handling

try:
    f = open('testfile.txt')  # throw an exception
    if f.name == 'corrupt_file.txt':
        raise Exception
except FileNotFoundError as e:  # print the exact exception
    print(e)
except Exception as e:  # common exceptions
    print(e)
else:   # if no exception
    print(f.read())
    f.close()
finally:    # run no matter what happens
    print('Executing finally...')
