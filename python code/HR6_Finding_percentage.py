if __name__ == '__main__':
    n = int(input())
    student_marks = dict()
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
for i in student_marks.keys():
    if(i==query_name):#print(round(float(sum(student_marks[i])/3),2))
        print("{0:.2f}".format(sum(student_marks[i])/3))
        #print('%.2f'%sum(student_marks[i])/3)
        #print("{0:.2f}".format(sum(query_scores)/(len(query_scores))
#the last print statement is used to print the output precise upto two decimal places
