"""Write a program to implement first-fit, best-fit and worst-fit allocation strategies."""

def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    
    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break
    return allocation

def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    
    for i in range(len(processes)):
        best_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_idx == -1 or blocks[best_idx] > blocks[j]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= processes[i]
    return allocation

def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    
    for i in range(len(processes)):
        worst_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_idx == -1 or blocks[worst_idx] < blocks[j]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= processes[i]
    return allocation

# Example usage:
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

print("First-Fit Allocation:", first_fit(blocks.copy(), processes))
print("Best-Fit Allocation:", best_fit(blocks.copy(), processes))
print("Worst-Fit Allocation:", worst_fit(blocks.copy(), processes))
