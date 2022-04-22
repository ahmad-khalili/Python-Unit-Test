# Assignment 4: White Box Testing & Unit Test
## 1- Flow Graph, Independent Paths List, Minimal Number of Paths to Achieve 100% Statement Coverage for Each Method
- The images for the flow charts can also be found in the "Images" directory if a clearer view of the charts was needed
### Multiplication/Subtraction/Addition
![QA_Assignment4-Multiply_Subtract_Add](https://user-images.githubusercontent.com/63163965/164723141-5f793b2d-444b-4a96-b57b-994ace6502c2.jpg)

### Division
![QA_Assignment4-Division](https://user-images.githubusercontent.com/63163965/164723174-4d5cea47-c4aa-4e45-9a1d-7f3e18468361.jpg)

### Input Checker
![QA_Assignment4-Input_Check](https://user-images.githubusercontent.com/63163965/164723301-464ce265-6c22-4320-bc99-b890c1391635.jpg)

### Exit Checker
![QA_Assignment4-isExit](https://user-images.githubusercontent.com/63163965/164723370-a4f54955-e064-40d2-831b-e05c09090b33.jpg)

### Calculation
![QA_Assignment4-Calculate](https://user-images.githubusercontent.com/63163965/164723405-4ad9314c-49e6-48f0-9649-96120da05611.jpg)

## 2- Test Cases
- Using the same concept as the examples already set for us. I've created methods that check for each path in the "calculatorrApp.py" file whether they're valid, or invalid. The test functions can be found in the "test_calculatorApp.py" file
```ruby
    def test_check_null_input(self):
        self.assertRaises(ValueError, check_user_input, '')
        self.assertRaises(ValueError, calculate, '1', '', '')

    def test_check_int_input(self):
        self.assertEqual(check_user_input('4'), 4)

    def test_check_float_input(self):
        self.assertEqual(check_user_input('5.4'), 5.4)

    def test_check_not_number_input(self):
        self.assertRaises(ValueError, check_user_input, 'w')

    def test_calculate_choice_invalid(self):
        self.assertRaises(Exception, calculate, '5', 4, 4)

    def test_add_valid(self):
        self.assertEqual(add(6, 3), 9)
        self.assertEqual(calculate('1', 6, 3), 9)

    def test_divide_valid(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(calculate('4', 10, 2), (10, "/", 2, "=", 5))

    def test_divide_denominator_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 3, 0)
        self.assertRaises(ZeroDivisionError, calculate, '4', '3', '0')

    def test_divide_numerator_zero(self):
        self.assertEqual(divide(0, 10), 0)
        self.assertEqual(calculate('4', '0', '10'), (0, "/", 10, "=", 0))

    def test_subtract_valid(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(calculate('2', 10, 5), 5)

    def test_multiply_valid(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(calculate('3', 2, 3), (2, "*", 3, "=", 6))

    def test_no_exit(self):
        self.assertEqual(isExit('no'), True)

    def test_yes_exit(self):
        self.assertEqual(isExit('yes'), False)

    def test_invalid_exit(self):
        self.assertRaises(ValueError, isExit, 'maybe')
```

## 3- Test Cases Run & Code Coverage Reports
- Both of the needed reports can be found above. The test cases run report is in the file named "nosetests.xml". And the code coverage report can be found in the "htmlcov" directory
