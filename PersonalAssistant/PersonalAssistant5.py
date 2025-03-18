# with pyttsx3 interruption. Voice assitant can be interrupted using next question.

import pyttsx3
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, ServiceContext
from langchain_openai import ChatOpenAI
from llama_index.core import StorageContext, load_index_from_storage
import speech_recognition
import os
import time
import keyboard
import multiprocessing

os.environ['OPENAI_API_KEY'] = 'your openAI API key'  
data_directory = r'data'
index_directory = r'index.json'
engine = pyttsx3.init()
engine.setProperty("rate", 130)
UserVoiceRecognizer = speech_recognition.Recognizer()


def sayFunc(phrase):
    engine.say(phrase)
    engine.runAndWait()
p = multiprocessing.Process(target=sayFunc, args=("Hi",))

def get_audio(phrase):
    global p
    if p.is_alive():
        #engine.stop()
        p.terminate()
    p = multiprocessing.Process(target=sayFunc, args=(phrase,))
    p.start()
    
    


def speechtotext():
    global UserVoiceInput  
    try:
        with speech_recognition.Microphone() as Source:
            UserVoiceInput = UserVoiceRecognizer.listen(Source)
            UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput).lower()
        return UserVoiceInput_converted_to_Text           
    
    except speech_recognition.UnknownValueError:
        return "No user voice"

def update_knowledge(directory_path = data_directory, index_path=index_directory):
    # Initialize LlamaIndex
    llm=ChatOpenAI(temperature=0.5, model_name="gpt-4")
    # Read documents from the directory
    documents = SimpleDirectoryReader(directory_path).load_data()
    # Create the knowledge base index
    index = VectorStoreIndex.from_documents(documents, llm = llm)
    # Save the index for future use
    index.storage_context.persist(persist_dir=index_path)
    print("Knowledge base updated.")
    return index

def answer_question(question, index_path=index_directory):
    #rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir=index_path)
    # load index
    index = load_index_from_storage(storage_context)
    query_engine = index.as_chat_engine()
    response = query_engine.chat(query)
    # Provide the answer
    get_audio(response.response)
    print(f"Ratna: {response.response}")
    return response.response

if __name__ == "__main__":
    os.system('cls')
    update_knowledge()
    welcome_message = "Hi welcome to department's personal assistant, I am Ratna"
    get_audio(welcome_message)
    print(welcome_message)


    while True:
        query = speechtotext()
        print("You:", query)
        if "thank you" in query or 'thankyou' in query or 'thank' in query or 'thanks' in query:
            print("You are welcome")
            get_audio("You are welcome")
            break
        if query != "No user voice":
            answer_question(query)
    exit(0)
    
        
        
         
    