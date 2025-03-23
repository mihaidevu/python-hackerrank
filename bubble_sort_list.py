students = ['John', 'Lisa', 'Mary', 'Chris', 'Linda', 'Matt']
test_performance = {
    'John': 87,
    'Lisa': 90,
    'Mary': 75,
    'Chris': 100,
    'Linda': 100,
    'Matt': 70	
}

scores = []

for key in test_performance:
    scores.append(test_performance[key])
    
def bubble_sort(scores):
    n = len(scores)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            if scores[i] > scores[i + 1]:
                scores[i], scores[i + 1] = scores[i + 1], scores[i]
                swapped = True 
        if not swapped:
            break
    return scores

sorted_scores = bubble_sort(scores)
print(sorted_scores)    # Expected output: [70, 75, 87, 90, 100, 100]

highest_score = sorted_scores[-1]
lowest_score = sorted_scores[0]

def average_class_score(scores):
    try:
        if not scores:
            raise ValueError("The score list is empty. Cannot calculate average.")
        return sum(scores) / len(scores)
    except ValueError as e:
        return str(e)
    
average_class_score = average_class_score(scores)
print(average_class_score) # Expected output: 87.0