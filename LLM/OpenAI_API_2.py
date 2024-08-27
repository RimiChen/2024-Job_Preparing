# main_script.py
from sk import my_sk  # Import the API key from sk.py
from langchain_community.chat_models import ChatOpenAI
# from langchain_openai import ChatOpenAI
# Print the API key to ensure it's being imported correctly
print(f"API Key: {my_sk}")

# # Use the imported API key
llm = ChatOpenAI(openai_api_key=my_sk, model_name="gpt-4")

# Example usage
response = llm("What are some best practices for using API keys in Python?")

print(response)