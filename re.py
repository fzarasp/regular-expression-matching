import copy
def GetRE():
    print('Please Enter the Regular Expression')
    r = input().split('-')
    ro = []
    for item in r:
            if item[0] == '[':
                sub = []
                for k in range(1 , item.index(']')):
                    sub.append(item[k])
                if len(item)> item.index(']') + 1:
                    count =  int(item[item.index(']') + 2])
                else:
                    count = 1
                sub.append(count)
                sub.append('1')
                ro.append(copy.deepcopy(sub))
            if item[0] == '{':
                sub = []
                for k in range(1 , item.index('}')):
                    sub.append(item[k])
                if len(item)> item.index('}') + 1:
                    count =  int(item[item.index('}') + 2])
                else:
                    count = 1
                sub.append(count)
                sub.append('0')
                ro.append(copy.deepcopy(sub))
            if item[0] != '{' and item[0] != '[':
                sub = []
                if len(item) == 1:
                    count = 1
                else:
                    count = int(item[2])
                sub = [item[0] , count,'1']
                ro.append(copy.deepcopy(sub))


    return ro

def RE(ro , rin):
    rout = ''
    i = 0
    j = 0
    #print(ro)
    while j <len(rin):
        #print(i , ro[i] , rin[j] , rout)
        rx = ro[i]
        state = rx[len(rx) - 1]
        count = int(ro[i][len(ro[i]) - 2])
        if state == '1':
            if ro[i][0] == 'X':
                for k in range(count):
                    rout = rout + '1'
                    j = j + 1
            else:
                for k in range(count):
        #            print(rin[j] , ro[i][0:len(ro[i]) - 2])
                    if rin[j] in ro[i][0:len(ro[i]) - 2]:

                        rout = rout + '1'
                    else:
                        rout = rout + '0'
                    j = j + 1
        else:
            for k in range(count):
                if not(rin[j] in ro[i][0:len(ro[i]) - 2]):
                    rout = rout + '1'
                else:
                    rout = rout + '0'
                j = j + 1
        i = i  + 1

    return rout



def Counter(s):
    c = 0
    for i in range(len(s)):
        if s[i] == '0':
            c = c + 1
        if c > 2:
            return 'No'

    return 'Yes'



x = GetRE()
n = int(input('Number of sequences:  '))
rin = []
print('Please Enter the sequences')
for i in range(n):
    r = input()
    rin.append(r)

print('-----RESULT----')
for rx in rin:
    y = RE(x , rx)
    print(Counter(y) , y)

#for item in x:
#    print(item)
