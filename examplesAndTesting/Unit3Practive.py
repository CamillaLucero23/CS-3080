def formattingNotes (a):
    print("------------------------------------------------------------------------------")
    print(a + "\n")

#Negative Indexs & Slicing
formattingNotes("Negative indexs & Slicing")
spam = ["hi","howdy", "ciao", "hola"]

print (spam[-1]) #print last item

print(spam[:2]) #slice up to index 2
print(spam[2:4]) #slice starting @ 2, up to 4

#----------------------------------------------------------------

#Concatenating Lists
formattingNotes("Concatenating Lists")

print("[1,2,3,] + ['A','B','C'] = ", [1,2,3,] + ['A','B','C'])

print("\nReplicate spam list 3 times: \n",  spam * 3)