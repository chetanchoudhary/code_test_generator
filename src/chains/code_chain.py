from configuration.settings import OPENAI_API_KEY
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence

def get_code_chain():
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    code_prompt = PromptTemplate(
        input_variables=["task", "language"],
        template="Write a {language} function that will {task}."
    )
    # Create a RunnableSequence instead of LLMChain
    code_chain = code_prompt | llm
    return code_chain

def execute_code_chain(language: str, task: str):
    code_chain = get_code_chain()
    # Use invoke instead of calling the chain directly
    result = code_chain.invoke({"language": language, "task": task})
    return result