import warnings
warnings.filterwarnings('ignore')

'''
from transformers import pipeline

# GPT-2 기반 텍스트 생성 파이프라인 로드
generator = pipeline("text-generation", model="gpt2")

# 텍스트 생성
result = generator("Once upon a time", max_length=50, num_return_sequences=1)
print(result)

'''

'''
from transformers import pipeline

# 감정 분석 파이프라인 로드
sentiment_analysis = pipeline("sentiment-analysis")
result1 = sentiment_analysis("I love using Hugging Face!")
result2 = sentiment_analysis("I hate you!")
print(result1)
print(result2)
'''

'''
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
from scipy.spatial.distance import cosine

sentences = [
    "The quick brown fox jumps over the lazy dog",
    "I love playing with my pet dog",
    "The dog barks at the stranger",
    "The cat sleeps on the sofa",
]

processed = [simple_preprocess(sentence) for sentence in sentences]

model = Word2Vec(sentences=processed, vector_size=5, window=5, min_count=1, sg=0)

dog = model.wv['dog']
cat = model.wv['cat']

# 코사인 유사도 계산
similarity = 1 - cosine(dog, cat)
print(similarity)
'''


from transformers import BertModel, BertTokenizer
import torch
from scipy.spatial.distance import cosine

model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

sentences = [
    "The quick brown fox jumps over the lazy dog",
    "I am the king",
    "The fox leaps over a sleepy dog"
]

input1 = tokenizer(sentences[0], return_tensors='pt')
input2 = tokenizer(sentences[1], return_tensors='pt')
input3 = tokenizer(sentences[2], return_tensors='pt')

with torch.no_grad():
    output1 = model(**input1)
    output2 = model(**input2)
    output3 = model(**input3)
    
embedding1 = output1.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
embedding2 = output2.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
embedding3 = output3.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()

# 코사인 유사도 계산
similarity1 = 1 - cosine(embedding1, embedding2)
similarity2 = 1 - cosine(embedding1, embedding3)

print(f"Cosine similarity between the two sentences: {similarity1:.4f}")
print(f"Cosine similarity between the two sentences: {similarity2:.4f}")