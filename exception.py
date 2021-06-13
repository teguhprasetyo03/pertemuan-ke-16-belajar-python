# exception dan error handling

# try

try:
    print(x)
except:
    print("Variabel x tidak di definisikan")

# while True:
 #   try:
  #      x = int(input("Masukkan number :"))
   #     break
   # except ValueError:
    #    print("Number yang anda masukkan salah : ... Please try again")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()