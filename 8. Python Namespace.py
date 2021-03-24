
import this

# Demo id is same
fish = 2
print("id(fish)=", id(fish))
print("id(2)=", id(2))

# Increment
print(id(fish))
fish = fish+1
print(id(fish))
print(id(3))

# Demo 3 instances of a:
def outer_fn():
    a = 20
    def inner_fn():
        a = 30
        print("a=", a)
    inner_fn()
    print("a=", a)
a = 10
outer_fn()
print("a=", a)

# Demo global usage of a:
def baz_outer():
    global z
    z = 30
    def baz_inner():
        global z
        z = 20
        print("z=", z)
    baz_inner()
    print("z=", z)
z = 10
baz_outer()
print("z=", z)

