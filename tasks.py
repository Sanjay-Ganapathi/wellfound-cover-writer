from crewai import Task
from textwrap import dedent


class WellFoundTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def resume_analysis(self, agent, resume_path):
        return Task(
            description=dedent(
                f"""
            Extract crucial information from the resume that is taken from the resume_path. The key details to be extracted 
            encompass a range of elements, such as skills, work experiences,year of experience, projects, achievements, 
            and any other pertinent information that holds significance for job applications. 
            This process is essential for efficiently evaluating a candidate's qualifications and 
            suitability for a particular job role. Also mention how the year of experience is calculated in detail at the bottom.
            Use appropriate tool to get the realtime date 
            {self.__tip_section()}
            **Parameters**: 
            - Resume full path : {resume_path}
            
        """
            ),
            expected_output="Full comprehensive resume content along with Year of Experience and how it was calculated mentioned at bottom.",
            async_execution=True,
            agent=agent,
        )

    def job_description_analysis(self, agent, job_url):
        return Task(
            description=dedent(
                f"""
            Analyze the job description from the provided URL and thoroughly examine
            to identify and extract key keywords and requirements. 
            This process includes isolating specific skills, qualifications, and attributes sought by the employer.
            Scrape the whole body of the provided URL 
                                       
            {self.__tip_section()}

            **Parameters**: 
            - Job Url : {job_url}
        """
            ),
            expected_output="Full comprehensive Job Description content along with required year of experience at the bottom",
            async_execution=True,
            agent=agent,
        )

    def generate_cover_letter(self, agent, context):
        return Task(
            description=dedent(
                f"""
            "Synthesize information from both the resume_analysis_agent and the job_analyzer_agent to craft a customized cover letter referencing the insights gathered from the two analyses.
            Convey why the candidate will be an excellent hire for this job.
            Establish the candidate as a qualified applicant in the first two lines of the cover letter. This should reflect the specific role the candidate is applying to and not be generic. Write what the candidate does and how it's relevant to the specific job listing.
            Use Clear and Direct Language.
            Do not fill the cover letter with jargon. Instead, be direct about the candidates qualifications and what the candidate is looking for with active language and simple short sentences.
            Quantify Impact 
            Instead of repeating the job history of the candidate, quantify the ways the candidate had an impact in previous roles. Providing numbers for the accomplishments builds trust in the resume and shows that the candidate is driven by results. 
            Proof Read 
            Spelling errors, poor sentence structure must not be there and grammar should be professional.
            Remember if the years of experience of candidate is less than the requirement of job description indicate how the candidate can stand out even with less experience and is suitable for the job
            
            {self.__tip_section()}
           
            
        """
            ),
            expected_output='Full length Cover letter ',
            context=context,
            agent=agent,
        )
