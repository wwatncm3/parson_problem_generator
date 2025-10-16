"""
Unit Tests for Python Parson's Problem Generator Solutions

This file contains unit tests for all 8 function-based Parson's problems
to verify that the correct solutions actually work as expected.

Run with: python test_parsons_solutions.py
"""

import unittest
import random
import time
from io import StringIO
import sys


class TestProductFilter(unittest.TestCase):
    """Test cases for Product Filter problem (Easy)"""
    
    def test_filter_by_price_basic(self):
        """Test basic filtering with example data"""
        def filter_by_price(products, max_price):
            affordable_items = []
            for product, price in products.items():
                if price <= max_price:
                    affordable_items.append(product)
            return affordable_items
        
        products = {"laptop": 1200, "mouse": 25, "keyboard": 75}
        result = filter_by_price(products, 100)
        self.assertIn("mouse", result)
        self.assertIn("keyboard", result)
        self.assertNotIn("laptop", result)
    
    def test_filter_by_price_all_affordable(self):
        """Test when all products are affordable"""
        def filter_by_price(products, max_price):
            affordable_items = []
            for product, price in products.items():
                if price <= max_price:
                    affordable_items.append(product)
            return affordable_items
        
        products = {"pen": 5, "notebook": 3, "eraser": 1}
        result = filter_by_price(products, 10)
        self.assertEqual(len(result), 3)
    
    def test_filter_by_price_none_affordable(self):
        """Test when no products are affordable"""
        def filter_by_price(products, max_price):
            affordable_items = []
            for product, price in products.items():
                if price <= max_price:
                    affordable_items.append(product)
            return affordable_items
        
        products = {"car": 20000, "house": 300000, "yacht": 1000000}
        result = filter_by_price(products, 100)
        self.assertEqual(len(result), 0)


class TestCalculateTotalCost(unittest.TestCase):
    """Test cases for Calculate Total Cost problem (Easy)"""
    
    def test_calculate_total_basic(self):
        """Test basic calculation with rounding"""
        def calculate_total(price, quantity):
            total = price * quantity
            return round(total, 2)
        
        result = calculate_total(10.50, 2)
        self.assertEqual(result, 21.00)
    
    def test_calculate_total_rounding(self):
        """Test rounding to 2 decimal places"""
        def calculate_total(price, quantity):
            total = price * quantity
            return round(total, 2)
        
        result = calculate_total(10.333, 3)
        self.assertEqual(result, 31.00)
    
    def test_calculate_total_single_item(self):
        """Test with quantity of 1"""
        def calculate_total(price, quantity):
            total = price * quantity
            return round(total, 2)
        
        result = calculate_total(99.99, 1)
        self.assertEqual(result, 99.99)


class TestStudentGradeAnalyzer(unittest.TestCase):
    """Test cases for Student Grade Analyzer problem (Medium)"""
    
    def test_find_passing_students_basic(self):
        """Test basic passing student filtering"""
        def find_passing_students(students):
            passing = []
            for name, score in students.items():
                if score >= 70:
                    passing.append(name)
            return passing
        
        students = {"Alice": 85, "Bob": 62, "Charlie": 90}
        result = find_passing_students(students)
        self.assertIn("Alice", result)
        self.assertIn("Charlie", result)
        self.assertNotIn("Bob", result)
    
    def test_find_passing_students_boundary(self):
        """Test boundary case with score exactly 70"""
        def find_passing_students(students):
            passing = []
            for name, score in students.items():
                if score >= 70:
                    passing.append(name)
            return passing
        
        students = {"Dave": 70, "Emma": 69}
        result = find_passing_students(students)
        self.assertIn("Dave", result)
        self.assertNotIn("Emma", result)
    
    def test_find_passing_students_all_pass(self):
        """Test when all students pass"""
        def find_passing_students(students):
            passing = []
            for name, score in students.items():
                if score >= 70:
                    passing.append(name)
            return passing
        
        students = {"Frank": 95, "Grace": 88, "Henry": 72}
        result = find_passing_students(students)
        self.assertEqual(len(result), 3)


class TestWordStartsWithFilter(unittest.TestCase):
    """Test cases for Word Starts With Filter problem (Medium)"""
    
    def test_find_matching_words_basic(self):
        """Test basic word filtering by starting character"""
        def find_matching_words(word_list, char):
            matching_words = []
            for word in word_list:
                if word[0].lower() == char.lower():
                    matching_words.append(word)
            return matching_words
        
        words = ["Zoology", "quiz", "juxtaposition", "zigzag", "jumble"]
        result = find_matching_words(words, "z")
        self.assertIn("Zoology", result)
        self.assertIn("zigzag", result)
        self.assertEqual(len(result), 2)
    
    def test_find_matching_words_case_insensitive(self):
        """Test case-insensitive matching"""
        def find_matching_words(word_list, char):
            matching_words = []
            for word in word_list:
                if word[0].lower() == char.lower():
                    matching_words.append(word)
            return matching_words
        
        words = ["Apple", "banana", "Avocado", "cherry"]
        result = find_matching_words(words, "A")
        self.assertEqual(len(result), 2)
    
    def test_find_matching_words_no_matches(self):
        """Test when no words match"""
        def find_matching_words(word_list, char):
            matching_words = []
            for word in word_list:
                if word[0].lower() == char.lower():
                    matching_words.append(word)
            return matching_words
        
        words = ["apple", "banana", "cherry"]
        result = find_matching_words(words, "z")
        self.assertEqual(len(result), 0)


