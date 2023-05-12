with open('text', 'r') as f:
    for i in f:
        parts = i.strip().split(';')
        nums = list(map(int, parts[0].split()))
        right_side = list(map(int, parts[1].split()))
        if sum(nums) // len(nums) == right_side[0] and sum(nums) % len(nums) == right_side[1]:
            print('True')
        else:
            print('False')