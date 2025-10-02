num = int(input(": "))

num1 = int(input(": "))

nishani_nishnuri = input(": ")

if nishani_nishnuri == "+":
    print(num + num1)
elif nishani_nishnuri == "-":
    print(num - num1)
elif nishani_nishnuri == "/":
    print(num / num1)
elif nishani_nishnuri == "//":
    print(num // num1)
elif nishani_nishnuri == "*":
    print(num * num1)
elif nishani_nishnuri == "**":
    print(num ** num1)
elif nishani_nishnuri == "%":
    print(num % num1)
else:
    print("wrong operator")