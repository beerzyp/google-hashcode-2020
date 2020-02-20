import copy
import itertools

hashGlobal = dict()


def main():
    infile = open("a_example.txt", "r")
    firstLine = infile.readline().split()
    numBooks = firstLine[0]
    numLibs = firstLine[1]
    numDays = firstLine[2]
    scores = infile.readline().split()
    allLibraries = []
    for i in range(int(numLibs)):
        library = dict()
        firstLine = infile.readline().split()
        library['numBooks'] = firstLine[0]
        library['signDays'] = firstLine[1]
        library['booksPerDay'] = firstLine[2]
        secondLine = infile.readline().split()
        library['listBooks'] = secondLine
        allLibraries.append(library)
    print(allLibraries)

# def auxCombination(): # Calculates sum for each combo

if __name__ == '__main__':
    main()
