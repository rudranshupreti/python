# Practice Problem: Create a countdown timer that starts from a given number and counts down to zero using a while loop.
def down(i):
    while i>0:
        print(i)    
        i-=1
print(down(8))

# Practice Problem: Write a program that creates a new text file named notes.txt, writes three separate lines of text to it, and then reads that file back to display the contents in the console.
with open("h.txt","w") as f:
    f.write("lorem")

with open("h.txt","r") as f:
    print(f.read())
    
# Practice Problem: Write a script that opens an existing .txt file and counts the total number of words it contains.

with open("h.txt","r") as f:
    w = list(f)
    print(len(w))