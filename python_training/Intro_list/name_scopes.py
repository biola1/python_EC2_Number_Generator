def show_truth():
    mystery_var = 'smiling!'
    print(mystery_var)
show_truth()

def show_truth():
    global mystery_var
    mystery_var = 'smiling!'
    print (mystery_var)
mystery_var = 'new smiling'
print(mystery_var)
show_truth()