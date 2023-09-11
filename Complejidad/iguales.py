

A = [1,2,3]
B = [2,3,1]
C = [False,False,False]

for i in range(len(A)):
    for j in range(len(B)):
        print(i,",",j)
        print(A[i])
        print(B[j])
        if  A[i] == B[j]:
            if not C[j]:
                C[j] = True
                print(C)
                break
    print(C)
        
                
   


            
