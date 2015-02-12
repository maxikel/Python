import commands, os, string

def ps ():
    program = raw_input("Enter the name of the program to check: ")

    try:
        output = commands.getoutput("ps -f |grep " + program)
        proginfo = string.split(output)

        print "\n\
            Full path:\t\t", proginfo[5], "\n\
            Owner:\t\t\t", proginfo[0], "\n\
            Process ID:\t\t", proginfo[1], "\n\
            Parent Process ID:\t", proginfo[2], "\n\
            Time Started:\t\t", proginfo[4]
    except:
        print "There was a problem with the program."

def main():
    if os.name == "posix":
        ps()
    elif os.name in ("nt", "dos", "ce"):
        print "You need to be on Linux or Unix to run this."


if __name__ == '__main__':
    main()
