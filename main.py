from matrix import Matrix

def main():

    matrix = Matrix(epsillon=0.0005,anzahl=61)

    eingelesen = matrix.einlesen_datei()

    n = eingelesen[0]
    a = eingelesen[1]
    b = eingelesen[2]


    x, _, _ = matrix.loese_gls(n,a,b)
    print(x)
    #print(matrix.loese_gls(n,a,b))

if __name__ == "__main__":
    main()