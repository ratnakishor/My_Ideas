from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai

url = input("Enter youtube video url: ")

genai.configure(api_key="your_google_api_key")

model = genai.GenerativeModel("gemini-1.5-flash")

def get_transcript(url):
	
	video_id = url.split("=",1)[1]

	transcript = YouTubeTranscriptApi.get_transcript(video_id)

	text = ""

	for d in transcript:
		text = text + " " + d["text"]
	return text

def generate_summary(text):

	prompt = '''Please analyze the follwoing youtube video transcription and provide the following analysis:
        1. A concise summary of the video content in a single sentence.
        2. The most important topics or key points discussed with tick mark bullet points
        3. The likely target audience for this video with tick mark bullet points
        4. Suggested max 3 keywords or tags with comma separation that would better represent this video
        The youtube video transcription text: 
        ''' + text

	response = model.generate_content(prompt)

	result = response.text

	result = result.replace("*","")

	return result

video_id = url.split("=")[1]

text = get_transcript(url)

content = generate_summary(text)

print(content)
