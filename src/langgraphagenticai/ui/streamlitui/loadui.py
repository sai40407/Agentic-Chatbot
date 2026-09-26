import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖"+self.config.get_page_title(),layout="wide")
        st.header("🤖"+ self.config.get_page_title())
        st.session_state.timeframe=''
        st.session_state.IsFetchButtionClicked = False

        with st.sidebar:
            #get options from config
            llm_options = self.config.get_llm_options()
            usecase_options=self.config.get_usecase_options()

            #LLM Selection
            self.user_controls["selected_llm"] =st.selectbox("select LLM",llm_options)

            if self.user_controls["selected_llm"]=='Groq':
                #model selection
                model_options = self.config.get_GROQ_model_options()
                self.user_controls["selected_groq_model"]=st.selectbox("select model",model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("APT KEY", type="password", key="GROQ_API_KEY_INPUT")
                # Validate API keys
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning(" please enter your GROQ APT KEY TO proceed.")

            ## usecases selection
            self.user_controls["selected_usecase"]=st.selectbox("select usecases",usecase_options)

            if self.user_controls["selected_usecase"] == "Chatbot with Web" or  self.user_controls["selected_usecase"] == "AI News":
                self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY API KEY", type="password", key="TAVILY_API_KEY_INPUT")
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"]


                #validate API key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("please enter your tavily api key to proced")

           ## if user select ai news then time frame will work
            if self.user_controls['selected_usecase']=="AI News":
                st.subheader("AI News Explorer")

                with st.sidebar:
                    time_frame=st.selectbox(
                        " select time frame",
                        ["Daily","Weekly","Monthly"],
                        index=0
                    )
                if st.button("Fetch Latest AI News",use_container_width=True):
                    st.session_state.IsFetchButtonClicked =True
                    st.session_state.timeframe=time_frame




        return self.user_controls
    