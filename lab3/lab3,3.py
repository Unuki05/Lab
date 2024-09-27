def tool(ug):
    useg = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    
    for i in ug:
        if i in useg:
            useg[i] += 1
            
    return useg

A = ("abcdefkjyhtgnbgrspoikjabcdefkjyhtgnbgrspoikj"
     "abcdefkjyhtgnbgrspoikjabcdefkjyhtgnbgrspoikj gkdljfhgkdfhgkld")

too = tool(A)

for x in 'abcde':
    print(f"{x}: {too[x]}")
