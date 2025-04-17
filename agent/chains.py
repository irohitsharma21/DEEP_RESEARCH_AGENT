from langchain.llms import HuggingFaceHub 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config.settings import HF_API_KEY, hf_model

class Chain(object):
    def __init__(self):
        self.summarize_prompt = PromptTemplate.from_template(""" summarize the following content in simple and concise points : \n\n {context}""")

        self.synthesis_prompt = PromptTemplate.from_template(""" based on the following summarized document, answer the question below: \n Summaries : \n {summaries}\n\n Questions : \n {question}""")


        self.llm = HuggingFaceHub(
            repo_id=hf_model, 
            model_kwargs={"temperature": 0.3}, 
            huggingfacehub_api_token=HF_API_KEY)


    def get_summarize_chain(self):
        summarize_chain = LLMChain(llm=self.llm, prompt=self.summarize_prompt)
        return summarize_chain
    
    def get_synthesis_chain(self):
        synthesis_chain=LLMChain(llm=self.llm, prompt=self.synthesis_prompt)
        return synthesis_chain
    


