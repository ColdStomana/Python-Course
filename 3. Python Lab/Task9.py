dalgina = int (input())
shirina = int (input())
visocina = int (input())
procent = int (input())

obem=dalgina*shirina*visocina
obemlitri=obem*0.001
zaetoprostranstvo=0.17
litrinujni=obemlitri*(1-zaetoprostranstvo)

print(litrinujni)
