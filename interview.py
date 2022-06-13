'''
Your colleague has recently started ice-skating, and after an injury, has become obsessed with padding his clothes in order to prevent future injuries. His padding obsession has become so severe, that all the documents you write together must also be padded. 

For every sentence, each word must be padded with enough spaces on each side, that each word has the same amount of characters as the longest word in that sentence.

e.g.

input:  'let's pad this sentence'
output: '  let's    pad    this  sentence'
'''

def padD(str):
    pad = str.split(" ")

    maxelement = max(pad, key=len)

    for i in range(len(pad)):
        # while len(pad[i]) < len(maxelement):
        num_spaces = len(maxelement)-len(pad[i])
        #new_str = pad[i] + " "*num_spaces

        # print(new_str) 
        if num_spaces%2==0:
            new_str = " "*int(num_spaces//2) + pad[i] + " "*int(num_spaces//2)
            
        else:
            rem_num = num_spaces//2 - (1)
            new_str = " "*int(num_spaces//2) + pad[i] + " "*int(rem_num)
    print(new_str)
    

l = "abd abcdef"
padD(l)