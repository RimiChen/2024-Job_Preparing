### because langchain >=2.0 didn't support older command of langchain community
### https://github.com/DataDog/dd-trace-py/issues/8212
import warnings
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser

