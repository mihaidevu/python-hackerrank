# def swap_case(s):
#     swapped = []
#     for char in s:
#         if char.islower():
#             swapped.append(char.upper()) # Transformă în mare
#         elif char.isupper():
#             swapped.append(char.lower()) # Transformă în mică
#         else:
#             swapped.append(char)         # Păstrează cifrele/simbolurile așa cum sunt
            
#     return "".join(swapped) # Transformă lista înapoi în string

#Ambele au complexitate temporală 
# dar List Comprehension evită overhead-ul apelării metodei .append() la fiecare iterație, fiind optimizat la nivel de interpretor."

def swap_case(s):
    return "".join(char.lower() if char.isupper() else char.upper() for char in s)
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)