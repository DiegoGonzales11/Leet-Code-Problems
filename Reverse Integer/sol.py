def reverse(self, x):
    x_lst = list(str(x))
    signed = False
    if x_lst[0] == '-':
        x_lst = x_lst[1:]
        signed = True
        
    x_lst.reverse()
    if signed == True:
        x_lst.insert(0,'-')            
        
    x_str = ''
    for char in x_lst:
        x_str += char
        
    return int(x_str)

