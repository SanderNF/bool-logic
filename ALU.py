

def ALU(f1,f2,f3, boolsA=[1,0], boolsB=[1,0]):
    if f1 == 0 and f2 == 0 and f3 == 0:
        operation = 'ADD'
    elif f1 == 0 and f2 == 0 and f3 == 1:
        operation = 'SUB'
    elif f1 == 0 and f2 == 1 and f3 == 0:
        operation = 'AND'
    elif f1 == 0 and f2 == 1 and f3 == 1:
        operation = 'OR'
    elif f1 == 1 and f2 == 0 and f3 == 0:
        operation = 'NAND'
    elif f1 == 1 and f2 == 0 and f3 == 1:
        operation = 'NOR'
    elif f1 == 1 and f2 == 1 and f3 == 0:
        operation = 'XOR'
    elif f1 == 1 and f2 == 1 and f3 == 1:
        operation = 'NOT'
    else:
        raise ValueError("Invalid control signals")
    out=[]
    c = 0
    for i in range(len(boolsA)):
        a = boolsA[i]
        b = boolsB[i]
        if operation == 'ADD':
            x = a ^ b               # xor bit
            s = x ^ c               # sum bit
            c = (a & b) | (c & x) # carry bit
            out.append(s)
        elif operation == 'SUB':
            x = a ^ b                 # xor bit
            s = x ^ c                 # sum bit
            c = (~a & b) | (c & ~x) # carry bit
            #print("x",x,"s",s,"c",c)
            out.append(s)
        elif operation == 'AND':
            out.append( a & b)
        elif operation == 'OR': 
            out.append( a | b)
        elif operation == 'NAND':
            out.append( (~(a & b))%2)
        elif operation == 'NOR':
            out.append( (~(a | b))%2)
        elif operation == 'XOR':
            out.append( a ^ b)
        elif operation == 'NOT':
            out.append( (~a)%2)
    return out
    


if __name__ == "__main__":
    def red_green(input):
        input = input.copy()
        for i in range(len(input)):
            if input[i] == 1:
                input[i] = "🟩"
            else:
                input[i] = "🟥"
        return input
    def test_ALU(i,a=[1,0,1,0], b=[1,1,0,0]):
        if i%2 == 0:
            f3 = 0
        else:
            f3 = 1
        if i%4 < 2:
            f2 = 0
        else:
            f2 = 1
        if i%8 < 4:
            f1 = 0
        else:
            f1 = 1
        
        result = ALU(f1, f2, f3, a, b)
        copyA = red_green(a)
        copyB = red_green(b) 
        result = red_green(result)
        Fs = red_green([f1, f2, f3])
        out = ""
        outA = ""
        outB = ""
        outF = ""
        for j in range(len(result)):
            out += str(result[j])
            outA += str(copyA[j])
            outB += str(copyB[j])
        for j in range(len(Fs)):
            outF += str(Fs[j])
            

        print(f"Result of operator code: {outF}\nA bits: {outA}\nB bits: {outB} \nresult:\n{out}\n")
        
    a = [1,0,1,0,1,0,1,0]
    b = [1,1,0,0,1,1,0,0]
    for i in range(8):
        test_ALU(i,a,b)
    