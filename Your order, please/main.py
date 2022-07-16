def order(sentence):
    if len(sentence) > 0:
        l = [str(i) for i in range(1, len(sentence.split(' ')) + 1)]
        answer = list()
        for i in l:
                answer.append([word for word in sentence.split(' ') if i in word][0])
        return ' '.join(answer)
    else:
        return ''