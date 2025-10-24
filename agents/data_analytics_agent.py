# data_analytics_agent.py

import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import OpenAI
import datetime

def create_data_analytics_agent(file_path: str):
    """
    Creates a data analytics agent that can answer questions about a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        A LangChain agent that can perform data analysis on the given CSV.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return "Error: The specified file was not found. Please check the file path."
    except Exception as e:
        return f"Error loading the CSV file: {e}"

    # Instantiate the OpenAI LLM
    # We are using a temperature of 0 to get deterministic outputs
    llm = OpenAI(temperature=0)

    # Create the pandas DataFrame agent
    # The agent will have access to the dataframe and the llm
    # and will be able to execute python code to answer questions.
    return create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)

def query_data_agent(agent, query: str) -> str:
    """
    Queries the data analytics agent with a natural language question.

    Args:
        agent: The data analytics agent.
        query (str): The natural language query about the data.

    Returns:
        str: The agent's response.
    """
    try:
        # The agent.invoke method runs the query and returns the result.
        response = agent.invoke(query)
        return response['output']
    except Exception as e:
        return f"An error occurred while querying the agent: {e}"