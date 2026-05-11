def even_odd_swap(x):
    if len(x)%2!=0:
        x = x + ' '

    even_letters = x[0::2]
    odd_letters  = x[1::2]
    s=''

    for i in range(len(even_letters)):
        s = s+odd_letters[i]
        s = s+even_letters[i]
    
    return s

def swap_middle(x):
    if len(x)%2!=0:
        x = x + ' '

    first_half = x[0:int(len(x)/2):1]
    second_half = x[int(len(x)/2)::1]
    
    s = ''
    s = s + second_half 
    s = s + first_half
    return s
    
def reverse(x):
    s = x[::-1]
    return s

def swap_mid_rev(x):
    s_swap = swap_middle(x)
    s = reverse(s_swap)
    return s

def swap_mid_rev_decode(x):
    s_rev = reverse(x)
    s = swap_middle(s_rev)
    return s

def reverse_word(x):
    words = x.split(' ')
    s = ''
    for kk in range(len(words)):
        s = s+reverse(words[kk])+' '
    return s

x = 'hold your horses'
#print(x)
x_even_odd = even_odd_swap(x)
print(x_even_odd)

input()

x_rev = reverse(x)
print(x_rev)
input()
x_rev_word = reverse_word(x)
print(x_rev_word)

input()

x_swap_mid = swap_middle(x)
print(x_swap_mid)

input()
x_swap_mid_rev = swap_mid_rev(x)
print(x_swap_mid_rev)
input()
print()

print(even_odd_swap(x_even_odd))
print(reverse(x_rev))
print(reverse_word(x_rev_word))
print()

