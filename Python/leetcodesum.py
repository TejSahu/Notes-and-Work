# nums = [2, 11, 7, 15]
# target = 9
#
# for idx, val in enumerate(nums):
#     if target - val in nums[idx + 1:]:
#         print([idx, nums[idx + 1:].index(target - val) + (idx + 1)])

"""Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure
your result is the smallest in lexicographical order among all possible results."""

sample = "stromatolites"
sample = set(sample)
