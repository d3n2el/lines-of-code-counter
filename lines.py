import sys
def main():
    length=[]
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        with open(f"{sys.argv[1]}") as file:
            lines = file.readlines()
    for line in lines:
        if line.lstrip().startswith("#") or line.strip() == "":
            continue
        else:
            length.append(line)

    print(len(length))





main()


