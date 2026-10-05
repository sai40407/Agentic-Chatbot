# Agentic AI Chatbot with LangGraph

A stateful agentic AI chatbot built with LangGraph and Streamlit. Users choose the LLM, model and use case from a sidebar.

## Features
- **Basic Chatbot:** conversational chat using Groq-hosted LLMs
- **Chatbot with Tool:** uses the Tavily search API to fetch live web information
- **AI News:** fetches the latest AI news for a daily, weekly or monthly timeframe, then sorts and summarizes it. Summaries are saved as markdown files (AINewsdaily_summary.md, AINewsweekly_summary.md, AINewsmonthly_summary.md)

## Tech Stack
Python, LangGraph, LangChain, Groq API, Tavily API, Streamlit

## Project Structure
- `app.py`: entry point of the Streamlit app
- `src/`: LangGraph graph, nodes, state and UI code
- `AINews/`: AI news summaries output
- `requirements.txt`: Python dependencies

## How to Run
1. Clone the repo
   git clone https://github.com/sai40407/Agentic-Chatbot.git
   cd Agentic-Chatbot
2. Install dependencies
   pip install -r requirements.txt
3. Get free API keys from Groq (console.groq.com) and Tavily (tavily.com)
4. Run the app
   streamlit run app.py
5. Enter your Groq API key in the sidebar, choose a use case and start chatting

## Author
Sai Kumar Arukala | github.com/sai40407
