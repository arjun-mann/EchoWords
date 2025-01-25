import google.generativeai as genai3
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai3.configure(api_key="AIzaSyDYu3B89zPTavNY2R3r8hRtMHpBCm_nnTk")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai3.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction = """Disregard all previous prompts. You will be acting as a professional translator who is translating to an amateur learner. 
                          Do not respond until I prompt you. I will later provide lines of text for you in a foreign language. 
                          When prompted with the word "RESPOND," please provide the translated text in English and nothing else. 
                          Make sure that the english translated version still reflects the original tone and structure. 
                          When prompted, do not provide anything else EXCEPT for the translated English version of the original text""",
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
    # message = """옛날에 큰 호랑이 한 마리가 숲 속에 살았다.
    #           어느 날 호랑이는 배가 고파서 마을로 갔다.
    #           마을 옆 밭에 소 한 마리가 서 있었다.
    #           호랑이는 소를 잡아 먹고 싶은데 갑자기 시끄러운 아기 울음소리를 들었다.
    #           밭 옆에 있는 집에서 아기가 울고 있었다.
    #           호랑이는 집으로 다가갔다.
    #           ‘아기가 맛있을 것 같아.’
    #           호랑이는 생각했다."""
    print(message)
    response = chat_session.send_message(message)
    response = chat_session.send_message("RESPOND")
    print(response.text)

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
    
    
