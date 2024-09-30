a = input()
b = int(input())
num = len(a)
result = ""  

for i in range(num):
    ascii_value = ord(a[i])
    operator = [".","!","?",","]
    if a[i] in operator:
        result += a[i]
        continue
    
    else:
        ascii_value_plus = ascii_value + b
        
        if ascii_value_plus > 124:
            ascii_value_plus = 0
            ascii_value_plus += ascii_value_plus + b
            
        else:
            result += chr(ascii_value_plus)  
    
    
print(result)