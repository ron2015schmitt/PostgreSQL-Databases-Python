


# write to file
# "w" - overwrite
# "a" - append

f=open("test.txt","w")

f.write("Hello world in a file!")
f.close()

f=open("ledger.txt","w")
f.write("1 Joe 350\n")
f.write("2 Rob 3500\n")
f.write("3 Cindy 450\n")
f.close()


# read from file
# "r"
f=open("ledger.txt","r")

while True:
    line=f.readline()
    split = line.split()
    try:
        index = split[0]
        name = split[1]
        balance = split[2]
        print("index=",index)
        print("name=", name)
        print("balance=", balance)
    except:
        break
f.close()


