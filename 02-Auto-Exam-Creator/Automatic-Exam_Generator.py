# Generate a multiple choice quiz on any topic with an answer sheet
# Each question can have N possible answers
# We must tell the model exactly how to specify the correct answer

import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')


def create_test_prompt(topic, num_questions, num_possible_answers):
    prompt = f"Create a multiple choice quiz on the topic of {topic} consisting of {num_questions} questions." \
             f"Each question should have {num_possible_answers} options." \
             f"Also include the correct answer for each question using the starting string 'Correct Answer:' "
    return prompt


def extract_answers(test, num_questions):
    answers = {1: ''}   # set up dict
    question_number = 1
    # Split test based on new lines
    for line in test.split("\n"):
        if line.startswith("Correct Answer:"):   # We know we are still in question
            answers[question_number] += line + '\n'
            # If Q num less than number of Q's, add 1 to Q count and move on to next key in dict and set as empty string
            if question_number < num_questions:
                question_number += 1
                answers[question_number] = ' '
    return answers


response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=create_test_prompt('US History', 4, 4),
    max_tokens=256,
    temperature=0.7,
)

# Dictionary of correct answers
answers = (extract_answers(response['choices'][0]['text'], 4))

student_view = (response['choices'][0]['text'], 4)


# Take the exam
def take_exam(student_view, num_questions):
    student_answers = {}
    for question in range(1, num_questions + 1):
        question_text = student_view[f"Question {question}:"]  # Get the question text
        print(question_text)
        answer = input("Enter your answer: ")
        student_answers[question] = answer
    return student_answers


student_answers = take_exam(answers, student_view, 4)


def grade(correct_answer_dict, student_answers):
    correct_answers = 0
    total_questions = len(correct_answer_dict)
    for question, answer in student_answers.items():
        if answer.lower() == correct_answer_dict[question].lower():
            correct_answers += 1
    percentage_correct = (correct_answers / total_questions) * 100

    if percentage_correct < 60:
        passed = "You did not pass!"
    else:
        passed = "Congratulations! You passed!"

    return f"{answers} / {total_questions} correct! You got {percentage_correct:.2f}% grade, {passed}"


print(grade(answers, student_answers))
