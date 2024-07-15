from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence

def get_code_chain(llm):
    code_prompt = PromptTemplate(
        input_variables=["task", "language"],
        template="Write a {language} function that will {task}."
    )
    code_chain = code_prompt | llm
    return code_chain

def execute_code_chain(llm, language: str, task: str):
    code_chain = get_code_chain(llm)
    result = code_chain.invoke({"language": language, "task": task})
    return result