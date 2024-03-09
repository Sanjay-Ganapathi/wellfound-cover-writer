import os
from crewai import Agent
from textwrap import dedent
from langchain_community.llms import OpenAI, Ollama, AzureOpenAI
from langchain_openai import ChatOpenAI, AzureChatOpenAI
from tools.pdf2text import PDFToTextTool
from tools.currentdate import GetCurrentDate
from crewai_tools import SeleniumScrapingTool
scarpe_wb = SeleniumScrapingTool()


class WellFoundCoverAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.AzureOAIGPT4 = AzureChatOpenAI(
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            api_key=os.getenv("AZURE_OPENAI_APIKEY"),
            openai_api_version="2024-02-15-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            model_name="gpt-4-32k",
            temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def resume_analysis_agent(self):
        return Agent(
            role="Resume Analysis Agent",
            backstory=dedent(f"""Have Decades of experience and Employ advanced natural language processing to meticulously scan and extract key details from resumes. I efficiently identify skills, experiences, and achievements, providing valuable insights to enhance the cover letter creation process."""),
            goal=dedent(f"""Analyze the content of the resume PDF, extracting key information such as skills, experiences,year of experience and achievements and every other things which can then be used to tailor the cover letter"""),
            tools=[PDFToTextTool.pdf2text, GetCurrentDate.getRealtimeDate],
            verbose=True,
            allow_delegation=False,
            llm=self.AzureOAIGPT4,
        )

    def job_analyzer_agent(self):
        return Agent(
            role="Job Analyser Agent",
            backstory=dedent(
                f"""Have decades of experience in analysis website content to provide relevant information according to the requirement"""),
            goal=dedent(f"""Parse information from the provided website link and analyze the job description then extract important keywords and requirements that addresses the specific needs of the position. """),
            tools=[scarpe_wb],
            allow_delegation=False,
            verbose=True,
            llm=self.AzureOAIGPT4,
        )

    def cover_letter_generator_agent(self):
        return Agent(
            role="Cover Letter Generator Agent",
            backstory=dedent(
                f"""Have experience in creating customized cover letters based on job descriptions and candidate resumes. I use advanced natural language processing techniques to highlight relevant skills, experiences, and achievements that match the job requirements."""),
            goal=dedent(f"""Generate a tailored cover letter based on the job description and candidate resume, highlighting the candidate's qualifications and suitability for the position."""),
            tools=[],
            allow_delegation=False,
            verbose=True,
            llm=self.AzureOAIGPT4,
        )
