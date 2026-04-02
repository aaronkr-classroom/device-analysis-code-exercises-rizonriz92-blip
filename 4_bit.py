# list
my_list1 = [1, 2, 'a', "Hello"]
my_list2 = [1, 'a', 3, 67]

my_list1[1] = 67
my_list2.append(89)  # asgnf

# tuple
my_t1 = ('Arnold', 1984)
my_t23 = (1991, 2003)

print(my_t23[0])  # my_t23[0] = 'Aaron'
my_t23 = (100, 1000)

# dictionary
my_dict = {
    "name": "Aaron",
    "list": my_list1,
    "tup": (1, 2, 3),
}

my_dict['tup'] = (1, 4, 5)
my_dict['name'] = "Brian"

# set
set1 = {1, 2, 'a', "Hello"}
set2 = {2, 3, 'b', "Hello"}

union_set = set1 | set2
intersection_set = set1 & set2
diff_set = set1 - set2
sym_diff_set = set1 ^ set2

print('u:', union_set)
print('i:', intersection_set)
print('d:', diff_set)
print('sd:', sym_diff_set)


# 4_math.py
# math

print(10 + 3)
print(10 - 3)
print(10 * 2)
print(10 / 3)
print(10 % 3)
print(10 // 3)  # FLOOR DIVISION
print(10 ** 3)  # EXPONENTIAL


a = 132
b = 45

fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'
n= 30
print("bitwise AND:")
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))
print('-'*n)
print(fmt0.format('a&b'), fmt1.format(a&b, a&b, a&b))


a = 132
b = 45

fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'
n= 30
print("bitwise OR:")
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))
print('-'*n)
print(fmt0.format('a|b'), fmt1.format(a|b, a|b, a|b))

##XOR
a = 132
b = 45

fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'
n= 30
print("bitwise XOR:")
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))
print('-'*n)
print(fmt0.format('a^b'), fmt1.format(a^b, a^b, a^b))

##NOT

a = 132
b = 45

fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'
n= 30
print("bitwise NOT:")
print(fmt0.format('a'), fmt1.format(a,a,a))

print('-'*n)
print(fmt0.format('~a'), fmt1.format(~a&0xff, ~a&0xFF, ~a&0xFF))

##LEFTSHIFT
a = 132
b = 45

fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'
n= 30
print("bitwise leftshift:")
print(fmt0.format('a'), fmt1.format(a,a,a))

print('-'*n)
print(fmt0.format('a<<2'), fmt1.format(a<<2&0xff, a<<2&0xff, a<<2&0xff))


##RIGHTSHIFT
a = 132
b = 45

fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'
n= 30
print("bitwise rightshift:")
print(fmt0.format('a'), fmt1.format(a,a,a))

print('-'*n)
print(fmt0.format('a>>2'), fmt1.format(a>>2&0xff, a>>2&0xff, a>>2&0xff))

