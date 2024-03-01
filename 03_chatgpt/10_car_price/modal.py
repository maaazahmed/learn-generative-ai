from openai import OpenAI
from dotenv import dotenv_values
import json
from openai.types.beta.thread import Thread
from openai.types.beta.threads.run import Run
from openai.types.beta.threads.thread_message import ThreadMessage
import time
from openai.types.beta.assistant import Assistant

# **** GPT_MODEL **** #
GPT_MODEL = "gpt-3.5-turbo-1106"


OPENAI_API_KEY:str = dotenv_values(".env").get("OPENAI_API_KEY")
client:OpenAI = OpenAI(api_key=OPENAI_API_KEY)



def show_json(obj):
    return json.loads(obj.model_dump_json())


class AiAssistant:
    # thread:Thread
    # assistant:Assistant
    # message:ThreadMessage

    # def __init__(self, thread, assistant, message):
    #     self.thread = thread
    #     self.assistant = assistant
    #     self.message = message



    def create_assistant(self):
        file = client.files.create(
            file=open("cardata.pdf", "rb"),
            purpose="assistants"
        )
        assistant = client.beta.assistants.create(
            name="Student Support Assistant",
            instructions="You are a customer support chatbot. Use your knowledge base to best respond to client queries about car",
            model=GPT_MODEL,
            tools=[{"type":"retrieval"}],
            file_ids=[file.id]
        )
        return assistant



    def create_thread(self):
        thread = client.beta.threads.create()
        return thread


    def create_message(self, assistant, thread):
        self.message = client.beta.threads.messages.create(
            thread_id= thread.id, #self.thread.id,
            role="user",
            content=f"""what is Colour and Reg No of FORD GALAXY 2.0 TDCI ZETEC 6 SPEED 5 Door MPV *IMPORTED* No Reserve Retail Dealership Vehicle Direct""",
        )


        run:Run = client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=assistant,  #self.assistant.id,
            instructions="Please address the user as Pakistani. The user is the student of PIAIC."
        )


        while run.status == "queued" or run.status == "in_progress":
                print(run.status, "===")
                run = client.beta.threads.runs.retrieve(
                    thread_id=self.thread.id,
                    run_id=run.id,
                )
                time.sleep(0.5)
        print(run.status)



        messages:list[ThreadMessage] =  client.beta.threads.messages.list(
            thread_id=thread.id
        )

        for m in reversed(messages.data):
            print(m.role + " : "+m.content[0].text.value)






# thread_instance = Thread
# assistant_instance = Assistant
# message_instance = ThreadMessage

# # Create an instance of AiAssistant with specific values
# ai_assistant_instance = AiAssistant(thread_instance, assistant_instance, message_instance)

# # Call the create_message method to print the 'assistant' attribute
# # ai_assistant_instance.create_assistant()
# # ai_assistant_instance.create_thread()
# ai_assistant_instance.create_message(assistant="")



print("---------------------")
# AiAssistant().create_assistant()
# AiAssistant().create_thread()
# AiAssistant().create_message()