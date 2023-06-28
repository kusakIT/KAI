import re

knowledge_base = {
    r"what.*name": "My name is AI.",
    r"how.*you": "I'm doing well, thank you!",
    r"(capital.*france|france.*capital)": "The capital of France is Paris.",
    r"president.*united.*states": "The current president of the United States is Joe Biden.",
    r"meaning.*life": "The meaning of life is subjective and varies for each individual."
}

def get_best_response(user_input):
    user_input = user_input.lower()
    
    for question_pattern, response in knowledge_base.items():
        if re.search(question_pattern, user_input):
            return response
    
    return "I'm sorry, I don't have an answer for that question."

while True:
    question = input("Ask a question (or enter 'q' to quit): ")
    
    if question.lower() == 'q':
        break
    
    response = get_best_response(question)
    
    print("AI: " + response)
