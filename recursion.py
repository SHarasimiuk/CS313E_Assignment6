"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Sebastian Harasimiuk, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: sph974
"""


def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0

    if group_sum(start + 1, nums, target - nums[start]):
        return True
    return group_sum(start + 1, nums, target)


def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0

    if group_sum_6(start + 1, nums, target - nums[start]):
        return True
    if nums[start] != 6:
        return group_sum_6(start + 1, nums, target)
    return False


def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0

    if group_no_adj(start + 2, nums, target - nums[start]):
        return True
    elif group_no_adj(start + 2, nums, target):
        return True
    elif start < len(nums) - 1:
        start += 1
        if group_no_adj(start + 2, nums, target - nums[start]):
            return True
        return group_no_adj(start + 2, nums, target)
    return False


def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0

    if nums[start] == 1 and nums[start - 1] % 5 == 0:
        return group_sum_5(start + 1, nums, target)
    if group_sum_5(start + 1, nums, target - nums[start]):
        return True
    if nums[start] % 5 != 0:
        return group_sum_5(start + 1, nums, target)
    return False


def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0

    value = None
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            value = nums[i]
        elif i < len(nums) - 1 and nums[i] == nums[i + 1]:
            value = nums[i]

    if group_sum_clump(start + 1, nums, target - nums[start]):
        return True
    if nums[start] != value:
        return group_sum_clump(start + 1, nums, target)
    return False


def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def split_array_helper(nums, i, res, sol):
        if i == len(nums):
            res.append(sol[:])
            return

        for j in range(i, len(nums)):
            sol[i], sol[j] = sol[j], sol[i]
            split_array_helper(nums, i + 1, res, sol)
            sol[i], sol[j] = sol[j], sol[i]

    res = []
    sol = nums[:]
    split_array_helper(nums, 0, res, sol)

    for elem in res:
        mid = len(elem) // 2
        left_sum = 0
        right_sum = 0

        for num in elem[:mid]:
            left_sum += num
        for num in elem[mid:]:
            right_sum += num

        if left_sum == right_sum:
            return True
    return False


def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def split_odd_10_helper(nums, i, res, sol):
        if i == len(nums):
            res.append(sol[:])
            return

        for j in range(i, len(nums)):
            sol[i], sol[j] = sol[j], sol[i]
            split_odd_10_helper(nums, i + 1, res, sol)
            sol[i], sol[j] = sol[j], sol[i]

    res = []
    sol = nums[:]
    split_odd_10_helper(nums, 0, res, sol)

    for elem in res:
        mid = len(elem) // 2
        left_sum = 0
        right_sum = 0

        for num in elem[:mid]:
            left_sum += num
        for num in elem[mid:]:
            right_sum += num

        if left_sum % 2 != 0 and right_sum % 10 == 0:
            return True
        if right_sum % 2 != 0 and left_sum % 10 == 0:
            return True
    return False


def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def split_53_helper(nums, i, res, sol):
        if i == len(nums):
            res.append(sol[:])
            return

        for j in range(i, len(nums)):
            sol[i], sol[j] = sol[j], sol[i]
            split_53_helper(nums, i + 1, res, sol)
            sol[i], sol[j] = sol[j], sol[i]

    res = []
    sol = nums[:]
    split_53_helper(nums, 0, res, sol)

    for elem in res:
        if len(elem) > 0:
            mid = len(elem) // 2
            left_sum = 0
            right_sum = 0
            left_5_count = 0
            left_3_count = 0
            right_5_count = 0
            right_3_count = 0

            for num in elem[:mid]:
                left_sum += num
                if num % 5 == 0:
                    left_5_count += 1
                elif num % 3 == 0:
                    left_3_count += 1
            for num in elem[mid:]:
                right_sum += num
                if num % 5 == 0:
                    right_5_count += 1
                elif num % 3 == 0:
                    right_3_count += 1

            if left_5_count != 0 and left_3_count == 0 and right_5_count == 0 and right_3_count != 0 and left_sum == right_sum:
                return True
            if left_5_count == 0 and left_3_count != 0 and right_5_count != 0 and right_3_count == 0 and left_sum == right_sum:
                return True
            if left_5_count != 0 and left_3_count == 0 and right_5_count == 0 and right_3_count == 0 and left_sum == right_sum:
                return True
            if left_5_count == 0 and left_3_count != 0 and right_5_count == 0 and right_3_count == 0 and left_sum == right_sum:
                return True
            if left_5_count == 0 and left_3_count == 0 and right_5_count != 0 and right_3_count == 0 and left_sum == right_sum:
                return True
            if left_5_count == 0 and left_3_count == 0 and right_5_count == 0 and right_3_count != 0 and left_sum == right_sum:
                return True
            if left_5_count == 0 and left_3_count == 0 and right_5_count == 0 and right_3_count == 0 and left_sum == right_sum:
                return True
    return False
