import streamlit as st
from portfolio import Portfolio
from langchain_community.document_loaders import WebBaseLoader
from chain import Chain
def create_streamlit_app(llm, portfolio):
    st.title("Cold email Generator")
    url_input = st.text_input("Enter a URL:", value="https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/job/256481?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            # Load the page data
            loader = WebBaseLoader([url_input])
            page_data = loader.load().pop().page_content
            
            # Load portfolio data
            portfolio.load_portfolio()
            
            # Extract jobs from page data
            jobs = llm.extract_jobs(page_data)
            
            for job in jobs:
                # Extract 'skills' from the job data
                skills = job.get('skills', '')
                
                if skills:
                    # Query portfolio links based on skills
                    links = portfolio.query_links(skills)
                    # Generate cold email
                    email = llm.write_email(job, links)
                    st.code(email, language='markdown')
                else:
                    st.warning("No skills found in the job description.")
                    
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio)