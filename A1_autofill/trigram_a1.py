import re
from collections import defaultdict

data = open("data2.txt").read().lower()
sentences = re.split('[\n,.@*()#]', data)


# remove any unuseful words
def remove_any_unuseful_words(tokens):
    meaningful_words = [w for w in tokens if not w in ['', "'", '"', '\\', '*', '@', ' ']]
    return meaningful_words


sentences = remove_any_unuseful_words(sentences)

# print(sentences)

# data2 = remove_any_unuseful_words(data.split())
# print(len(data.split()))
# print(len(data2))


model = defaultdict(lambda: defaultdict(lambda: 0))

# Count frequency of co-occurance
for sentence in sentences:
    for listTrigrams in [sentence.split()[i:i + 3] for i in range(len(sentence.split()) - 3 + 1)]:
        model[(listTrigrams[0], listTrigrams[1])][listTrigrams[2]] += 1

# Let's transform the counts to probabilities
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count


# print(dict(model["and","animals"]))

# Create Prediction function using trigrams
def predict_word(w1, w2):
    sort_model = sorted(dict(model[w1.lower(), w2.lower()]).items(), key=lambda x: x[1], reverse=True)
    predictedList = []
    # for item in sort_model:
    #     print(item)
    if len(sort_model) < 5:
        for word in sort_model:
            predictedList.append(word[0])
    else:
        for i in range(5):
            predictedList.append(sort_model[i][0])

    return predictedList
