filename = input("Enter filename: ")
outfile = open(filename, "w")
content_ = "This is a test\n"
try:
    outfile.write(content_)
finally:
    outfile.close() 