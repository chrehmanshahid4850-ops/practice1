marks = [88, 45, 92, 67, 30, 75]

passed = sum(1 for mark in marks if mark >= 50)
average = sum(marks) / len(marks)

highest = max(marks)
lowest = min(marks)

print(f"Passed: {passed}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest} Lowest: {lowest}")