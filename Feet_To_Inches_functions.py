def checkfloatdata() :
    while True :
        try :
            floatdatatype = float(input())
        except ValueError :
            print("Wrong data type entered - RE-ENTER A POSITIVE VALUE")
            continue
        else :

            if floatdatatype < 0 :
                print("You entered a negative value -RE-ENTER A POSITIVE VALUE")
                continue
            else :

                break
    return floatdatatype

def convertdata(number) :
    inches = number*12
    return inches

def result(a, b, c) :
    c.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    c.write("           CONVERTING FEET TO INCHES\n")
    c.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    c.write("            " + format(a, ",.2f") + " feet = " + format(b, ",.2f") + " inches  \n")
    c.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def main() :
    filename = "Feet_Inches_Output.txt"
    outFile = open(filename, "w")
    print("What is the number of feet you are attempting to convert to inches?")
    feet = checkfloatdata()
    result(feet, convertdata(feet), outFile)
    outFile.close()

main()
        
