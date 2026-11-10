# Number Analyzer & Sorting System

A beginner-friendly Python project that analyzes a list of numbers and sorts them.

## Features

- Find the largest number
- Find the smallest number
- Find the second-largest **distinct** number
- Sort numbers in ascending order
- Sort numbers in descending order
- Validate user input
- Uses Bubble Sort implemented manually (no `sort()` or `sorted()`)

## Requirements

- Python 3.8 or newer
- No third-party packages required

## Run the project

```bash
python main.py
```

Enter numbers separated by spaces when prompted.

## Example

```text
Enter numbers separated by spaces: 45 12 89 23 67

Original numbers : [45.0, 12.0, 89.0, 23.0, 67.0]
Largest number   : 89.0
Smallest number  : 12.0
Second largest   : 67.0
Ascending order  : [12.0, 23.0, 45.0, 67.0, 89.0]
Descending order : [89.0, 67.0, 45.0, 23.0, 12.0]
```

## Algorithm

Bubble Sort repeatedly compares adjacent values and swaps them when they are in the wrong order.

- Time complexity: O(n²) average and worst case
- Best case: O(n) when the list is already sorted, due to early stopping
- Extra space: O(n) for the copied result list

## Project structure

```text
number-analyzer/
├── main.py
├── README.md
└── .gitignore
```

## GitHub upload

Create a public repository named `number-analyzer`, then run these commands inside this folder:

```bash
git init
git add .
git commit -m "Add number analyzer and bubble sort project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/number-analyzer.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Author

Add your name here.
