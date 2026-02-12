if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        # {'Ion': [1.0, 4.0, 6.0]}
        
        print(student_marks)
    query_name = input()
    student = student_marks[query_name]
    average = sum(student) / len(student)
    print("{0:.2f}".format(average))
    #https://www.hackerrank.com/challenges/finding-the-percentage/problem