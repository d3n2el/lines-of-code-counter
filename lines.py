import sys
def main():
    length=
    #check for length of sys.argv and respond accordingly
    if sys.argv < 2:
        sys.exit("Too few command-line arguments")
    elif sys.argv > 2:
        sys.exit
    else:
        with open(f"{sys.argv[1]}") as file:
            lines = file.readlines()
    for line in lines:
        if line.lstrip().startswith("#"):
            comment+= lines(line)
        elif line

        else:
            length.append(line)





main()


