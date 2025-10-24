# conversational_agent.py

from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

def create_conversational_agent() -> RunnableSequence:
    """
    Creates a conversational agent that can rephrase and format text using LCEL.
    """
    llm = OpenAI(temperature=0)

    prompt_template = """
    You are a data analyst assistant. Your ONLY job is to take the raw data analysis output below and present it in a clear, concise, and user-friendly manner.

    - Do NOT add any new information or insights that are not present in the original analysis.
    - Focus on rephrasing the key findings.
    - If the analysis is a table, format it nicely.
    - If the analysis is a single number or statement, present it cleanly.

    Original analysis:
    ```{analysis}```

    Your beautifully formatted and easy-to-understand response:
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["analysis"])

    # Create the modern LangChain sequence using the pipe operator
    return prompt | llm

def format_response(agent: RunnableSequence, analysis_result: str) -> str:
    """
    Uses the conversational agent to format the data analysis result.
    """
    try:
        # Use .invoke() with a dictionary input
        response = agent.invoke({"analysis": analysis_result})
        return response
    except Exception as e:
        return f"An error occurred while formatting the response: {e}"