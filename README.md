# [🗺️ Range Detective: Discover the Hidden Number Streaks! 🔍✨](https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150)
You are given a **sorted array of unique integers 🔢**. Think of this array as a collection of hidden number trails 🛤️ where some numbers may be standing together in a **continuous sequence 📈**.

Your task is to uncover these consecutive streaks 🔥 and represent them as the ***smallest possible list of ranges 📋***. Each range should describe a group of numbers that appear one after another without any gaps.

A range **`[a, b]`** represents **all integers from `a` to `b` (inclusive) 🧮**. Your final answer should cover every number in the array **exactly once** ✅.

#### ⚡ Rules of the Range Map:
- 🧩 Every number from **`nums`** must belong to **one and only one range**.
- 🚫 A range must not contain any number that is missing from the original array.
- 📉 The ranges must be returned in the same sorted order as the original array.
- ✂️ The goal is to create the **smallest number of ranges possible** by merging consecutive numbers together.

#### ✨ Range Formatting Rules:
For every discovered range:
- 🔗 If the range contains multiple consecutive numbers, represent it as:
**`"start->end"`**, eg: **`[3,4,5,6]`** becomes **`"3->6"`**

- 🎯 If the range contains only a single number, represent it as: **`"number"`**, eg **`[8]`** becomes **`"8"`**

### 🌟 Examples
- **🟢 Example 1: Compressing Multiple Consecutive Streaks 🚀** 
    ```
    Input: [0,1,2,4,5,7]
    Output: `["0->2","4->5","7"]
    ```
    **🔍 Explanation:**
    The array contains three hidden streaks:
    - **🚀 `[0,1,2]`** → a continuous number chain → **`"0->2"`**
    - **🔗 `[4,5]`** → another consecutive pair → **`"4->5"`**
    - **🎯 `[7]`** → a standalone number → **`"7"`**
    
    The final compressed range map is: **`["0->2", "4->5", "7"]`**

- **🔵 Example 2: Handling Gaps Between Number Trails 🌉**
    ```
    Input: [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    ```
    **🔍 Explanation:** The numbers split into multiple groups because of missing values:
    - **🎯 `[0]`** → isolated number → **`"0"`**
    - **🚀 `[2,3,4]`** → consecutive sequence → **`"2->4"`**
    - **🎯 `[6]`** → isolated number → **`"6"`**
    - **🔗 `[8,9]`** → consecutive pair → **`"8->9"`**
    
    The final compressed range map becomes: **`["0", "2->4", "6", "8->9"]`**

### 📜 Constraints
- 📏 **`0 <= nums.length <= 20`**
    → The array can be empty or contain up to 20 numbers.
- 🔢 **`-2³¹ <= nums[i] <= 2³¹ - 1`** → Numbers can be very small or very large integers.
- 🧬 All values of **`nums`** are unique → No duplicate numbers will appear.
- 📈 **`nums`** is sorted in ascending order → Numbers are already arranged from smallest to largest.

### 🏆 Challenge
Become the **Range Detective 🕵️‍♂️** and transform a scattered collection of numbers into the most compact range map 🗺️. Find all hidden consecutive streaks 🔥, merge them into meaningful ranges 🔗, and create the cleanest representation possible ✨.

---
### 🗺️ Solution Explanation: Single Pass Range Compression 🚀
#### 💡 Intuition
Since the given array **`nums`** is already ***sorted in ascending order*** 📈 and contains ***unique values*** 🔢, all consecutive numbers will naturally appear next to each other.

Instead of checking every possible range, we can scan the array once and build ranges as we go:
- 🎯 Start a new range from the current number.
- 🔗 Keep extending the range while the next number is exactly **`previous + 1`**.
- 🏷️ Once the consecutive sequence breaks, store the range.
- 🚶 Continue from the next unexplored number.

This allows us to compress the array into the ***smallest possible list of ranges*** efficiently.

#### 🪜 Steps
1. 📋 Create an empty list to store the summarized ranges.
2. 🚶 Traverse the array using a pointer:
    - Treat the current number as the start of a new range.
    - Initialize the end of the range with the same number.
3. 🔍 Check the following numbers:
    - If the next number is consecutive, extend the current range.
    - Continue until a gap is found.
4. 🏷️ Format the discovered range:
    - If start and end are the same:
        - Add **`"number"`**
    - Otherwise:
        - Add **`"start->end"`**
5. 🔄 Move the pointer to the first number after the current range.
6. ✅ Return the list of compressed ranges.

#### 📝 Pseudocode
```
function summaryRanges(nums):

    create empty list summarized_ranges

    set current_position = 0

    while current_position < length(nums):

        range_start = nums[current_position]
        range_end = range_start

        next_position = current_position + 1

        while next_position < length(nums)
              AND nums[next_position] == range_end + 1:

            range_end = nums[next_position]
            next_position += 1

        if range_start == range_end:
            add range_start to summarized_ranges
        else:
            add range_start + "->" + range_end to summarized_ranges

        current_position = next_position

    return summarized_ranges
```

#### ⏱️ Time Complexity `O(n)` 🚀
- Each number is visited only once.
- The inner loop does not restart from the beginning; it only moves forward.
- Total operations are proportional to the size of the array.

#### 💾 Space Complexity 
- **`O(1)` 🪶 (excluding output)**
    - Only a few variables are used:
        - **`range_start`**
        - **`range_end`**
        - **`current_position`**
        - **`next_position`**

- The output list requires: **`O(k)` 📦**, where **`k`** is the number of generated ranges.

#### 🏆 Why This Approach Is Optimal?
✅ Uses the sorted property of the input <br>
✅ Processes each element only once <br>
✅ Avoids unnecessary searching or extra data structures <br>
✅ Achieves the best possible time complexity: O(n) 🔥 <br>

---