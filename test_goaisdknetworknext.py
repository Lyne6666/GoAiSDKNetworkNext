# test_goaisdknetworknext.py
"""
Tests for GoAiSDKNetworkNext module.
"""

import unittest
from goaisdknetworknext import GoAiSDKNetworkNext

class TestGoAiSDKNetworkNext(unittest.TestCase):
    """Test cases for GoAiSDKNetworkNext class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GoAiSDKNetworkNext()
        self.assertIsInstance(instance, GoAiSDKNetworkNext)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GoAiSDKNetworkNext()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
