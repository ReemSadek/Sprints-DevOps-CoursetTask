import sprints as sprints

def testCaseTwo():
    listInt = [10, 20, 30, 40, 50, 60]
    listFloat = [-190.0, -1000.1, 190, -50.0]
    result = sprints.meanCalculator(listInt, listFloat)
    assert result[0] == (10+20+30+40+50+60) / 6, "Should be {(10+20+30+40+50+60) / 6}"
    assert result[1] == 190, "Should be 190"

def testCaseOne():
    listInt = [1, 2, 3, 4, 5, 6]
    listFloat = [9.1, 10.2, 31.4, 56.5, 100.6]
    result = sprints.meanCalculator(listInt, listFloat)
    assert result[0] == (2+4+6) / 3, "Should be 4"
    assert result[1] == 100.6, "Should be 100.6"



if __name__ == "__main__":
    testCaseOne()
    testCaseTwo()
    print("The two test cases passed successfully")