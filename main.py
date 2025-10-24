# main.py
import os
from agents.data_analytics_agent import create_data_analytics_agent, query_data_agent
from agents.conversational_agent import create_conversational_agent, format_response
from agents.charting_agent import create_charting_agent, query_charting_agent
from config import DATA_CSV_PATH, CHARTING_KEYWORDS

def main():
    """
    The main function to run the agent system.
    Includes routing for data analysis and chart generation.
    """
    print("Initializing the Agent System...")

    data_file_path = DATA_CSV_PATH

    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set.")
        return

    # Create the agents
    data_agent = create_data_analytics_agent(data_file_path)
    chart_agent = create_charting_agent(data_file_path)
    conv_agent = create_conversational_agent()

    # Check for agent creation errors
    if any(isinstance(agent, str) for agent in [data_agent, chart_agent]):
        print("Failed to initialize one or more agents. Exiting.")
        return

    print("\nSystem is ready. You can now ask questions about your data.")
    print("Example: 'What are the total sales per country?'")
    print("Example: 'Plot a bar chart of the total amount by category.'")
    print("Type 'exit' to quit.")

    while True:
        user_query = input("\nYour question: ")
        if user_query.lower() == 'exit':
            print("Exiting... Goodbye!")
            break

        # Route to the appropriate agent based on keywords
        if any(keyword in user_query.lower() for keyword in CHARTING_KEYWORDS):
            print("\nGenerating chart...")
            chart_response = query_charting_agent(chart_agent, user_query)
            print(f"\nInsight: {chart_response}")
        else:
            print("\nAnalyzing data...")
            analysis_result = query_data_agent(data_agent, user_query)

            print("\nFormatting response...")
            formatted_output = format_response(conv_agent, analysis_result)

            print("\nHere are the insights:")
            print(formatted_output)

if __name__ == "__main__":
    main()