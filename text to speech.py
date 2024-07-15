
import nltk
from newspaper import Article
from gtts import gTTS
import os

post = Article('https://www.codingninjas.com/studio/library/building-a-qr-code-generator-in-python')

post.download()
post.parse()



nltk.download('punkt')
post.nlp()



txt = post.text



language = 'en' 

obj = gTTS(text=txt, lang=language, slow=False)
