# charting_agent.py
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import OpenAI
import os
import matplotlib

# Force a non-interactive backend to prevent GUI/font warnings
matplotlib.use('Agg')

def create_charting_agent(file_path: str):
    """
    Creates a data analytics agent that can create and save charts.
    """
    if not os.path.exists("charts"):
        os.makedirs(r"C:\Users\SOWMILY DUTTA\Python_Projects\Upgrad\Course 6 - Gen AI\SemanticSpotter\charts")

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return "Error: The specified file was not found. Please check the file path."
    except Exception as e:
        return f"Error loading the CSV file: {e}"

    llm = OpenAI(temperature=0)
    return create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        allow_dangerous_code=True
    )

def query_charting_agent(agent, query: str) -> str:
    """
    Queries the charting agent with a natural language instruction to create a plot.
    """
    prompt = f"""
    Analyze the user's query to generate a plot using python's matplotlib or seaborn library.

    **Instructions:**
    1.  The plot MUST be saved to a file in the 'charts/' directory.
    2.  Name the file descriptively based on the query (e.g., 'sales_by_country.png').
    3.  **Crucially, all text in the plot (titles, x-axis, y-axis, legends) MUST be in English.** Do NOT use any other language.
    4.  Do NOT call `plt.show()`. Only save the plot to a file using `plt.savefig()`.
    5.  After saving the plot, respond ONLY with the path to the saved file. For example: "Chart saved to charts/sales_by_country.png"

    User's query: "{query}"
    """
    try:
        response = agent.invoke(prompt)
        return response['output']
    except Exception as e:
        return f"An error occurred while querying the charting agent: {e}"
    
# This module creates the agent responsible for formatting final answers.
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