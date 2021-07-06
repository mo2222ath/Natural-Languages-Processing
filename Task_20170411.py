 # Moaaz Hasan - 20170411 CS-IS-1
 # NLP Task

def is_cat_or_dog(word):
    dog = wn.synset('dog.n.01')
    cat = wn.synset('cat.n.01')

    dog_similar = wn.synset(word.split()[0] +'.n.01').wup_similarity(dog)
    cat_similar = wn.synset(word.split()[0] +'.n.01').wup_similarity(cat)

    answer = word + ' is not a cat or dog'
    print('dog_similar: ' , dog_similar)
    print('cat_similar: ' , cat_similar)

    if dog_similar > cat_similar and dog_similar >= 0.80:
      answer = 'dog'
    elif cat_similar > dog_similar and cat_similar >= 0.80:
      answer = 'cat'

    return answer


word = input('Enter the word:')
result = is_cat_or_dog(word)
print(result)