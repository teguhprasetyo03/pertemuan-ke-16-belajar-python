# local scope / local variabel
# variabel yang dibuat di dalam fungsi, hanya bisa
# di panggil di dalam fungsi tersebut

def hello():
    j = 200
    print(j)

hello()

# global scope / global variabel
# variabel yang dibuat secara global atau
# diluar function
x = 300
def func():
    print(x)

func()
print(x)

# membuat function di dalam function

def hello_bro():
    a = 125.5
    def hello_cin():
        print(a)
    hello_cin()

hello_bro()


# membuat function global
nilai_a = 200


def tampil_nilai_a():
    print(nilai_a)
    def tampil_nilai_b():
        # nilai b harus di local
        nilai_b = 100
        print(nilai_b)
    tampil_nilai_b()

tampil_nilai_a()

# kalo kita membuat variabel lokal menjadi global
# dengan keyword global
def hitung():
    global x
    x = 300

hitung()
print(x)

# mengubah variabel global
i = 20
def hitung_bro():
    global i
    i = 200

hitung_bro()
print(i)




