"""
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"])) 

    'The above syntax is applied below to store the question objects in the question_bank as a list of objects.'
"""

question_bank = [(Question(question["text"], question["answer"])) for question in question_data]
