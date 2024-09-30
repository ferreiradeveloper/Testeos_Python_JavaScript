a = {1,2,3,4}
b = {4,5,6,7}

print(a&b) # intercepción
print(a-b) # elementos unicos de b
print(b-a) # elementos unicos de a
print(a^b) # diferencia simetrica

print(a.symmetric_difference(b))
print(a.intersection(b))
