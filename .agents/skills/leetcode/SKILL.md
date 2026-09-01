---
name: leetcode
description: "Automate the setup of a new LeetCode problem workspace: create the directory, initialize main.py with the commented-out description, paste the template code, add typing imports, and generate run_main tests from the examples. Maintains a strict educational/learning policy (no code fixes or suggestions)."
---

## Overview

Use this skill when the user wants to start or work on a LeetCode problem (e.g. when they specify a LeetCode title, number, or want to import a new problem).

## Step-by-Step Workflow

1. **Convert the Title to a Directory Name**:
   - Take the LeetCode title provided by the user (e.g., "518. Coin Change II").
   - Convert it to a slugified directory name: lowercase, replace spaces/punctuation/periods with hyphens, collapse multiple hyphens, and remove leading/trailing hyphens.
     - Example: "518. Coin Change II" -> "518-coin-change-ii"
     - Example: "1. Two Sum" -> "1-two-sum"
   - Create this directory within the user's LeetCode project workspace directory (typically `/Users/bobhoskins/projects/leetcode/`).

2. **Retrieve the Problem Details**:
   - The user only needs to provide the problem title (e.g., "1448. Count Good Nodes in Binary Tree") or the LeetCode URL (e.g., `https://leetcode.com/problems/count-good-nodes-in-binary-tree/description`).
   - Use web search to fetch the problem description, examples, and function signature/code template.
   - If you are blocked from the website or unable to find the details, ask the user to paste the problem description and code template as a backup.

3. **Initialize `main.py`**:
   - Create `main.py` in the new directory.
   - At the top of `main.py`, paste the problem description, ensuring that every line of the description is commented out using `# `.
   - Include any necessary imports at the top of the file based on the types and structures used in the code template (e.g., `from typing import List, Optional, Dict`, `from collections import deque`).
   - Add the template code directly below the imports without changing any of the code.

4. **Extract and Setup Test Cases**:
   - Parse the Examples in the problem description to extract test inputs and expected outputs.
   - Append a `if __name__ == "__main__":` block at the end of `main.py`.
   - Inside this block, write code that:
     - Instantiates the solution class (e.g., `sol = Solution()`).
     - Calls the solution method with the parsed input parameters for each example.
     - Prints the input, the output, and the expected output.
     - Uses `assert` to verify that the output matches the expected output.
     - Prints a success message (e.g. `All tests passed!`) if all assertions pass.

5. **Run the Tests**:
   - Proactively execute the code (e.g. `python3 <dir>/main.py`) to verify it runs and show the user the output.

## Strict Learning Policy

Since the user is learning to solve the problems:
- **NEVER** edit the user's implementation code or suggest optimizations/corrections.
- **NEVER** solve the problem for the user or provide code hints for the solution itself.
- Only modify `main.py` to add imports, the description comments, or update the test harness.

## Python notes

Unless specified the user will be working in Python3

Ensure there are two lines before the main block...

``` python3
if __name__ == "__main__":
```

Be careful not to use f strings when there are no placeholders.


