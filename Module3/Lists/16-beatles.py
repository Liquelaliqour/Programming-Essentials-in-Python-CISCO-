beatles = []                              # step 1
print("Step 1:", beatles)

beatles.append("John Lennon")               # step 2
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Step 2:", beatles)

for i in range(2):                         # step 3
    beatles.append(input("Add members to the beatles club : "))

print("Step 3:", beatles)

del beatles[-1]                                   # step 4
del beatles[-1]
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")           # step 5
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))
