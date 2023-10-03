# Write a function that takes in a non-empty array of arbitrary intervals,
 # merges any overlapping intervals, and returns the new intervals in no particular order.
 # Each interval interval is an array of two integers, with interval[0] as the start
 # of the interval and interval[1] as the end of the interval.
 # Note that back-to-back intervals aren't considered to be overlapping.
 # For example, [1,5] and [6,7] aren't overlapping; however, [1,6] and [6,7] are indeed overlapping.
 # Also note that the start of any particular interval will always be less than
 # or equal to the end of that interval.
 # Sample Input
 # intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
 # Sample Output
 # [[1, 2], [3, 8], [9, 10]]

interval_lst = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
print(interval_lst)
 
def overlapping_intervals(interval_lst):

    number_of_elements = len(interval_lst)
    number_of_times = number_of_elements -2
    
    id = 0
    counter = 0

    while counter < number_of_times:
        current_interval = interval_lst[id]
        next_interval = interval_lst[id +1]

        if current_interval[1] >= next_interval[0]:
            next_interval[0] = current_interval[0]
            interval_lst.remove(current_interval)
        else:
            id +=1

        counter +=1

    print(interval_lst)
    return interval_lst

overlapping_intervals(interval_lst)
