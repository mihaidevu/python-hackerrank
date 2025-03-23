def categorize_ratings(rating_list):
    number_of_low_ratings = 0
    number_of_medium_ratings = 0
    number_of_high_ratings = 0
    for i in rating_list:
        if i < 5:
            number_of_low_ratings += 1
            continue
        
        if i >= 5 and i <= 7:
            number_of_medium_ratings += 1
            continue
        
        if i > 7:  
            number_of_high_ratings += 1
            continue
        
    print("Low:", number_of_low_ratings)
    print("Medium:", number_of_medium_ratings)
    print("High:", number_of_high_ratings)
    
categorize_ratings([1, 3, 5, 7, 8, 9]) # Expected output: Low: 2, Medium: 2, High: 2