def question_1():
    n = 10
    count = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i < j and j < k:
                    count += 1

    print("Question 1 Output:", count)


def question_2():
    n = 1000
    count = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i < j and j < k:
                    count += 1

    print("Question 2 Output:", count)


# Run the questions
question_1()
question_2()
