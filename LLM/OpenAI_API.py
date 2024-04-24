import openai
from sk import my_sk #import secret key from sk,py file
import time
import sys

print(sys.executable)

openai.api_key = my_sk

message_list = [
    {"role":"system", "content":"This is the end"},
    {"role":"user", "content":"Hold your breath and count to ten"},
    {"role":"assistant", "content":"This is a fire starting in my heart"},
    {"role":"user", "content":"It could have it all"},
    {"role":"assistant", "content":"Rolling in the deep"},
    {"role":"user", "content":"Listen to your"}
]


# chat_completion.to_dict()
for i in range(4):
#ChatCompletion --> chat.completions, openai >= 1.0.0
# temperature: control the randomness
# n: number of answers
    chat_completion = openai.chat.completions.create(model="gpt-3.5-turbo",
                                                    messages=message_list,
                                                    max_tokens = 15, n = 1,
                                                    temperature = 0)

    print(chat_completion.choices[0].message.content)

    new_message = {"role":"assistant", "content": chat_completion.choices[0].message.content}
    message_list.append(new_message)
    time.sleep(0.1)
