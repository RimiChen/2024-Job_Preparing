### because langchain >=2.0 didn't support older command of langchain community
### https://github.com/DataDog/dd-trace-py/issues/8212
### langchain helps to incorperate calls to LLM within python codes
import warnings
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
# from langchain.llms import HuggingFaceHub
# from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
# from langchain.llms import OpenAI
from sk import my_sk # importing secret key from python file, openAI API


### output parser
class GradeOutputParser(BaseOutputParser):
    """Determine whether grade was correct or wrong"""
    def parse(self, text:str):
        """Parse the output of an LLM call."""
        return "wrong" not in text.lower()
    

### define LLM object
chat_model = ChatOpenAI(model_name="gpt-4", openai_api_key = my_sk, temperature = 0)

### defin prompt template
prompt_template_text = """
You are a high school history teacher grading homework assignments.\
Based on the homework question indicated by '**Q:**'\
whether the student's answer is correct. Grading is binart; therefore, \
student answers can be correct or wrong. Simple misspellings are okay.

**Q:** {question}
**A:** {correct_answer}

**Student's Answer:** {student_answer}

"""

prompt = PromptTemplate(
    input_variable = ["question", "correct_answer", "student_answer"], \
    template = prompt_template_text
)

### define chain
chain = LLMChain(
    llm = chat_model,
    prompt = prompt,
    output_parser = GradeOutputParser()
    )

### define inputs
question = "Who was the 35th president of the United States of America?"
correct_answer = "John F. Kennedy"
student_answer = "FDR"

### run chain
# answer = chain.run({'question': question, 'correct_answer':correct_answer, \
#            'student_answer':student_answer})

# print(answer)
### expected output: studnet's answer is wrong

### run chain in for loop
student_answer_list = ["John F. Kennedy", "JFK", "FDR", "John F. Kenedy", \
                       "John Kennedy", "Jack Kennedy", "Jacqueline Kennedy", \
                        "Robert F. Kenedy"]

for student_answer in student_answer_list:
    print(student_answer + "-" +
          str(chain.run({'question': question, 'correct_answer':correct_answer, \
           'student_answer':student_answer})))
    print("\n")