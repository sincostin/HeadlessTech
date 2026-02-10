# test_headless.py
"""
Tests for Headless module.
"""

import unittest
from headless import Headless

class TestHeadless(unittest.TestCase):
    """Test cases for Headless class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Headless()
        self.assertIsInstance(instance, Headless)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Headless()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
