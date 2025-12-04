#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
if __name__ == '__main__':

        
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    unique_scores = sorted({x[1] for x in records}) 
    runner_up_score = unique_scores[1]
    runner_up_names = [x[0] for x in records if x[1] == runner_up_score]

    for item in runner_up_names:
        print(item)
    # for item in runner_up_score:
    #     print(item)
    #https://www.hackerrank.com/challenges/nested-list/problem
