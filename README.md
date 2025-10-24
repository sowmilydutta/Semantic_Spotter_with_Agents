# 📊 SemanticSpotter: Conversational Data Analysis Agent

SemanticSpotter is a sophisticated system that leverages Large Language Models (LLMs) and the **LangChain Expression Language (LCEL)** to provide natural language access to data analysis and visualization. Users can interact with the system using plain English to query data within a CSV file, receive formatted insights, and generate charts.

The architecture employs a specialized **trio of autonomous agents** to handle the full lifecycle of a data request: **Data Analysis**, **Chart Generation**, and **Conversational Formatting**.

## ✨ Core Features

*   **Natural Language Data Analysis:** Users ask questions about their data, and the system autonomously generates and executes Python code using a `pandas` agent to find the answer.
*   **Intelligent Routing:** Queries are automatically routed to the correct agent (Analysis or Charting) based on predefined keywords (e.g., "plot," "chart," "visualize").
*   **LLM-Powered Visualization:** The Charting Agent can autonomously create and save data visualizations (using Matplotlib/Seaborn) based on the user's instructions.
*   **Conversational Summarization (LCEL):** Raw analysis output is passed to a dedicated Conversational Agent, which uses LCEL to rephrase and present the findings in a clear, non-technical, and user-friendly summary.
*   **High Reliability:** Agents use a low temperature setting for deterministic code generation and execution, ensuring accurate and consistent results.

## 🏗️ System Architecture: A Trio of Agents

SemanticSpotter's power lies in its modular design, where three distinct agents collaborate to deliver the final output.

### 1. Data Analytics Agent (`data_analytics_agent.py`)

*   **Functionality:** Responsible for complex analytical tasks, calculations, filtering, and aggregation.
*   **Implementation:** Built using the `create_pandas_dataframe_agent` from LangChain, giving the LLM direct, controlled access to the Pandas DataFrame loaded from the user's CSV.
*   **Process:** Takes a natural language query (e.g., "What is the average sales amount per region?") and converts it into runnable Python code (via the LLM) to produce the quantitative result.

### 2. Charting Agent (`charting_agent.py`)

*   **Functionality:** Responsible for generating and saving data visualizations.
*   **Implementation:** Also uses a specialized `create_pandas_dataframe_agent` but is strictly instructed to generate Matplotlib/Seaborn code.
*   **Process:** The agent receives a plotting instruction (e.g., "Plot a bar chart of total amount by category") and executes code to save the generated chart file locally to the `charts/` directory.

### 3. Conversational Agent (`conversational_agent.py`)

*   **Functionality:** Responsible for transforming raw, technical output into a professional, conversational summary.
*   **Implementation:** Uses the modern **LangChain Expression Language (LCEL)** with a simple `Prompt | LLM` sequence.
*   **Process:** Takes the raw analytical result (e.g., a Pandas table or a Python string) from the Data Analytics Agent and, guided by a system prompt, formats it concisely and clearly for the end user.

## ⚙️ Setup and Installation

### Prerequisites

*   Python 3.x
*   **Dependencies:** All dependencies are managed in `requirements.txt` (including `pandas`, `langchain-openai`, `matplotlib`).
*   **OpenAI API Key:** The system requires the `OPENAI_API_KEY` to be set as an environment variable.

### 1. Install Dependencies

Install all necessary Python packages:

```bash
pip install -r requirements.txt
```

### 2. Configure Data Path

Before running, ensure the `DATA_CSV_PATH` in `config.py` points to your target CSV file.

```python
# config.py

# Point this to the absolute or relative path of your data file
DATA_CSV_PATH = "path/to/your/data.csv" 
```

### 3. Execution

Run the `main.py` file to start the interactive agent system:

```bash
python main.py
```

## 💬 Usage Examples

Once the system initializes, you can pose questions directly to the console. The system handles the routing and formatting automatically.

**Example 1: Data Analysis (Routed to Data Analytics Agent)**

*   **User Query:** `What is the total sales amount for the 'Electronics' category this year?`
*   **System Response:** Initiates analysis, executes code, and formats the numeric result conversationally.

**Example 2: Chart Generation (Routed to Charting Agent)**

*   **User Query:** `Plot a bar chart showing the distribution of customers by country.`
*   **System Response:** Initiates chart generation, saves the file to the `charts/` directory, and responds with the saved file path.
