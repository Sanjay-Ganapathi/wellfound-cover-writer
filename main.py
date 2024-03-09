import os
from crewai import Agent, Task, Crew, Process
from textwrap import dedent
from agents import WellFoundCoverAgents
from tasks import WellFoundTasks
from dotenv import load_dotenv

load_dotenv()


class WellFoundCoverCrew:
    def __init__(self, resume_path, job_url):
        self.resume_path = resume_path
        self.job_url = job_url

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = WellFoundCoverAgents()
        tasks = WellFoundTasks()

        # Define your custom agents and tasks here
        resume_analysis_agent = agents.resume_analysis_agent()
        job_analyzer_agent = agents.job_analyzer_agent()
        cover_letter_generator_agent = agents.cover_letter_generator_agent()

        # Custom tasks include agent name and variables as input
        resume_analysis = tasks.resume_analysis(
            resume_analysis_agent,
            self.resume_path,

        )

        job_description_analysis = tasks.job_description_analysis(
            job_analyzer_agent,
            self.job_url,
        )
        generate_cover_letter = tasks.generate_cover_letter(
            cover_letter_generator_agent,
            context=[resume_analysis, job_description_analysis]
        )

        # Define your custom crew here
        crew = Crew(
            agents=[resume_analysis_agent, job_analyzer_agent,
                    cover_letter_generator_agent],
            tasks=[resume_analysis, job_description_analysis,
                   generate_cover_letter],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Wellfound Cover Writer")
    print("-------------------------------")
    resume_path = input(dedent("""Please input your resume path [PDF] """))
    job_url = input(
        dedent("""Please enter your wellfound job url [GET THE LINK FROM SHARE JOB] """))

    print(resume_path)
    custom_crew = WellFoundCoverCrew(resume_path, job_url)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is your cover letter")
    print("########################\n")
    print(result)
