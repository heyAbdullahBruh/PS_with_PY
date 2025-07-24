# Problem-22 ---> Pattern Printing ( tringle and dimond) -->
# Tringle
def tringlePattern(t):
    for r in range(1,t+1):
        print((2*r-1)*'*')
tringlePattern(10) 

# diamond
def diamondPattern(t):
    for r in range(1,t+1):
        print((2*r-1)*'*')
    for r in reversed(range(1,t+1)):
        print((2*r-1)*'* ')
diamondPattern(10) 
