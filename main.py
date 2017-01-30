#PyNote
'''
Author:Python giant
Langage:Python 2.7
'''

#Say Welcome
print("\t\t\t Hello and welcome to PyNote")

def TheRecursion():

    #the place where we keep our file
    f=open("note.txt","r+")
    #ask the user what they want to do
    user=raw_input("what do you want to do[read,write,exit]")

    if user == "write" or user == "Write":
        #Ask the user for notes
        note=raw_input("Ok,give a title to your notes here:")
        body=raw_input("Now the body : ")    
        #ask for the date
        date=raw_input("what is the date ?")
        
        #write to the file
        f.write(date + ":" + note+"\n" )
        f.write(body)
        f.close()
        #Print the success 
        print ("Success! Note '"+ note + "' was added.")
        TheRecursion()
    elif user == "Read" or  user == "read":
        contents=f.read()
        print(contents)
        TheRecursion()
    elif user == "exit" :
        exit  
if __name__=="__main__":           
    TheRecursion()