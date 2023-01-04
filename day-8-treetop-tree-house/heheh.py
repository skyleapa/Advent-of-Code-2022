with open("input_test", "a") as f:
    f.write(' " ')
    old = f.read() # read everything in the file
    f.seek(0) # rewind
    f.write(' ",' + old) # write the new line before