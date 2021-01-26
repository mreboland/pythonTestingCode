# Testing the AnonymousSurvey Class
# Let's write a test to verify that a single response to the survey question is stored properly.
# We'll use the assertIn() method to verify that the response is in the list of responses after it's been stored

# Import unittest module and our class we want to test
import unittest
from survey import AnonymousSurvey

# Create testing class using proper naming convention and inheriting from unittest.TestCase
# class TestAnonymousSurvey(unittest.TestCase):
    # """Tests for the class AnonymouseSurvey"""
    
    # Our test method here checks that when we store a response to the survey question, the response ends up in the survey's list of responses
    # def testStoreSingleResponse(self):
        # """Test that a single response is stored properly."""
        
        # question = "What language did you first learn to speak?"
        # In order to test the class we need to make an instance of it which calls the class with our created question
        # mySurvey = AnonymousSurvey(question)
        # We store a single response
        # mySurvey.storeResponse("English")
        # We then verify that the response was stored correctly by asserting that "English" is in the list mySurvery.responses
        # self.assertIn("English", mySurvey.responses)
        
# if __name__ == "__main__":
#     unittest.main()
    
# Our above test passed, however a survey is only useful if it generates more than one response. Let's verify that three responses can be stored correctly.

# class TestAnonymousSurvey(unittest.TestCase):
#     """Tests for the class AnonymouseSurvey"""
    
#     def testStoreSingleResponse(self):
#         """Test that a single response is stored properly."""

#         question = "What language did you first learn to speak?"
#         # In order to test the class we need to make an instance of it which calls the class with our created question
#         mySurvey = AnonymousSurvey(question)
#         # We store a single response
#         mySurvey.storeResponse("English")
#         # We then verify that the response was stored correctly by asserting that "English" is in the list mySurvery.responses
#         self.assertIn("English", mySurvey.responses)
    
#     # Here we call the new method to test 3 responses
#     def testStoreThreeResponses(self):
#         """Test that a single response is stored properly."""
#         question = "What language did you first learn to speak?"

#         # We created an instance just like in the single instance
#         mySurvey = AnonymousSurvey(question)
#         # Because we want multiple responses, we made a list of them
#         responses = ["English", "Spanish", "Mandarin"]
#         # We loop over the list so we can store each one in our responses list in our Class AnonymousSurvey
#         for response in responses:
#             mySurvey.storeResponse(response)
            
#         # We then loop over our responses list above so we can compare them to the list mySurvey.responses in our Class to make sure they match.
#         for response in responses:
#             self.assertIn(response, mySurvey.responses)


# if __name__ == "__main__":
#     unittest.main()
    
# The above works perfectly again, however these tests are a bit repetitive, so we'll use another feature of unittest to make them more efficient

# The setUp() method
# In test_survey.py we created a new instance of AnonymousSurvey in each test
# method, and we created new responses in each method. The unittest.TestCase
# class has a setUp() method that allows you to create these objects once and
# then use them in each of your test methods. When you include a setUp()
# method in a TestCase class, Python runs the setUp() method before running
# each method starting with test_. Any objects created in the setUp() method
# are then available in each test method you write.

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymouseSurvey"""
    
    # The method setUp() does two things:
    def setUp(self):
        """Create a survey and a set of responses for use in all test methods"""
        question = "What language did you first learn to speak?"
        # It creates a survey instance and,
        self.mySurvey = AnonymousSurvey(question)
        # it creates a list of responses
        self.responses = ["English", "Spanish", "Mandarin"]
        # The above are prefixed by 'self', so they can be used anywhere in the class.
        

    def testStoreSingleResponse(self):
        """Test that a single response is stored properly."""
        # We take the response in the first spot of our list above and save it to our response list in our class AnonymousSurvey
        self.mySurvey.storeResponse(self.responses[0])
        # We then check if spot 1 in the list above is save in our list in our class
        self.assertIn(self.responses[0], self.mySurvey.responses)

    def testStoreThreeResponses(self):
        """Test that a single response is stored properly."""
        # Looping over our list above to save it to our class
        for response in self.responses:
            self.mySurvey.storeResponse(response)
        
        # looping over our list above again to test each one against the saved list in our class
        for response in self.responses:
            self.assertIn(response, self.mySurvey.responses)
        


if __name__ == "__main__":
    unittest.main()

# These tests would be particularly useful when trying to expand AnonymousSurvey 
# to handle multiple responses for each person. After modifying the code to accept 
# multiple responses, you could run these tests and make sure you haven’t affected the
# ability to store a single response or a series of individual responses.
# When you’re testing your own classes, the setUp() method can make
# your test methods easier to write. You make one set of instances and attributes
# in setUp() and then use these instances in all your test methods. This
# is much easier than making a new set of instances and attributes in each
# test method.

# Note: When a test case is running, Python prints one character for each unit test as it is
# completed. A passing test prints a dot, a test that results in an error prints an E, and
# a test that results in a failed assertion prints an F. This is why you’ll see a different
# number of dots and characters on the first line of output when you run your test cases.
# If a test case takes a long time to run because it contains many unit tests, you can
# watch these results to get a sense of how many tests are passing.
