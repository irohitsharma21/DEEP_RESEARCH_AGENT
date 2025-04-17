from tavily import TavilyClient
from langchain.tools import Tool
from config.settings import TAVILY_API_KEY

class WebAgent:

    def __init__(self):

        self.tavily = TavilyClient(api_key=TAVILY_API_KEY)
        self.max_results=2
    
    def search(self,query: str):
        results = self.tavily.search(
            query=query,
            search_depth="advanced",
            max_results= self.max_results
        )
        return results
    
    def web_search_tool(self,query:str)-> str:
        results = self.search(query = query)
        contents=[]
        for r in results.get("results",[]):
            contents.append(r['content'])
        return "\n\n".join(contents)
    
    def get_search_tool(self):
        tavily_tool=Tool(
            name="TavilySearch",
            func= self.web_search_tool,
            description="Tavilly web search function"
        )
        return tavily_tool
            
    
