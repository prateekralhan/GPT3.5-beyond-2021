import os
import json
import openai
import warnings
import streamlit as st
from streamlit_lottie import st_lottie
from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent

warnings.filterwarnings("ignore")

serper_api_key = os.environ["SERPER_API_KEY"]
openai_api_key = os.environ["OpenAI_API_Key_v2"]

st.set_page_config(
    page_title="ChatGPT Beyond 2021",
    page_icon="✨",
    layout= "wide",
    initial_sidebar_state="expanded",
    menu_items={
    'Get Help': 'https://github.com/prateekralhan',
    'Report a bug': "mailto:ralhanprateek@gmail.com",
    'About': "## A minimalistic streamlit application using ChatGPT with google search capabilities."
    } )

@st.cache_data()
def lottie_local(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.cache_data()
def hide_footer():
    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

@st.cache_data()
def instantiate_agent():
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0.7, model_name='gpt-3.5-turbo')
    tools = load_tools(["google-serper"], llm=llm)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
    return agent

hide_footer()
st.title("ChatGPT Beyond 2021 🚀")

col1, col2 = st.columns(2)
with col1:
    anim = lottie_local(r"./static/animation.json")
    st_lottie(anim,
            speed=1,
            reverse=False,
            loop=True,
            height = 700,
            width = 700,
            quality="high",
            key=None)

with col2:
    agent = instantiate_agent()
    st.info(" ##### Let me get answers to anything across the internet and beyond Sep 2021 😉 ")
    question = st.text_area("Please Enter a question 💫", height = 250)
    if st.button("Do the magic! ✨", use_container_width=True):
        with st.spinner("Working.. 💫"):
            try:
                st.success(f"{str(agent.run(question))}")
            except Exception as e:
                    st.error(f"Error: {e}")
