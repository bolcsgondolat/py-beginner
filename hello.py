def score_counter(score_list):
    negative_scores =0
    neutral_scores =0
    positive_scores =0
    
    for score in score_list:
        if score >=9:
            positive_scores +=1
        elif score >=6:
            neutral_scores +=1
        else:
            negative_scores +=1

    print('Negative: ' + str(negative_scores))
    print('Neutral: ' + str(neutral_scores))
    print('Positive: ' + str(positive_scores))

print("Hello Wolrd :)")

score_counter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

print("Bye :)")
