class Item:
    def __init__(self, benefit, weight):
        self.benefit = benefit
        self.weight = weight
        self.benefit_to_weight_ratio = benefit / weight

    def __lt__(self, other):
        return self.benefit_to_weight_ratio < other.benefit_to_weight_ratio

def fractional_knapsack(items, capacity):
    # Sort items based on benefit-to-weight ratio in descending order
    items.sort(reverse=True)
    
    total_benefit = 0
    remaining_capacity = capacity
    
    for item in items:
        if remaining_capacity >= item.weight:
            # Take the whole item
            total_benefit += item.benefit
            remaining_capacity -= item.weight
        else:
            # Take a fraction of the item
            fraction = remaining_capacity / item.weight
            total_benefit += fraction * item.benefit
            break  # Knapsack is full
        
    return total_benefit

def max_sum_array(arr):
    # Enumerate the array to get (value, index) pairs
    arr_with_indices = [(val, idx) for idx, val in enumerate(arr)]
    
    # Sort the array with indices in non-decreasing order of values
    arr_with_indices.sort()
    
    # Rearrange the array to maximize the sum of arr[i] * i
    max_sum_arr = [val for val, _ in arr_with_indices[::-1]]
    
    return max_sum_arr


def min_product_sum(array_One, array_Two):
    # Sort both arrays
    array_One.sort()
    array_Two.sort(reverse=True)  # Sort array_Two in descending order
    
    # Calculate the minimum sum of the product of pairs
    min_sum = sum(array_One[i] * array_Two[i] for i in range(len(array_One)))
    return min_sum

# Example usage for each problem

# 1. Fractional Knapsack Problem
items = [
    Item(benefit=60, weight=10),
    Item(benefit=100, weight=20),
    Item(benefit=120, weight=30)
]
capacity = 50
optimal_solution = fractional_knapsack(items, capacity)
print("1. Optimal solution (fractional knapsack):", optimal_solution)

# 2. Maximize sum of arr[i] * i
arr = [2, 5, 3, 4, 0]
max_sum_arr = max_sum_array(arr)
print("Maximized sum array:", max_sum_arr)

# Calculate the sum of arr[i] * i for the maximized sum array
max_sum_value = sum(val * idx for idx, val in enumerate(max_sum_arr))
print("Maximized sum:", max_sum_value)

# 3. Minimum sum of product of pairs
array_One = [7, 5, 1, 4]
array_Two = [6, 17, 9, 3]
min_product = min_product_sum(array_One, array_Two)
print("3. Minimum sum of product of pairs:", min_product)
