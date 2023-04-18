

def makeStudent(student):
    ##################################################
    # Code your program here
    ##################################################


def printStudent(student):
    ##################################################
    # Code your program here
    ##################################################


def getMaxScore(student):
    ##################################################
    # Code your program here
    ##################################################


def main():
    student = {}
    makeStudent(student)
    printStudent(student)
    sname = getMaxScore(student)
    print(f'The max score student {sname} : {student[sname]}')


if __name__ == '__main__':
    main()
