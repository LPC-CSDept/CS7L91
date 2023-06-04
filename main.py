

def makeStudent(names, scores):
    """
    ########################################
    Code Your Program here
    ########################################
    """

    return student


def printStudent(student):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    for k, v in student.items():
        print(f'{k} : \t {v}')


def getMaxScore(student):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():
    names = ['Kim', 'Bill', 'Mary']
    scores = [[100, 80, 70, 60],
              [100, 90, 80, 60],
              [90, 80, 70, 100]]
    student = makeStudent(names, scores)
    printStudent(student)
    sname = getMaxScore(student)
    print(f'The max score student {sname} : {student[sname]}')


if __name__ == '__main__':
    main()
