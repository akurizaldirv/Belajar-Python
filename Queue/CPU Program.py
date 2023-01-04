import queueProgram as qq

def createProgram(banyak):
    q = qq.createQueue()
    for i in range(banyak):
        a = input("Nama proses ke-{} : ".format(i))
        b = int(input("Waktu proses : "))
        c = [a,b]
        qq.enqueue(q,c)
    print("")
    CPUProcess(q)

def CPUProcess(q):
    d = int(input("Waktu proses CPU : "))
    print("")
    print("Antrian proses beserta waktunya =", q)
    g = 0
    while qq.size(q) != 0:
        e = len(q) - 1
        f = q[e]
        f[1] = f[1] - d
        g = g+1
        if f[1]<1:
            qq.dequeue(q)
            print("Iterasi ke-{}".format(g))
            print("     Proses {} telah selesai di proses".format(f[0]))
            print("     Data yang tersisa =", q)
            print('')
        else:
            qq.dequeue(q)
            qq.enqueue(q,f)
            print("Iterasi ke-{}".format(g))
            print("     Proses {} sedang di proses, dan sisa waktu proses {} = {}".format(f[0], f[0], f[1]))
            print("     Data yang tersisa =", q)
            print('')

banyak = int(input('Jumlah proses yang akan di jadwal CPU = '))
createProgram(banyak)
