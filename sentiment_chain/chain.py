from .prompt import SYSTEM_MESSAGE, PASSAGE_MESSAGE
from langchain.schema.language_model import BaseLanguageModel
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessage,
    SystemMessagePromptTemplate
)
from langchain.pydantic_v1 import BaseModel

class ChainInput(BaseModel):
  context: str
  passage: str

def load_sentiment_analysis_chain(llm: BaseLanguageModel):
  messages = [
    SystemMessagePromptTemplate.from_template(SYSTEM_MESSAGE),
    HumanMessage(content=PASSAGE_MESSAGE)
  ]

  prompt = ChatPromptTemplate.from_messages(messages)

  return (
    {
      "context": lambda x: x['context'],
      "passage": lambda x: x['passage']
    }
    |
    prompt
    |
    llm.bind(temperature=0)
  )
