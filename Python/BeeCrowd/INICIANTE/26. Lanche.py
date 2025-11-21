codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)

while codigo < 0 or codigo > 5:
    codigo, quantidade = input().split()
    codigo = int(codigo)
    quantidade = int(quantidade)

match codigo:
    case 1:
        print(f"Total: R$ {quantidade*4.00:.2f}")
    case 2:
        print(f"Total: R$ {quantidade*4.50:.2f}")
    case 3:
        print(f"Total: R$ {quantidade*5.00:.2f}")
    case 4:
        print(f"Total: R$ {quantidade*2.00:.2f}")
    case 5:
        print(f"Total: R$ {quantidade*1.50:.2f}")
