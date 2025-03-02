# Write a Python program to write a list to a file.


def writesome(list_of_elements):
    with open("extext.txt", '+a') as f:
        text = "\n"
        for i in list_of_elements:
            text+=str(i)+' '
        f.write(text)
        f.close()
    
 

writesome([111223, 6665544, 7788999 ,"Aktau","Almaty",15,18])