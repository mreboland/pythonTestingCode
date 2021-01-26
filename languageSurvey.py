from survey import AnonymousSurvey

# Define a question, and make a survey
question = "What language did you first learn to speak?"
mySurvey = AnonymousSurvey(question)

# Show the question, and store responses to the question
mySurvey.showQuestion()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == "q":
        break
    mySurvey.storeResponse(response)
    
# Show the survey results
print("\nThank you to everyone who participated in the survey!")
mySurvey.showResults()

# This class works for a simple anonymous survey. But let’s say we want to
# improve AnonymousSurvey and the module it’s in, survey. We could allow each
# user to enter more than one response. We could write a method to list only
# unique responses and to report how many times each response was given.
# We could write another class to manage nonanonymous surveys.

# Implementing such changes would risk affecting the current behavior
# of the class AnonymousSurvey. For example, it’s possible that while trying to
# allow each user to enter multiple responses, we could accidentally change
# how single responses are handled. To ensure we don’t break existing behavior
# as we develop this module, we can write tests for the class.
