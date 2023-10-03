def merge_intervals(interval_lst):
    if not interval_lst:
        return []

    # Sort the intervals based on their start times
    interval_lst.sort(key=lambda x: x[0])

    merged_intervals = [interval_lst[0]]

    for interval in interval_lst[1:]:
        current_start, current_end = interval
        last_merged_start, last_merged_end = merged_intervals[-1]

        if current_start <= last_merged_end:
            # There is an overlap; merge the intervals
            merged_intervals[-1] = [last_merged_start, max(last_merged_end, current_end)]
        else:
            # No overlap; add the current interval to the merged list
            merged_intervals.append(interval)

    return merged_intervals

# Sample Input
interval_lst = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

# Call the function and print the result
merged_intervals = merge_intervals(interval_lst)
print(merged_intervals)
