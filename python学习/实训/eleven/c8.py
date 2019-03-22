origin=0
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos=pos+step
        pos=new_pos
        return pos
    return go
    
tourist=factory(origin)
print(tourist(2),tourist(3),tourist(5))
print(origin)