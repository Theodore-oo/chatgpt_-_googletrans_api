from googletrans import Translator

text_ = str(input("Input English, Something you want to translate : "))
translator = Translator()
text_trans = translator.translate(text_, dest='my').text

print("Translate to Myanmar is : ", text_trans)
