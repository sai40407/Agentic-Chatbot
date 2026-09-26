from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

from src.langgraphagenticai.state import state


class AINewsNode:
    def __init__(self,llm):
        """
        Initiallize the AINewNode with API keys for Tavily and GROQ.
        """

        self.tavily=TavilyClient()
        self.llm=llm
        # this is used to capture various steps in this file so that later can be use for steps show
        self.state={}

    def fetch_news(self,state:dict)->dict:
        """
        Fetch AI  news based on the specified frequency.
        
        Args:
            state (dict): the state dictionary containing 'frequency'.
             
        Returns:
            dict:updated state with 'news_data' key containg fetched news.
             """
        frequency=state['messages'][0].content.lower()
        self.state['frequency']=frequency
        time_range_map={'daily':'d','weekly':'w','monthly':'m',"year":'y'}
        days_map={'daily':1,'weekly':7,'monthly':30,'year':366}


        response = self.tavily.search(
            query="Top Artificial Intelligence (AI) technology news India and globally",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer="advanced",
            max_results=10,
            days=days_map[frequency],
            #include_domain=["techcrunch.com","venturebeat.com/ai",...]
        )

        state['news_data']=response.get('results',[])
        self.state['news_data']=state['news_data']
        return state
        print(f"DEBUG: fetched {len(state['news_data'])} articles")


    def summarize_news(self,state:dict)->dict:
        """
        summarize the fetched news using an LLM.
        
        Args:
            state(dict): the state dictionary containing 'news_data'.
            
        Returns:
            dict: update state with 'summary' key containing the summarized news.
            """
        news_items = self.state.get('news_data', [])

        prompt_template= ChatPromptTemplate.from_messages([
            ("system","""summarize AI nwes articles into markdown format. for ecah item include:
            Date in **YYYY-MM-DD** format in IST Timezone
            consise sentences summary from latest news
            sort news by date wise (latest first)
            source URL as lnk 
            use format:
            ### [Date]
            [summary](URL)"""),
            ("user","Articles:\n{articles}")
        ])

        articles_str = "\n\n".join([
            f"Content:{item.get('content','')[:500]}\nURL:{item.get('url','')}\nDate:{item.get('published_date','')}"
            for item in news_items
        ])

        response = self.llm.invoke(prompt_template.format(articles=articles_str))
        state['summary']=response.content
        self.state['summary']=state['summary']
        return self.state
        print(f"DEBUG: news_items count = {len(news_items)}")
        print(f"DEBUG: articles_str length = {len(articles_str)}")

    def save_result(self,state):
        frequency=self.state['frequency']
        summary=self.state['summary']
        filename=f"./AINews/{frequency}_summary.md"
        with open(filename,'w', encoding='utf-8') as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)
        self.state['filename']=filename
        return self.state
                            





    
        

