import time

def knapsack_brute_force(W, m, weights, values, classes):
    n = len(weights)
    max_value = 0
    best_combination = []
    
    for i in range(1, m+1):
        if i not in classes:
            return "At least one item is missing from class " + str(i)
    
    for i in range(2**n):
        combination = format(i, '0' + str(n) + 'b')
        current_weight = 0
        current_value = 0
        class_counter = [0] * m
        
        for j in range(n):
            if combination[j] == '1':
                current_weight += weights[j]
                current_value += values[j]
                class_counter[classes[j]-1] += 1
                
        if current_weight <= W and all(count > 0 for count in class_counter):
            if current_value > max_value:
                max_value = current_value
                best_combination = list(combination)
    
    return max_value, best_combination


# Read input from file
def read_input(file_path):
    with open(file_path, 'r') as file:
        W = int(file.readline().strip())
        m = int(file.readline().strip())
        weights = list(map(float, file.readline().strip().split(', '))) #input file
        values = list(map(int, file.readline().strip().split(', ')))
        classes = list(map(int, file.readline().strip().split(', ')))
        
    return W, m, weights, values, classes


# Write output to file
def write_output(file_path, max_value, best_combination, is_skipped=False):
    with open(file_path, 'w') as file:
        if is_skipped:
            file.write("TLE")
        else:
            file.write(str(max_value) + '\n') #end line
            file.write(', '.join(best_combination))


# Main function
def main():
    for i in range(10):
        input_file = f'input{i}.txt'
        output_file = f'output{i}.txt'
        output_file_skipped = f'output{i}_skipped.txt'  # For skipped cases
        
        W, m, weights, values, classes = read_input(input_file)
        
        if len(values) > 20:
            print(f"Skipping {input_file} as the number of values (n={len(values)}) is greater than 20.")
            write_output(output_file_skipped, 0, [], is_skipped=True)
            continue

        start_time = time.time()
        max_value, best_combination = knapsack_brute_force(W, m, weights, values, classes)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        write_output(output_file, max_value, best_combination)
        
        print(f"Execution time for {input_file}: {execution_time} milliseconds")

main()
