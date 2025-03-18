from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, ServiceContext
from langchain_openai import ChatOpenAI
from llama_index.core import StorageContext, load_index_from_storage
import os


os.environ['OPENAI_API_KEY'] = 'your openAI API key'  
data_directory = r'data'
index_directory = r'index.json'

def update_knowledge(directory_path = data_directory, index_path=index_directory):
  # Initialize LlamaIndex
  llm=ChatOpenAI(temperature=0, model_name="gpt-4")
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
  print(f"Answer: {response.response}")
  return response.response

#update_knowledge()
#question = input("Enter your query: ")
#answer_question(question)