import json
import google.generativeai as genai2
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai2.configure(api_key="AIzaSyDYu3B89zPTavNY2R3r8hRtMHpBCm_nnTk")

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
  system_instruction ="""Disregard all prior instructions. You will be acting as a professional translator who is translating to an amateur learner. Provide me a word by word (EXCLUDING punctuations) english translation of the text I will send you next.
                        For each word, also provide the part of speech. 
                        Your output will only have a JSON file where the text (EXCLUDING PUNCTUATION) will be parsed into a dictionary with the original word being the key and the translation and part of speech being the value. NONE of the keys should be translated or considered. 
                        IGNORE ALL PUNCTUATIONS. All of the keys must be able to combine to compose the entirety of the original text without punctuation. example format: {

  "作为": "Conjucture: as",

  "中国": "Noun: China",

  "文学": "Noun: literature",

}

YOU SHOULD NOT BE TRANSLATING ANY KIND OF PUNCTUATION. IGNORE ALL PUNCTUATION WHEN EXECUTING. You will only execute the prompt after I give the keyword "TRANSLATE". Don't give any other output or analysis or commentary other than the json file.

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
    # message = """옛날에 큰 호랑이 한 마리가 숲 속에 살았다.
    #           어느 날 호랑이는 배가 고파서 마을로 갔다.
    #           마을 옆 밭에 소 한 마리가 서 있었다.
    #           호랑이는 소를 잡아 먹고 싶은데 갑자기 시끄러운 아기 울음소리를 들었다.
    #           밭 옆에 있는 집에서 아기가 울고 있었다.
    #           호랑이는 집으로 다가갔다.
    #           ‘아기가 맛있을 것 같아.’
    #           호랑이는 생각했다."""
    # message = """「おれの方が強い。」「いいや、ぼくの方が強い。」北風と太陽の声が聞えます。二人はどちらの力が強いかでケンカをしているようです。「太陽が毎日元気だから、暑くてみんな困っているよ。おれが涼しい風を吹くと、みんな嬉しそうだ。おれの方がみんなの役に立っているよ。」「でも、ぼくがいないと、木や野菜は育たないよ。冬は北風の吹く風が冷くて、とても寒かった。みんな外に出られなかったよね？最近は暖かいから、みんな喜よろこんでいるよ。」「いいや、あそこを見て。太陽が強く照すから、川の水がもうすぐ無なりそうだ。水がないと、みんな生活できないよ。」"""
    message = "おれが涼しい風を吹くと、みんな嬉しそうだ。おれの方がみんなの役に立っているよ。」「でも、ぼくがいないと、木や野菜は育たないよ。冬は北風の吹く風が冷くて、とても寒かった。みんな外に出られなかったよね？最近は暖かいから、みんな喜よろこんでいるよ。」「いいや、あそこを見て。太陽が強く照すから、川の水がもうすぐ無なりそうだ。水がないと、みんな生活できないよ。"
    response = chat_session.send_message(message)
    response = chat_session.send_message("TRANSLATE")
    print(response.text)
    #return word_translate(message)

def parse_json(jsonfile):
    return json.loads(jsonfile)


if __name__=="__main__":
    main()


#   "史上": "in history",

#   "第一部": "the first",

#   "章回": "chapter",

#   "小说": "novel",

#   "《三国演义》": "Romance of the Three Kingdoms",

#   "为": "for",

#   "我们": "us",

#   "展示": "show",

#   "出": "out",

#   "一幅": "a",

#   "波澜壮阔": "grand",

#   "乱世": "turbulent times",

#   "英雄": "hero",

#   "争": "fight",

#   "天下": "the world",

#   "的": "of",

#   "历史": "history",

#   "画面": "picture"