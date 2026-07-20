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