from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 📋 Stores the final compressed list of ranges
        summarized_ranges: List[str] = []

        # 🔢 Pointer to track the current position in the array
        current_position: int = 0
        total_numbers: int = len(nums)

        # 🚶 Traverse through the sorted numbers
        while current_position < total_numbers:
            # 🎯 The current number starts a new range
            range_start: int = nums[current_position]
            range_end: int = range_start

            # ➡️ Start checking the next number for consecutive sequence
            next_position: int = current_position + 1
            expected_next_number: int = range_start + 1

            # 🔍 Expand the range while consecutive numbers are found
            # Example: [1,2,3] becomes "1->3"
            while (
                next_position < total_numbers 
                and nums[next_position] == expected_next_number
            ):
                # 🔗 Extend the current range endpoint
                range_end = expected_next_number

                # 🚀 Move forward to check the next consecutive number
                next_position += 1
                expected_next_number += 1

            # 🏷️ Format the range based on its length:
            # 🎯 Single number  -> "number"
            # 🔗 Multiple numbers -> "start->end"
            if range_start == range_end:
                summarized_ranges.append(str(range_start))
            else:
                summarized_ranges.append(f"{range_start}->{range_end}")

            # 🔄 Continue processing from the next unvisited number
            current_position = next_position

        # ✅ Return the smallest list of sorted ranges
        return summarized_ranges
