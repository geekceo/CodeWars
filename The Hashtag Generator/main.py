def generate_hashtag(s):
    return '#' + ''.join([word.title() for word in s.split(' ')]) if s and len(s) < 145 else False