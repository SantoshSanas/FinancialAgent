# Financial Agent Project

A multi-agent system that combines web search capabilities with financial data analysis using phidata framework.

## Setup

1. **Install Python**
   - Make sure you have Python 3.8 or higher installed
   - You can check your Python version by running:
     ```
     python --version
     ```

2. **Install Required Packages**
   ```cmd
   pip install phidata python-dotenv openai yfinance
   ```

3. **Configure Environment Variables**
   - The project uses a `.env` file in the `Financial_agent` folder
   - Make sure your `.env` file has these API keys:
     ```
     API_KEY = "your-phi-api-key"
     GROQ_API_KEY = "your-groq-api-key"
     OPENAI_API_KEY = "your-openai-api-key"
     ```

## Project Structure
```
Financial_agent/
├── .env                  # API keys and configuration
├── financial_agent.py    # Main agent implementation
└── run_agent.py         # Interactive runner script
```

## Running the Project

1. **Navigate to the project directory**
   ```cmd
   cd c:\Users\Admin\Documents\AgenticAI
   ```

2. **Run the interactive agent**
   ```cmd
   python Financial_agent\run_agent.py
   ```

3. **Using the Agent**
   - Type your queries and press Enter
   - The agent will respond using both web search and financial data
   - Type 'exit' or press Ctrl+C to quit

## Example Queries
- "What is the current stock price of Tesla?"
- "Show me the latest news about Apple and its stock performance"
- "Give me a technical analysis of Microsoft stock"
- "What are the key financial metrics for Amazon?"

## Troubleshooting

If you encounter any errors:
1. Make sure all required packages are installed
2. Verify your API keys are correctly set in the `.env` file
3. Check that you're running the command from the correct directory
4. Ensure your Python environment has access to all required dependencies

## Notes
- The agent uses Groq's LLM for processing
- Financial data is fetched from Yahoo Finance
- Web searches are performed using DuckDuckGo