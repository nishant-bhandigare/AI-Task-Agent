import os
from dotenv import load_dotenv
from google import genai

# load environment variables
load_dotenv()

# initialize gemini api client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# read task from task.txt
def read_tasks(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# make a call to gemini api to get categorize tasks
def summarize_tasks(tasks):

    prompt = f"""
                You are a smart task planning agent.
                Given a list of tasks, categorize them into 3 priority buckets:
                - High Priority: Tasks that are critical and must be completed today.
                - Medium Priority: Tasks that are important and should be completed within the next few days.
                - Low Priority: Tasks that are not critical and can be completed later.

                The tasks are:
                {tasks}

                Return the categorization in the following format:
                High Priority: 
                - Task 1
                - Task 2
                - Task 3

                Medium Priority:
                - Task 4
                - Task 5

                Low Priority:
                - Task 6
                - Task 7
                """
    
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
    )

    return response.text


if __name__ == "__main__":
    tasks = read_tasks("tasks.txt")
    summarized_tasks = summarize_tasks(tasks)
    print(summarized_tasks)
