# lists.py

mylist = [5, 10, 15, 20]
print(mylist)
mytype = type(mylist)
print(mytype)

# start address + size of one data leement * offset

print(mylist[0])
print(mylist[1])


for val in mylist:
    print(val)


for val in range(len(mylist)):
    print(val)
    print(mylist[val])


# Don't use these unless you're going to

for idx, val in enumerate(mylist):
    print(f"{idx}: {val}")

i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1


mylist.append(25)
for val in mylist:
    print(val)


length = len(mylist)

mylist = [1, 2.5, "3.5", [4, 5, 6], (6, 7)]
print(mylist)
print(len(mylist))


mylist = [0] * 15
print(mylist)

mylist = [1, 2, 3] * 5
print(mylist)
lista = list(range(1, 3))
listb = list(range(2, 5))
listc = lista + listb
print(listc)


# find out if an element is in the list
mylist = ["a", "b", "c", "d", "e"]
if ("c" in mylist):
    print("hello")
else:
    print("oh no")


idex = mylist.index("d")
print(idex)

print(list(range(1, 2)))

idx - mylist.index("d", 3, 6)
print(idx)

# Inserting into list
mylist.insert(3, "z")
print(mylist)


mylist.pop()
print(mylist)

mylist.pop(2)
print(mylist)


popped = mylist.pop()
print(mylist, popped)

print(len(mylist))


# Count things
cnt = mylist.count("a")
print(cnt)

mylist += "5", 0x01
print(mylist)
