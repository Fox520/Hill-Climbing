# Problem from https://www.cs.upc.edu/~bejar/ia/transpas/teoria.mti/2-BH3-Busqueda_local-eng.pdf
values = [8, 7, 12, 6, 2, 3]
weights = [5, 6, 10, 4, 1, 1]
ks_solution_weights = []
ks_solution_values = []
ks_max_weight = 16


def calculate_heuristic(arr):
    # Returns sum of values
    return sum(arr)


def get_ks_weight():
    return sum(ks_solution_weights)


for step in range(0, len(values)):
    current_heuristic = calculate_heuristic(ks_solution_values)
    heuristic_index = -1
    for j in range(0, len(values)):
        # Don't attempt on item which will make sack over limit weight if added
        if get_ks_weight() + weights[j] <= ks_max_weight:
            # Pretend to add item and get heuristic(value) with newly added item
            temp_sack = ks_solution_values.copy()
            temp_sack.append(values[j])

            temp_heuristic = calculate_heuristic(temp_sack)
            if temp_heuristic > current_heuristic:
                # New heuristic
                heuristic_index = j
                current_heuristic = temp_heuristic

    # Add item with highest heuristic in current iteration to sack
    if heuristic_index != -1:
        # Remove from values and weights from array to avoid duplicate processing in next iteration
        ks_solution_weights.append(weights.pop(heuristic_index))
        ks_solution_values.append(values.pop(heuristic_index))
        print(
            "Step =>",
            step,
            "Current heuristic =>",
            calculate_heuristic(ks_solution_values),
            "Sack weight =>",
            get_ks_weight(),
        )


print("Weights:", ks_solution_weights)
print("Values:", ks_solution_values)
