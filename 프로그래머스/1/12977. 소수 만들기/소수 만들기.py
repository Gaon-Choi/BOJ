def solution(nums):
    answer = 0

    nums.sort()
    
    max_ = nums[-1] + nums[-2] + nums[-3]
    
    is_prime = [True] * (max_ + 1)
    
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, max_):
        if is_prime[i]:
            for n in range(i * 2, max_ + 1, i):
                is_prime[n] = False
                
    size = len(nums)
                
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                if is_prime[nums[i] + nums[j] + nums[k]]:
                    answer += 1

    return answer