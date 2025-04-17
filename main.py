from agent.tools import WebAgent
from agent.chains import Chain
import gradio as gr 
from pprint import pprint

webagent = WebAgent()
chain=Chain()
travily_tool = webagent.get_search_tool()
summarize_chain = chain.get_summarize_chain()
synthesis_chain =chain.get_synthesis_chain()

def research_chat(message, history):
    search_content = travily_tool.run(message)
    summary= summarize_chain.run(
        {
            
            "context": search_content
        }
    )

    answer = synthesis_chain.run({
        "summaries" : summary,
        "question" : message
    })
    return answer

chat = gr.ChatInterface(
    fn=research_chat,
    title="Agentica Research Assistant",
    description = "your very own personal deep research agent !",
    examples = [
        "Latest breakthrough in AI",
        "renewable energy adoption in europe ?",
        "benefits and risk of using LLMs ?"
    ],
    theme = "soft"
)
chat.launch()