def son_iguales(A,B,C):
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


if __name__ == "__main__":
    A = [1,2,3]
    B = [2,3,1]
    C = [False,False,False]
    
    son_iguales(A, B, C)


            
