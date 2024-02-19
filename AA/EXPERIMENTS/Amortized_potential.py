doubling_costs = []
current_length = 1
potential = []

for i in range(1, 11):
    if current_length < i:
        current_length *= 2
        doubling_costs.append(i-1)
    else:
        doubling_costs.append(0)
    potential.append(2*i- current_length)

total_cost = [x+1 for x in doubling_costs]
print('Doubling Cost\t Iteration\t Total Cost\t Potential\tAmortized Cost')

print(f'{doubling_costs[0]}\t\t {1}\t\t {total_cost[0]}\t\t{potential[0]}\t\t {total_cost[0] + potential[0]}')

for j in range(1, 10):
    amortized_cost = total_cost[j] + potential[j]- potential[j-1]
    print(f'{doubling_costs[j]}\t\t {1}\t\t {total_cost[j]}\t\t{potential[j]}\t\t {amortized_cost}')