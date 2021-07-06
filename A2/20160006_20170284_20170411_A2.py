import os
import sys
import pathlib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

documentPos = []
documentNeg = []

for path in pathlib.Path("/content/drive/MyDrive/nlp2/pos").iterdir():
    if path.is_file():
        current_file = open(path, "r")
        documentPos.append(str(current_file.read()))
        current_file.close()

for path in pathlib.Path("/content/drive/MyDrive/nlp2/neg").iterdir():
    if path.is_file():
        current_file = open(path, "r")
        documentNeg.append(str(current_file.read()))
        current_file.close()


document = documentPos + documentNeg

df = pd.DataFrame( document , columns=['text'])

labelpos = [1]*1000
labelneg = [0]*1000
label = labelpos + labelneg

df['label'] = label

# print(df.head())
# print(df)


X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                     ('clf', LinearSVC()),])


text_clf.fit(X_train, y_train)  


predictions = text_clf.predict(X_test)

print(metrics.accuracy_score(y_test,predictions))

text_clf.predict(['movie is good bad '])[0]

text_clf.predict(['I enjoy the movie '])[0]

text_clf.predict(['the movie disappointed but great'])[0]

indexes = y_test.index.tolist()
# len(indexes)

plt.clf()
plt.xlabel("Sample")
plt.ylabel("Review")
color = y_test.apply(lambda x: 'green' if x == 1 else 'red')
plt.scatter(indexes, y_test , c=color)
X = [0,250,500,750,1000,1250]
Y = [0.0,0.2,0.4,0.6,0.8,1]
plt.plot(X,Y)
plt.show()

indexes2 = df.index.tolist()

text = input('Enter text to predict: ')
res = text_clf.predict([text])[0]

if res == 0:
  print('This review is negative')
else:
  print('This review is postive')