# test_zkstream.py
"""
Tests for ZKStream module.
"""

import unittest
from zkstream import ZKStream

class TestZKStream(unittest.TestCase):
    """Test cases for ZKStream class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZKStream()
        self.assertIsInstance(instance, ZKStream)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZKStream()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
