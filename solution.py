### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.


def welcome_assignment_answers(question):
    # Students do not have to follow the skeleton for this assignment.
    # Another way to implement is using a "case" statements similar to C.

    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted " \
                   "by a TA?":
        answer = "mtls"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking'":
        answer = "42b76fe51778764973077a5a94056724"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to?":
        answer = 5
    elif question == "What layer of the TCP/IP model the protocol TCP belongs to?":
        answer = 4
    else:
        answer = "No other answers"
    return answer


# Complete all the questions.


if __name__ == "__main__":
    # use this space to debug and verify that the program works
    debug_question1 = "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel " \
                      "posted by a TA? "
    print(welcome_assignment_answers(debug_question1))
    debug_question2 = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question2))
    debug_question3 = "Is it possible to decrypt a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question3))
    debug_question4 = "Is it possible to decode a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question4))
    debug_question5 = "Is a hashed message supposed to be un-hashed? - Yes/No"
    print(welcome_assignment_answers(debug_question5))
    debug_question6 = "What is the MD5 hashing value to the following message: 'NYU Computer Networking'"
    print(welcome_assignment_answers(debug_question6))
    debug_question7 = "Is MD5 a secured hashing algorithm? - Yes/No"
    print(welcome_assignment_answers(debug_question7))
    debug_question8 = "What layer from the TCP/IP model the protocol DHCP belongs to?"
    print(welcome_assignment_answers(debug_question8))
    debug_question9 = "What layer of the TCP/IP model the protocol TCP belongs to?"
    print(welcome_assignment_answers(debug_question9))

###Questions:
###"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
###"Are encoding and encryption the same? - Yes/No"
###"Is it possible to decrypt a message without a key? - Yes/No"
###"Is it possible to decode a message without a key? - Yes/No"
###"Is a hashed message supposed to be un-hashed? - Yes/No"
###"What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code"
###"Is MD5 a secured hashing algorithm? - Yes/No"
###"What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number"
###"What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number"
