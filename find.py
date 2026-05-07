the_string = 'Cosmo the dog'
the_pattern = 'mo'

# Look for a single-character pattern in a string using a for-loop
for i in range(len(the_string)):
    if the_string[i] == the_pattern:
        print("Found at index", i)
        break
else:
    print("Not found")