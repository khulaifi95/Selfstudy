# File objects

# Read

with open('text_file.txt', 'r') as f:
    f_contents = f.read(100)  # readlines(), readline()
    print(f_contents)

with open('text_file.txt', 'r') as f:
    for line in f:
        print(line, end='')

with open('text_file.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
        print(f.tell())  # seek()


# Write

with open('text_file_2.txt', 'r') as f:
    f.write('Test')
    f.seek(0)  # 2nd override 1st loc
    f.write('R')

with open('text_file.txt', 'r') as rf:  # read file
    with open('text_copy.txt', 'w') as wf:  # write file
        for line in rf:
            wf.write(line)

# Copy an image

with open('img.jpg', 'rb') as rf:  # read bit
    with open('img_copy.jpg', 'wb') as wf:  # write bit
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
