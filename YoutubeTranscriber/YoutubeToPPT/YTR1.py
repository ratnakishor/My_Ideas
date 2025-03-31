from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import streamlit as st
import streamlit.components.v1 as components

# Getting video transcript

#url = input("Enter youtube video url: ")

genai.configure(api_key="your_google_api_key")

model = genai.GenerativeModel("gemini-1.5-flash")



def get_transcript(url):
	
	video_id = url.split("=")[1]

	transcript = YouTubeTranscriptApi.get_transcript(video_id)

	text = ""

	for d in transcript:
		text = text + " " + d["text"]
	return text

# Gemini-pro

def generate_ppt(text):

	prompt = "Please create the content for power point presentation following text, suggest best title for it. And also explain each concept" + text

	response = model.generate_content(prompt)

	result = response.text

	result = result.replace("*","")

	return result


st.sidebar.title("PPT Content Generator From an Youtube Video")

url = st.sidebar.text_input("Enter url: ")

st.markdown("# ")

components.html("<html><body><h2 style = color:brown><-- Enter Youtube video url to get presentation content</h2></body></html>")

if len(url) > 0:

	video_id = url.split("=")[1]

	st.sidebar.image(f"http://img.youtube.com/vi/{video_id}/hqdefault.jpg") 

	text = get_transcript(url)

	content = generate_ppt(text)

	st.write(content)





	
