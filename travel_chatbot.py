# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

# Start coding here
system_prompt = "You are a travel guide chatbot for Peterman Reality Tours, an internationally acclaimed tourism company. You will answer travel queries related to Paris and deliver valuable insights into the city's landmarks. You will respond to user queries in an intelligent way to provide a more engaging and seamless experience."
question1 = "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?"
question2 = "Where is the Arc de Triomphe?"
question3 = "What are the must-see artworks at the Louvre Museum?"

questions = [question1, question2, question3]
conversation = []
s_dict = {"role": "system", "content": system_prompt}
conversation.append(s_dict)

for q in questions:
    q_dict = {"role": "user", "content": q}
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = [s_dict, q_dict],
        temperature = 0.0,
        max_completion_tokens = 100
    )
    conversation.append(q_dict)
    a_dict = {"role": "assistant", "content": response.choices[0].message.content}
    conversation.append(a_dict)

print(conversation)
# Add as many cells as you like