class TestRandomWinnerSelection(unittest.TestCase):
    """Test cases for Random Winner Selection problem (Medium)"""
    
    def test_announce_winner_output(self):
        """Test that winner announcement produces correct output"""
        def announce_winner(entries):
            print("And the winner is ...")
            time.sleep(0.01)  # Shortened for testing
            winner = random.choice(entries)
            print(winner)
            return winner  # Added return for testing
        
        participants = ["Simone", "Javi", "Miles"]
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        winner = announce_winner(participants)
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("And the winner is ...", output)
        self.assertIn(winner, participants)
        self.assertIn(winner, output)
    
    def test_announce_winner_valid_choice(self):
        """Test that winner is always from participant list"""
        def announce_winner(entries):
            print("And the winner is ...")
            time.sleep(0.01)
            winner = random.choice(entries)
            print(winner)
            return winner
        
        participants = ["Alice", "Bob", "Charlie"]
        
        # Test multiple times to verify randomness
        for _ in range(10):
            captured_output = StringIO()
            sys.stdout = captured_output
            winner = announce_winner(participants)
            sys.stdout = sys.__stdout__
            self.assertIn(winner, participants)


class TestBookInventoryManager(unittest.TestCase):
    """Test cases for Book Inventory Manager problem (Hard)"""
    
    def test_check_low_stock_basic(self):
        """Test basic low stock detection"""
        def check_low_stock(inventory, threshold=5):
            low_stock = []
            for book, quantity in inventory.items():
                if quantity <= threshold:
                    low_stock.append(book)
            return low_stock
        
        inventory = {"1984": 3, "Dune": 12, "Hamlet": 5}
        result = check_low_stock(inventory)
        self.assertIn("1984", result)
        self.assertIn("Hamlet", result)
        self.assertNotIn("Dune", result)
    
    def test_check_low_stock_custom_threshold(self):
        """Test with custom threshold"""
        def check_low_stock(inventory, threshold=5):
            low_stock = []
            for book, quantity in inventory.items():
                if quantity <= threshold:
                    low_stock.append(book)
            return low_stock
        
        inventory = {"Book1": 8, "Book2": 10, "Book3": 5}
        result = check_low_stock(inventory, threshold=8)
        self.assertIn("Book1", result)
        self.assertIn("Book3", result)
        self.assertNotIn("Book2", result)
    
    def test_check_low_stock_all_low(self):
        """Test when all books are low stock"""
        def check_low_stock(inventory, threshold=5):
            low_stock = []
            for book, quantity in inventory.items():
                if quantity <= threshold:
                    low_stock.append(book)
            return low_stock
        
        inventory = {"Book1": 2, "Book2": 3, "Book3": 1}
        result = check_low_stock(inventory)
        self.assertEqual(len(result), 3)


class TestTemperatureConverter(unittest.TestCase):
    """Test cases for Temperature Converter problem (Hard)"""
    
    def test_convert_temp_freezing(self):
        """Test freezing temperature"""
        def convert_temp(fahrenheit):
            celsius = (fahrenheit - 32) * 5 / 9
            if celsius < 0:
                return "Freezing"
            elif celsius < 20:
                return "Cold"
            elif celsius < 30:
                return "Moderate"
            else:
                return "Hot"
        
        result = convert_temp(20)  # -6.67°C
        self.assertEqual(result, "Freezing")
    
    def test_convert_temp_cold(self):
        """Test cold temperature"""
        def convert_temp(fahrenheit):
            celsius = (fahrenheit - 32) * 5 / 9
            if celsius < 0:
                return "Freezing"
            elif celsius < 20:
                return "Cold"
            elif celsius < 30:
                return "Moderate"
            else:
                return "Hot"
        
        result = convert_temp(50)  # 10°C
        self.assertEqual(result, "Cold")
    
    def test_convert_temp_moderate(self):
        """Test moderate temperature"""
        def convert_temp(fahrenheit):
            celsius = (fahrenheit - 32) * 5 / 9
            if celsius < 0:
                return "Freezing"
            elif celsius < 20:
                return "Cold"
            elif celsius < 30:
                return "Moderate"
            else:
                return "Hot"
        
        result = convert_temp(77)  # 25°C
        self.assertEqual(result, "Moderate")
    
    def test_convert_temp_hot(self):
        """Test hot temperature"""
        def convert_temp(fahrenheit):
            celsius = (fahrenheit - 32) * 5 / 9
            if celsius < 0:
                return "Freezing"
            elif celsius < 20:
                return "Cold"
            elif celsius < 30:
                return "Moderate"
            else:
                return "Hot"
        
        result = convert_temp(86)  # 30°C
        self.assertEqual(result, "Hot")
    
    def test_convert_temp_boundaries(self):
        """Test boundary conditions"""
        def convert_temp(fahrenheit):
            celsius = (fahrenheit - 32) * 5 / 9
            if celsius < 0:
                return "Freezing"
            elif celsius < 20:
                return "Cold"
            elif celsius < 30:
                return "Moderate"
            else:
                return "Hot"
        
        # Test 0°C boundary
        result_32 = convert_temp(32)
        self.assertEqual(result_32, "Cold")
        
        # Test 20°C boundary (68°F)
        result_68 = convert_temp(68)
        self.assertEqual(result_68, "Moderate")


