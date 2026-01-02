n = 3

a = [[4,-2,0],[-2,4,-2],[0,-2,4]]

b = [-0.5,-0.5,-0.5]

xn = [0,0,0]

x = [0,0,0]


anzahl = 1

for iteration in range(anzahl):
   

    for i in range(n):
        s1 = 0
        s2 = 0

    #erste Summe

        for j in range(i):
            s1 += a[i][j]*x[j]

    #zweite Summe

        for j in range(i+1,n):
            s2 += a[i][j]*x[j]


        xn[i] = (1/a[i][i]) * (b[i]-s1-s2)

    for i in range(n):
        x[i] = xn[i]

print(x)