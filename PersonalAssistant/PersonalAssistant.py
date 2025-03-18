import pyttsx3
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, ServiceContext
from langchain_openai import ChatOpenAI
from llama_index.core import StorageContext, load_index_from_storage
import speech_recognition
import os
import time

os.environ['OPENAI_API_KEY'] = 'your openAI API key' 
data_directory = r'data'
index_directory = r'index.json'
engine = pyttsx3.init()
engine.setProperty("rate", 130)
UserVoiceRecognizer = speech_recognition.Recognizer()

def get_audio(text):
    # Convert text to speech
    engine.say(text)
    engine.runAndWait()  # Wait until the speech is finished
    


def speechtotext():
        
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
	# Query the index
  query = f"{question}"
  query_engine = index.as_query_engine()
  response = query_engine.query(query)
	# Provide the answer
  print(f"Ratna: {response.response}")
  return response.response

os.system('cls')
update_knowledge()
welcome_message = "Hi welcome to department's personal assistant, I am the ratna, how can i assist you?"
print(welcome_message)
get_audio(welcome_message)


while(1):
    query = speechtotext()
    if "ratna" in query:
        print("You:", query)
        answer = answer_question(query)
        get_audio(answer)
    if "thank you" in query or 'thankyou' in query:
        exit(0)
        
        
         
    