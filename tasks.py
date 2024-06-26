from crewai import Task
from agents import data_researcher, linkedin_post_writer, humanizer_agent

# create tasks

find_data = Task(
    description = "Generate information about the given project - {project} using the language model. Provide details which can be used to write LinkedIn posts about how the project was created from scratch. Ensure the information is accurate, informative, and useful.",
    expected_output = "A detailed and structured summary of the project - {project}, including key insights and steps on how it was created from scratch. The output should be ready to be used for writing LinkedIn posts, highlighting the main aspects of the project in a clear and engaging manner.",
    agent = data_researcher,
)


post_writing = Task(
    description = "Write a concise LinkedIn post about the project - {project} using the information generated by the language model. Include a short introduction about the project and the technologies used, followed by bullet points highlighting various tools and aspects along with other bullets to include the steps that can be used. Ensure the post is clear, engaging, and within 100-200 words, using emojis as well to make it appealing. Remember that that this is a personal project.",
    expected_output = "A concise and engaging LinkedIn post about the project - {project}, including a brief introduction about the project and the technologies used, followed by bullet points highlighting various tools and aspects along with steps that can be used. The post should be within 80-100 words and use emojis to enhance engagement and remember that this is a personal project, so generate accordingly.",
    agent = linkedin_post_writer,
)

humanizing_task = Task(
    description = "Humanize the LinkedIn post about the project - {project} generated by the post writer agent. Add personal touches, anecdotes, and real-life examples to make the post more relatable and engaging. Ensure the post is within 100-120 words and use emojis to enhance engagement. Make sure to use Linekdin's formatting options to make the post visually appealing, and use bullet points necessarily and it should be humanized perfectly",
    expected_output = "A humanized LinkedIn post about the project - {project}, enriched with personal touches, anecdotes, and real-life examples to increase audience engagement. The post should be within 100-120 words and use emojis to convey emotions and enhance engagement.",
    tools = [],
    agent = humanizer_agent,
    output_file = "linkedin_post.txt"
)


