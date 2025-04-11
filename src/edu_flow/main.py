#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from .crews.edu_content_writer.edu_content_writer import EduContentWriter
from .crews.edu_research.edu_research import EduResearch
import os

class EduFlow(Flow):
    inputs = {
            "audience_level": "beginner",
            "topic": "fine-tuning LLMs"
        }
    @start()
    def generate_researched_content(self):
        return EduResearch().crew().kickoff(self.inputs).pydantic
        
        

    @listen(generate_researched_content)
    def generate_educational_content(self, plan):        
        final_content = []
        for section in plan.sections:
            writer_inputs = self.inputs.copy()
            writer_inputs['section'] = section.model_dump_json()
            final_content.append(EduContentWriter().crew().kickoff(writer_inputs).raw)
        print(final_content)


    @listen(generate_educational_content)
    def save_to_markdown(self, content):
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists
        
        # Use topic and audience_level from input_variables to create the file name
        topic = self.input_variables.get("topic")
        audience_level = self.input_variables.get("audience_level")
        file_name = f"{topic}_{audience_level}.md".replace(" ", "_")  # Replace spaces with underscores
        
        output_path = os.path.join(output_dir, file_name)
        
        with open(output_path, "w") as f:
            for section in content:
                f.write(section)
                f.write("\n\n")

def kickoff():
    edu_flow = EduFlow()
    edu_flow.kickoff()


def plot():
    edu_flow = EduFlow()
    edu_flow.plot()


if __name__ == "__main__":
    kickoff()
