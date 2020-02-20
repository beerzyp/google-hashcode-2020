from operator import itemgetter

hashGlobal = dict()


def main():
    infile = open("b_read_on.txt", "r")
    firstLine = infile.readline().split()
    numBooks = int(firstLine[0])
    numLibs = int(firstLine[1])
    numDays = int(firstLine[2])
    scores = infile.readline().split()
    scores = [int(i) for i in scores]
    allLibraries = []
    for i in range(int(numLibs)):
        library = dict()
        firstLine = infile.readline().split()
        library['numBooks'] = int(firstLine[0])
        library['signDays'] = int(firstLine[1])
        library['booksPerDay'] = int(firstLine[2])
        secondLine = infile.readline().split()
        library['listBooks'] = secondLine
        allLibraries.append(library)
    orderingSignUp(allLibraries)


def orderingSignUp(allLibraries):
    #sorting by longest signup period
    sortedLibraries = sorted(allLibraries, key=itemgetter('signDays'))
    for i in sortedLibraries:
        print(i)


if __name__ == '__main__':
    main()
