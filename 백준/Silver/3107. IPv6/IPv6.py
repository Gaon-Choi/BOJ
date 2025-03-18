ipv6 = input()

colon_before = ""
colon_after = ""

if "::" in ipv6:
    colon_before, colon_after = ipv6.split("::")
    
    colon_before_list = list(filter(lambda x : x != "", colon_before.split(":"), ))
    colon_after_list = list(filter(lambda x : x != "", colon_after.split(":"), ))
else:
    colon_before_list = list(filter(lambda x : x != "", ipv6.split(":"), ))
    colon_after_list = []

result = []

for elem in colon_before_list:
    result.append(elem.rjust(4, '0'))
    
for _ in range(8 - len(colon_before_list) - len(colon_after_list)):
    result.append("".rjust(4, '0'))
    
for elem in colon_after_list:
    result.append(elem.rjust(4, '0'))
    
print(':'.join(result))