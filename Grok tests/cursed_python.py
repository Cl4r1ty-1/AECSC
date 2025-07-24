def a(): {
(b := "hello"),
print(b)
}
    
a()

def c(): (b:="hellO"), print(b)

c()

def d():
    global b
    b = False
    if b:
        return False
    else:
        return (b := "what")
    
e = d()
print(e)
print(b)