from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
# import logging

# Optional: Increase logging level to debug
# logging.basicConfig(level=logging.DEBUG)

# Initialize tokenizer, retriever, and model
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base", trust_remote_code=True)
retriever = RagRetriever.from_pretrained(
    "facebook/rag-token-base", 
    index_name="exact", 
    use_dummy_dataset=False,  # Try with a real dataset
    trust_remote_code=True
)
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-base", retriever=retriever)

# Input query for the model
query = "What is the significance of the RAG pipeline?"

# Tokenize the input query
input_ids = tokenizer(query, return_tensors="pt")["input_ids"]

# Generate the output using the RAG pipeline
output_ids = model.generate(input_ids)

# Decode and print the output
generated_output = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
print("Generated Output:", generated_output[0])