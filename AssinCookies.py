student = [1, 2, 3]
cookie = [1, 2]

student.sort()
cookie.sort()
i = 0  
j = 0  
count = 0
while i < len(student) and j < len(cookie):
    if cookie[j] >= student[i]:
        count += 1
        i += 1
        j += 1
    else:
        j += 1

print(count)
