ENCRYPTED_TEXT = 'PBFPVYFBQXZTYFPBFEQJHDXXQVAPTPQJKTOYQWIPBVWLXTOXBTFXQWAXBVCXQWAXFQJVWLEQNTOZQGGQLFXQWAKVWLXQWAEBIPBFXFQVXGTVJVWLBTPQWAEBFPBFHCVLXBQUFEVWLXGDPEQVPQGVPPBFTIXBVFOJIWFFACFCCFHQWAUVWFLQHGFXVAFXQHFUFHILTTAVWAFFAWTEVOITDHFHFQAITIXPFHXAFQHEFZQWGFLVWPTOFFA'

plain_text = ''
eng_list = ['E','A','R','I','O','T','N','S','L','C','U','D','P','M','H','G','B','F','Y','W','K','V','X','Z','J','Q'] 

encrypt_list = []
freq_count = {}
final_list = {}

lst = [
    [15,'A'],
    [14,'B'],
    [5, 'C'],
    [3,'D'],
    [8,'E'],
    [33,'F'],
    [7,'G'],
    [10,'H'],
    [10,'I'],
    [5,'J'],
    [2,'K'],
    [10,'L'],
    [0,'M'],
    [1,'N'],
    [6,'O'],
    [15,'P'],
    [24,'Q'],
    [0,'R'],
    [0,'S'],
    [8,'T'],
    [3,'U'],
    [19,'V'],
    [18,'W'],
    [20,'X'],
    [3,'Y'],
    [3,'Z']
    ]
    
lst = sorted(lst, reverse=True)


for i in lst:
    encrypt_list.append(i[1])

for i in range(len(encrypt_list)):
    final_list[encrypt_list[i]] = eng_list[i]
    

for i in ENCRYPTED_TEXT:
    if i not in freq_count:
        freq_count[i] = 1
    else:
        freq_count[i] += 1
print(sorted(freq_count))


for i in ENCRYPTED_TEXT:
    plain_text += final_list[i]

print(plain_text)