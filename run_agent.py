"""Interactive runner for the multi-agent system defined in `financial_agent.py`.

Usage:
  - Set environment variables via a local `.env` file or your shell. At minimum set `GROQ_API_KEY` and `OPENAI_API_KEY`.
  - Run: python run_agent.py
"""
import sys
from dotenv import load_dotenv
import os

# Load environment variables from .env if present
load_dotenv()

# Import agents from the module
try:
    from financial_agent import multi_ai_agent
except Exception as e:
    print("Failed to import agents from financial_agent.py:", e)
    sys.exit(1)


def query_agent(agent, text):
    """Call the agent with the provided text using a few common method names."""
    if hasattr(agent, "run"):
        return agent.run(text)
    if hasattr(agent, "respond"):
        return agent.respond(text)
    if hasattr(agent, "ask"):
        return agent.ask(text)
    raise RuntimeError("Agent object does not expose a supported call method (run/respond/ask).")


def main():
    print("Interactive runner for `multi_ai_agent`. Type 'exit' or Ctrl+C to quit.")
    while True:
        try:
            user_input = input("\nEnter your query: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit"):
            print("Goodbye.")
            break

        try:
            response = query_agent(multi_ai_agent, user_input)
        except Exception as e:
            print("Agent call failed:", e)
            continue

        print("\n--- Agent response ---\n")
        print(response)


if __name__ == "__main__":
    main()
