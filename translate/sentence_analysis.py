import json
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai.configure(api_key="AIzaSyCcBmgGrY_mN9Ezd1KPyCr_E5hNlOKEKCE")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction = """Disregard all previous prompts. You will be acting as a professional translator who is translating to an amateur learner. Do not respond until I prompt you. 
                          I will later provide lines of text for you in a language. 
                          Analyze the grammar and the sentence structure in detail line by line for every sentence. 
                          After analyzing, give the direct translation. Please respond back in English that still reflects the original tone and structure. 
                          Put the response of your analysis in English in JSON format. Even for the nested key value pairs, recursively change the key into English. 
                          Also for each of the words and/or phrases from the original language, put a corresponding English word/phrase by recursively adding English next to the original language. 
                          Use this JSON schema: 
                          sentences = {Sentence: “original sentence”, Translation: “translated sentence”, Grammatical structure: “grammar”, Analysis: “translated analysis of the entire sentence, not individual words” }
                          Return: list[sentences] 
                          You should respond back in English when I say PLEASE HELP.
                          """,
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

def sentence_translate(original_text: str) -> json:
    response = chat_session.send_message(original_text)
    response = chat_session.send_message("PLEASE HELP")
    return response.json
    
def main():
    #message = "作为中国文学史上第一部章回小说，《三国演义》为我们展示出了一幅波澜壮阔乱世英雄争天下的历史画面，故事情节随着几大人物阵营的演变紧紧抓牢看客眼球。那么随着时间推移，三国人物阵营是怎样变化的呢？狗熊会根据《三国演义》原著电子版汉语文本，应用文本分析、关联规则挖掘和社区探测技术，从数据角度分析三国各个时期的人物阵营情况。"
    message = """옛날에 큰 호랑이 한 마리가 숲 속에 살았다.
              어느 날 호랑이는 배가 고파서 마을로 갔다.
              마을 옆 밭에 소 한 마리가 서 있었다.
              호랑이는 소를 잡아 먹고 싶은데 갑자기 시끄러운 아기 울음소리를 들었다.
              밭 옆에 있는 집에서 아기가 울고 있었다.
              호랑이는 집으로 다가갔다.
              ‘아기가 맛있을 것 같아.’
              호랑이는 생각했다."""
    response = chat_session.send_message(message)
    response = chat_session.send_message("PLEASE HELP")
    #print(response.text)
    print(parse_json(response.text))


def parse_json(some_file):
    return json.loads(some_file)

if __name__ == "__main__":
    main()
    