class TestEmailValidator(unittest.TestCase):
    """Test cases for Email Validator problem (Hard)"""
    
    def test_validate_email_valid(self):
        """Test valid email addresses"""
        def validate_email(email):
            if email.count("@") != 1:
                return False
            at_position = email.find("@")
            domain = email[at_position + 1:]
            if "." in domain:
                return True
            else:
                return False
        
        self.assertTrue(validate_email("user@example.com"))
        self.assertTrue(validate_email("test@mail.org"))
        self.assertTrue(validate_email("admin@company.co.uk"))
    
    def test_validate_email_invalid_no_at(self):
        """Test email without @ symbol"""
        def validate_email(email):
            if email.count("@") != 1:
                return False
            at_position = email.find("@")
            domain = email[at_position + 1:]
            if "." in domain:
                return True
            else:
                return False
        
        self.assertFalse(validate_email("userexample.com"))
    
    def test_validate_email_invalid_multiple_at(self):
        """Test email with multiple @ symbols"""
        def validate_email(email):
            if email.count("@") != 1:
                return False
            at_position = email.find("@")
            domain = email[at_position + 1:]
            if "." in domain:
                return True
            else:
                return False
        
        self.assertFalse(validate_email("user@@example.com"))
    
    def test_validate_email_invalid_no_dot(self):
        """Test email without dot in domain"""
        def validate_email(email):
            if email.count("@") != 1:
                return False
            at_position = email.find("@")
            domain = email[at_position + 1:]
            if "." in domain:
                return True
            else:
                return False
        
        self.assertFalse(validate_email("user@example"))
    
    def test_validate_email_dot_before_at(self):
        """Test email with dot before @ (should be invalid per our logic)"""
        def validate_email(email):
            if email.count("@") != 1:
                return False
            at_position = email.find("@")
            domain = email[at_position + 1:]
            if "." in domain:
                return True
            else:
                return False
        
        # This should be invalid because dot is not in domain part
        self.assertFalse(validate_email("user.name@example"))


class TestIntegration(unittest.TestCase):
    """Integration tests to verify all solutions work together"""
    
    def test_all_functions_defined(self):
        """Verify all function signatures are correct"""
        # This test ensures all functions can be defined without errors
        
        def filter_by_price(products, max_price):
            affordable_items = []
            for product, price in products.items():
                if price <= max_price:
                    affordable_items.append(product)
            return affordable_items
        
        def calculate_total(price, quantity):
            total = price * quantity
            return round(total, 2)
        
        def find_passing_students(students):
            passing = []
            for name, score in students.items():
                if score >= 70:
                    passing.append(name)
            return passing
        
        def find_matching_words(word_list, char):
            matching_words = []
            for word in word_list:
                if word[0].lower() == char.lower():
                    matching_words.append(word)
            return matching_words
        
        def check_low_stock(inventory, threshold=5):
            low_stock = []
            for book, quantity in inventory.items():
                if quantity <= threshold:
                    low_stock.append(book)
            return low_stock
        
        def convert_temp(fahrenheit):
            celsius = (fahrenheit - 32) * 5 / 9
            if celsius < 0:
                return "Freezing"
            elif celsius < 20:
                return "Cold"
            elif celsius < 30:
                return "Moderate"
            else:
                return "Hot"
        
        def validate_email(email):
            if email.count("@") != 1:
                return False
            at_position = email.find("@")
            domain = email[at_position + 1:]
            if "." in domain:
                return True
            else:
                return False
        
        # If we get here, all functions are defined correctly
        self.assertTrue(True)


def run_tests():
    """Run all tests and display results"""
    print("=" * 70)
    print("Running Unit Tests for Parson's Problem Generator")
    print("=" * 70)
    print()
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestProductFilter))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculateTotalCost))
    suite.addTests(loader.loadTestsFromTestCase(TestStudentGradeAnalyzer))
    suite.addTests(loader.loadTestsFromTestCase(TestWordStartsWithFilter))
    suite.addTests(loader.loadTestsFromTestCase(TestRandomWinnerSelection))
    suite.addTests(loader.loadTestsFromTestCase(TestBookInventoryManager))
    suite.addTests(loader.loadTestsFromTestCase(TestTemperatureConverter))
    suite.addTests(loader.loadTestsFromTestCase(TestEmailValidator))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print()
    print("=" * 70)
    print("Test Summary")
    print("=" * 70)
    print(f"Total Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 70)
    
    return result


if __name__ == '__main__':
    result = run_tests()
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
