# basic file write
filename = input("Enter filename: ")
content_ = "This is a test\n"
try:
    outfile = open(filename, "w")
except:
    print("Program unable to be opened!")
    raise

try:
    outfile.write(content_)
finally:
    outfile.close()
print('Continue with program')