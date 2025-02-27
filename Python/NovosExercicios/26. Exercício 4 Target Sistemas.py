faturamento_SP = 67836.43
faturamento_RJ = 36678.66
faturamento_MG = 29229.88
faturamento_ES = 27165.48
faturamento_OUTROS = 19849.53

soma_total = faturamento_SP + faturamento_RJ + faturamento_MG + faturamento_ES + faturamento_OUTROS

print(f"Faturamento_SP: {((faturamento_SP * 100) / soma_total):.2f}%")
print(f"Faturamento_RJ: {((faturamento_RJ * 100) / soma_total):.2f}%")
print(f"Faturamento_MG: {((faturamento_MG * 100) / soma_total):.2f}%")
print(f"Faturamento_ES: {((faturamento_ES * 100) / soma_total):.2f}%")
print(f"Faturamento_OUTROS: {((faturamento_OUTROS * 100) / soma_total):.2f}%")
