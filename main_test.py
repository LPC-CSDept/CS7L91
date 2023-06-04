import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    names = ['Kim', 'Bill', 'Mary']
    scores = [[100, 80, 70, 60],
              [100, 90, 80, 60],
              [90, 80, 70, 100]]
    student = main.makeStudent(names, scores)
    print(f'Your return value is : {student}')
    assert isinstance(student, dict)
    main.printStudent(student)

    sname = main.getMaxScore(student)
    assert sname == 'Mary'
    assert student[sname] == [90, 80, 70, 100]
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    names = ['Jane', 'John', 'Tom']
    scores = [[100, 100, 100],
              [90, 90, 90],
              [80, 80, 80]]
    student = main.makeStudent(names, scores)
    print(f'Your return value is : {student}')
    assert isinstance(student, dict)
    main.printStudent(student)

    sname = main.getMaxScore(student)
    assert sname == 'Jane'
    assert student[sname] == [100, 100, 100]
