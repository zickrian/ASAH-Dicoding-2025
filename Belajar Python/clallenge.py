#buatlah string yang menampung angka 0 - 500 (hanya angka genap saja)

varr = [i for i in range(501) if i %2 == 0]
print(varr)

var = []
for i in range(501):
    if i % 2 == 0:
        var.append(i)


print(var)