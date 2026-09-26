import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    loads and runs the langgraph agenticai application with steamlit ui.
    this function initializes the ui, handles user input,configures the llm model,
    sets up the graph based on the selected use case,and displays the output while
    implementing exception handling for robustness.
    """


    ## load ui
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the ui.")
        return

   # Text input for user message
    if st.session_state.get("IsFetchButtonClicked", False):
        user_message=st.session_state.timeframe
    else:
          user_message=st.chat_input("enter your message:")

    if user_message:
       
        try:
            ## configure the LLM's
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized")
                return

            #initialize and set up the graph based on use case
            usecase=user_input.get("selected_usecase")

            if not model:
                            st.error("Error: LLM model could not be initialized")
                            return

            ## Graph Builder

            graph_builder=GraphBuilder(model)
            try:
                  graph=graph_builder.setup_graph(usecase)
                  DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph set up failed {e}")
                return


        except Exception as e:
              st.error(f"Error:Graph set up failed {e}")
              return

