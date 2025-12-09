from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read Groq API key from environment (set GROQ_API_KEY in your .env or environment)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    # Do not raise here to keep this change low-risk; print a warning so users know to set it.
    print("Warning: GROQ_API_KEY is not set. Groq model calls may fail at runtime if an API key is required.")

webserch_agent = Agent(
    name="WebSearchAgent",
    role = "search the web for relevant information using DuckDuckGo",
    model = Groq(model = "llama3-groq-70b-8192-tool-use-preview", api_key=GROQ_API_KEY),
    tools = [DuckDuckGo()],
    instructions = """You are a web search agent that uses DuckDuckGo to find relevant information on the internet.
When given a query, use the DuckDuckGo tool to search for information and provide concise and relevant answers based on the search results. with source links when applicable.""",
    show_tool_calls=True,
    markdown=True
)

# Financial agent that can search the web and fetch financial data
financial_agent = Agent(
    name="FinancialAgent",
    role = "assist users with financial information and data retrieval using web search and Yahoo Finance",
    model = Groq(model = "llama3-groq-70b-8192-tool-use-preview", api_key=GROQ_API_KEY),
    tools = [ YFinanceTools(stock_price=True, company_info=True, technical_indicators=True, stock_fundamentals=True, company_news=True)],
    instructions = ["You are a financial agent that helps users with financial information and data retrieval. show in table formt"],
    show_tool_calls=True,
)

multi_ai_agent = Agent(
    team=[webserch_agent, financial_agent],
    instructions="You are a team of agents consisting of a Web Search Agent and a Financial Agent. Collaborate to provide accurate and comprehensive responses to user queries by leveraging each agent's strengths.",
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("summarize the latest news about Tesla and provide its current stock price along with a brief company overview.",stream=True)