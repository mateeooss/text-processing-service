import spacy
from transformers import pipeline, BertTokenizer, BertForTokenClassification
# Carrega o modelo spaCy para processamento de texto

class NerService:
    def __init__(self):
        # Inicializa o modelo de NLP, pode ser configurado aqui
        self.nlp = spacy.load("pt_core_news_lg")

    def process_text(self, sentencelist):
        list = [
            {
                "text": sentence['text'],
                "imagesUrl": sentence['imagesUrl'],
                "rootPath": sentence['rootPath'],
                "audioPath": sentence['audioPath'],
                "videoPath": sentence['videoPath'],
                "imagesPath": sentence['imagesPath'],
                "keyWords": [a.text for a in self.nlp(sentence['text']).ents]}
            for sentence in sentencelist
        ]

        return list