#ProcessData.py
#Name:
#Date:
#Assignment:

def main():
    inFile = open("names.dat", 'r')
    outFile = open("StudentList.csv", 'w')


    for line in inFile:
        data = line.split()
        first = data[0]
        last = data[1]
        idNum = data[3]
        major = data[4] [:3]
        year_full = data [5]. lower()

        if year_full == "freshman" :
            year = "FR"
        elif year_full == "sophomore" :
            year = "SO"
        elif year_full == "junior" :
            year = "JR"
        elif year_full == "senior" :
            year = "SR" 
        else:
            year = "NA"
        
        major_year = major + "-" + year
    
        

        student_id = makeID(first, last , idNum)

        output = last + "," + first + "," + student_id + major_year + "\n"
        outFile.write(output)

    inFile.close()
    outFile.close()


def makeID(first, last, idNum):
    
    idLen = len(idNum)

    while len(last) < 5:
        last = last + "x"

    # Get last 3 digits of student ID (after removing dashes)
    id =first[0] + last + idNum[idLen - 3: ]

    # Build and return UserID
    return id





if __name__ == '__main__':
    main()
