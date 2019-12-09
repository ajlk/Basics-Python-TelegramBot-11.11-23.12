ans = []
for i in objects:
    if id(i) not in ans:
        ans.append(id(i))
print(len(ans))
