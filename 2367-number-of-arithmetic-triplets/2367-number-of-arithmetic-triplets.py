

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        num_count = {}
        triplets_count = 0
        
        # Count the frequency of each number in nums
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        # Check for arithmetic triplets
        for num in nums:
            if num - diff in num_count and num + diff in num_count:
                triplets_count += 1
        
        return triplets_count

# Example usage:
solution = Solution()
nums = [1, 2, 3, 4, 5]
diff = 1
print(solution.arithmeticTriplets(nums, diff))  # Output: 4
