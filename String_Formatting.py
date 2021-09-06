def print_formatted(n):
    results = []
for i in range(1, n+1):
    decimal = str(i)
    octal = str(oct(i)[2:])
    hex_ = str(hex(i)[2:]).upper()
    binary = str(bin(i)[2:])
    results.append([decimal, octal, hex_, binary])
width = len(results[-1][3]) 
for i in results:
    print(*(rep.rjust(width) for rep in i))