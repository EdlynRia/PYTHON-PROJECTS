with open('sample1.py','w')as file:
    file.write("hi i am nivesh and i am 1 year old")
    file.close()


with open('sample1.py','r') as file:
    data=file.readlines(
        print("words in this file are...............")    )
    for line in data:
        word=line.split()
        print(word)
    file.close()