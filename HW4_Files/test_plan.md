# Test Plan for HW4
## 1. 'add' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
1 | Add two positive integers | 3,2 | 5 | 1 | Fail | The function is not adding the two integers, but rather subtracting them.
2 | Add 0 and a positive integer | 0, 5 | 5 | 5 | Pass | NA

## 2. 'subtract' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
1 | Subtract two positive integers | 5,3 | 2 | 8 | Failed | The function is not subtracting the two integers, but rather adding them.
2 | Subtract 0 and a positive integer | 0, 5 | -5 | -5 | Pass | NA

## 3. 'divide' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
1 | Divide two positive integers | 6,2 | 3 | 2 | Fail | The function is not dividing the two integers, but rather multiplying them.
2 | Divide a positive integer by 0 | 1, 0 | ZeroDivisionError | ZeroDivisionError | Pass | NA


## 4. 'multiply' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
1 | Multiply two positive integers | 4,3 | 12 | 1.333333 | Fail | The function is not multiplying the two integers, but rather dividing.
2 | Multiply a positive integer and 0 | 4,0 | 0 | 0 | Pass | NA

## 5. 'greet' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
1 | Greet a person | "John" | "Heloo, John!" | "Hello, John!" | Fail | There is a typo in the expected result.
2 | Greet a person | "Doe" | "Hello, Doe!" | "Hello, Doe!" | Pass | NA

## 6. 'grade_calc' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
1 | Calculate the grade of A student | 95 | "A" | "A" | Pass | NA
2 | Calculate the grade of B student | 85 | "B" | "B" | Pass | NA
3 | Calculate the grade of C student | 79 | "C" | "Invalid Score" | Fail | 79 is not inclusive in the range for 70 <= score < 79 and should be changed to 80|

## 7. 'speed_check' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
1 | Check the speed of a car | 10 | "Too Slow" | "Too Slow" | Pass | NA
2 | Check the speed of a car | 50 | "Within limit" | "Within limit" | Pass | NA
3 | Check the speed of a car | 80 | "Over speed limit" | "Over speed limit" | Pass | NA
4 | Check the speed of a car | 65 | "Within limit" | "Unknown" | Fail | The upper end of the range is not inclusive.


## 8. 'is_leap_year' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
1 | Check if a year is a leap year | 2020 | True | True | Pass | NA
2 | Check if a year is a leap year | 1900 | False | True | Fail | if year % 4 == 0 return true and elsif year % 100 == 0 return false) were not combined|