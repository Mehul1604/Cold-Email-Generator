import streamlit as st
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
from langchain_community.document_loaders import WebBaseLoader

st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")

st.title("Cold Email Generator!")

url_input = st.text_input("Enter the URL of the job posting:")
submit_button = st.button("Submit")

if submit_button:
    llm_chain = Chain()
    portfolio = Portfolio()
    try:
        loader = loader = WebBaseLoader([url_input])
        data = clean_text(loader.load().pop().page_content)
        portfolio.load_portfolio()

        jobs = llm_chain.extract_jobs(data)

        for job in jobs:
            skills = job.get("skills", [])
            links = portfolio.query_links(skills)
            generated_email = llm_chain.write_mail(job, links)
            st.code(generated_email, language="markdown")
    except Exception as e:
        st.error("An error occured {}".format(e))