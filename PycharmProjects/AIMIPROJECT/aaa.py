##### 데이터 불러와서 문장 단위로 쪼개기 #####
# data 폴더의 리뷰 크롤링 데이터 사용
# 파일 불러와서, 각 문장별로 쪼갠 것을 리스트화 해서 사용
import kss
from kiwipiepy import Kiwi
kiwi = Kiwi()

dir_list = ['./data/crawling_data.txt', './data/crawling_data2.txt', './data/crawling_data3.txt']

with open(dir_list[0], encoding='utf-8') as f:
    contents = f.read()

# 1. kss
# contents = kss.split_sentences(contents)  #이거왜안되는데...
# 2. kiwi
# normalize_coda : True인 경우 '먹었엌ㅋㅋ'처럼 받침이 덧붙어서 분석에 실패하는 경우, 받침을 분리하여 정규화합니다.
# return_tokens : True/False여부에 상관없이 내부적으로 형태소 분석 수행, 반환 시 포함/미포함 여부만 다름
    # return_tokens=True로 설정하는 게 문장 분리 후 따로 형태소 분석 수행하는 것보다 효율적
sents_list = kiwi.split_into_sents(contents, normalize_coda=True, return_tokens=True)
print(sents_list)
# >>> kiwi 성능이 꽤 괜찮은 듯?

# 품사 정보 세분화돼있음 > 대분류(첫글자)만 뽑아내기
# print(sents_list[0].tokens[0].tag[0])

# 문장만 포함된 리스트로 만들기
contents = []
for i in range(len(sents_list)):
    contents.append(sents_list[i].text)

##### 전처리 #####
# 특수문자 제거
import re
for i in range(len(contents)):
    contents[i] = re.sub('[^A-Za-z0-9가-힣 ]', '', contents[i])
# 맞춤법, 띄어쓰기 교정
from hanspell import spell_checker
for i in range(len(contents)):
    result = spell_checker.check(contents[i])
    contents[i] = result.checked


##### 문장 유사도 측정 #####
# tfidf 함수 생성
# idf : log()문서 n이 너무 커질 수 있기 때문
import scipy as sp

# TF-IDF는 TF와 IDF를 곱한 값을 의미 (return값!)
def tfidf(t, d, D):
    tf = float(d.count(t)) / sum(d.count(w) for w in set(d))
    idf = sp.log( float(len(D))/(len([doc for doc in D if t in doc])) )
    return tf * idf

# scikit-learn 의 TfidfVectorizer import
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(min_df=1, decode_error='ignore')

#### 글자수 짧은 문장 탈락시키기
tmp_list = []
for sentence in contents:
    if ' ' in sentence:
        tmp_list.append(sentence)
contents = tmp_list
print("contents after remove short sentences:", contents)

#### 키워드별 핵심 단어(ex.공부, 콘센트, 넓-) 포함된 문장만 남기기
keyword = ['공부','스터디','집중']
list = []
for sentence in contents:
    for i in range(0, 3):
        if keyword[i] in sentence:
            list.append(sentence)
print("contents after remove sentences without keyword:", list)

# 비교대상이 될 문장 리스트(contents) 벡터화
# 형태소 추출 후 띄어쓰기로 구분하여 하나의 문장으로 만들기
from konlpy.tag import Okt
t = Okt()
contents_tokens = [t.morphs(row, norm=True, stem=True) for row in list]

contents_for_vectorize = []
for content in contents_tokens:
    sentence = ''
    for word in content:
        sentence = sentence + ' ' + word
    # print(sentence)
    contents_for_vectorize.append(sentence)

# 벡터화
X = vectorizer.fit_transform(contents_for_vectorize)
num_samples, num_features = X.shape

# 비교 기준이 될 문장(new_post) 벡터화
# 형태소 분석 후 띄어쓰기로 구분하여 하나의 문장으로 만들기
new_post = ['공부하기 좋아요']
new_post_tokens = [t.morphs(row, norm=True, stem=True) for row in new_post]

new_post_for_vectorize = []
for content in new_post_tokens:
    sentence = ''
    for word in content:
        sentence = sentence + ' ' + word
    new_post_for_vectorize.append(sentence)
# transform
new_post_vec = vectorizer.transform(new_post_for_vectorize)

# 유사도 값 구하기
best_doc = None
best_dist = 65535
best_i = None

def dist_raw(v1, v2):
    delta = v1 - v2   # 벡터 사이의 거리를 구하기 위해 빼줌
    return sp.linalg.norm(delta.toarray())

for i in range(0, num_samples):
    post_vec = X.getrow(i)
    # 함수 호출
    d = dist_raw(post_vec, new_post_vec)
    print("== Post %i with dist=%.2f   : %s" % (i, d, list[i]))
    if d < best_dist:
        best_dist = d
        best_i = i

print("Best post is %i, dist = %.2f" % (best_i, best_dist))
print('-->', new_post)
print('---->', list[best_i])