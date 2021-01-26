# Testing a class
# We'll be using classes in our own programs so it's helpful to be able to prove that our classes work correctly. If we have a passing test for a class, we can be confident that improvements we make to the class won't accidentally break its current behaviour

# A variety of asset methods
# Python provides a number of assert methods in the unittest.TestCase class.
# See the table below for the most commonly used assert methods.

# Method                  Use
# assertEqual(a, b)       Verify that a == b
# assertNotEqual(a, b)    Verify that a != b
# assertTrue(x)           Verify that x is True
# assertFalse(x)          Verify that x is False
# assertIn(item, list)    Verify that item is in list
# assertNotIn(item, list) Verify that item is not in list

# A class to test
# Testing a class is similar to testing a function with a few differences

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    
    # class starts with a survey question that we provide and includes and empty list to store respones.
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
        
    # Show the survey question we stored
    def showQuestion(self):
        """Show the survey question"""
        print(self.question)
        
    # Add new responses to the list
    def storeResponse(self, newResponse):
        """Store a single response to the survey"""
        self.responses.append(newResponse)
    
    # Print all the stored responses
    def showResults(self):
        """Show all the responses that have been given"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
            
# To create an instance to this class, all we need to provide is a question. We'll show that in languageSurvey.py