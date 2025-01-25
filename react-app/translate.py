# import sys
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai.configure(api_key="AIzaSyCcBmgGrY_mN9Ezd1KPyCr_E5hNlOKEKCE")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instructions = """Disregard all previous prompts. You will be acting as a professional translator who is translating to an amateur learner. Do not respond until I prompt you. 
  I will later provide a paragraph of text for you in Chinese. 
  Analyze the grammar and the sentence structure in detail line by line for every sentence. 
  After analyzing, give the direct translation. 
  Please respond back in English that still reflects the original tone and structure. 
  Put the response of your analysis in English in JSON format. 
  Even for the nested key value pairs, recursively change the key into English. 
  Also for each of the Chinese words and/or phrases, put a corresponyding English word/phrase by recursively adding English next to Chinese. 
  For all the keys called “Original Sentence”, I want you to replace it with “Sentence” and a number corresponding to the sentence line. 
  You should respond back in English when I say PLEASE HELP.""",
  # Turn off safety so that the process won't be terminated.
  safety_settings={HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                   HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                   HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                   HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                   }
)

chat_session = model.start_chat(
  history=[
  ]
)

def main():
    message = "作为中国文学史上第一部章回小说，《三国演义》为我们展示出了一幅波澜壮阔乱世英雄争天下的历史画面，故事情节随着几大人物阵营的演变紧紧抓牢看客眼球。那么随着时间推移，三国人物阵营是怎样变化的呢？狗熊会根据《三国演义》原著电子版汉语文本，应用文本分析、关联规则挖掘和社区探测技术，从数据角度分析三国各个时期的人物阵营情况。"
    response = chat_session.send_message(message)
    response = chat_session.send_message("PLEASE HELP")
    print(response.text)
    # print(sys.path)

def your_translate_function(text): #DUMMY FUNCTION DO NOT EDIT
    # Dummy function to reverse the input text
    return text[::-1]

def your_analysis_function(text): #DUMMY FUNCTION DO NOT EDIT
    # Dummy function to analyze the input text
    word_count = len(text.split())
    char_count = len(text)
    char_frequency = {char: text.count(char) for char in set(text)}
    return {
        "word_count": word_count,
        "char_count": char_count,
        "char_frequency": char_frequency
    }


if __name__ == "__main__":
    main()
    
    
