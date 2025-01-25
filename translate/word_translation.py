import json
import google.generativeai as genai2
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai2.configure(api_key="")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai2.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction ="""Disregard all prior instructions. Can you give me a word by word english translation of the text I will send you next. Your output will only have a json file where the text will be parsed into a dictionary with the original word being the key and the translation being the value. All of the keys must be able to combine to compose the entirety of the original text, with nothing missing or added. example format: {

  "作为": "as",

  "中国": "China",

  "文学": "literature",

  "史上": "in history",

  "第一部": "the first",

  "章回": "chapter",

  "小说": "novel",

  "《三国演义》": "Romance of the Three Kingdoms",

  "为": "for",

  "我们": "us",

  "展示": "show",

  "出": "out",

  "一幅": "a",

  "波澜壮阔": "grand",

  "乱世": "turbulent times",

  "英雄": "hero",

  "争": "fight",

  "天下": "the world",

  "的": "of",

  "历史": "history",

  "画面": "picture"

}

You will only execute the prompt after I give the keyword "TRANSLATE". Don't give any other output or analysis or commentary other than the json file.


""" ,
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
def word_translate(msg):
    response = chat_session.send_message(msg)
    response = chat_session.send_message("TRANSLATE")
    return response.text

def main():
    message = """옛날에 큰 호랑이 한 마리가 숲 속에 살았다.
              어느 날 호랑이는 배가 고파서 마을로 갔다.
              마을 옆 밭에 소 한 마리가 서 있었다.
              호랑이는 소를 잡아 먹고 싶은데 갑자기 시끄러운 아기 울음소리를 들었다.
              밭 옆에 있는 집에서 아기가 울고 있었다.
              호랑이는 집으로 다가갔다.
              ‘아기가 맛있을 것 같아.’
              호랑이는 생각했다."""
    response = chat_session.send_message(message)
    response = chat_session.send_message("TRANSLATE")
    return word_translate(message)

def parse_json(jsonfile):
    return json.loads(jsonfile)


if __name__=="__main__":
    main()