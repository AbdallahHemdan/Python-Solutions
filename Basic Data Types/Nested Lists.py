n = int(input())
students = []
for i in range(n):
    students.append([input(), float(input())])
scores = set([students[x][1] for x in range(n)])
scores = list(scores)
scores.sort()

students = [x[0] for x in students if x[1] == scores[1]]
students.sort()

for s in students:
    print (s)
