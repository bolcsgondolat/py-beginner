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

score_counter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

# RUN THIS CELL TO TEST YOUR FUNCTION

import random
random.seed(42)

possible_scores = list(range(1,11))
score_list1 = random.choices(possible_scores, weights=[8,8,8,8,8,3,3,4,20,30], k=10)
score_list2 = random.choices(possible_scores, weights=[1,2,3,4,5,10,15,15,7,9], k=450)
score_list3 = random.choices(possible_scores, weights=[1,2,3,4,4,5,5,10,15,25], k=10000)

print('Test 1:')            # SHOULD OUTPUT (neg, neut, pos):
score_counter(score_list1)  # 5, 1, 4
print('\nTest 2:')
score_counter(score_list2)  # 85, 253, 112
print('\nTest 3:')
score_counter(score_list3)  # 1935, 2652, 5413