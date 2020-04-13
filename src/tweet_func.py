def remove_empties(x):
    """input: a list of words
       output: a list of words with null or empty strings removed"""
    res = []
    for val in x:
        if val != '' and val != ' ':
            res.append(val)
    return res

def remove_stopwords(x, stop_words):
    """input: a list of words
       output: a list of words with stop_words removed"""
    valids = []
    words = x.split(' ')
    for word in words:
        if word not in stop_words:
            valids.append(word)
    return ' '.join(valids)

def clean_tags(x):
    """input: a list of either mentions or hashtags
       output: a list with special characters and numbers removed after the # or @"""
    filtered_list = []
    for word in x:
        cleaned_word = word[0]
        for char in word[1:]:
            if char.isalpha():
                cleaned_word += char
        filtered_list.append(cleaned_word)
    return filtered_list

def remove_phrase(x, leading_chars):
    """Removes phrases like mentions or hashtags from a list
    input: x - list
           leading_char - character like @ or #
    output: list without phrases"""
    filtered_list = []
    words = x.split(' ')
    for word in words:
        if word[:len(leading_chars)] != leading_chars:
            filtered_list.append(word)
    return ' '.join(filtered_list)

def filter_out_nonalpha(x):
    """Filter out special characters or numbers
    input: a list of words
    output: a list of strings only containing letters"""
    valids = []
    words = x.split(' ')
    for word in words:
        clean_word = ''
        for character in word:
            if character.isalpha() and character != 'ä' and character != 'ó' and character != 'ñ':
                clean_word += character
        if clean_word != 'amp':
            valids.append(clean_word)
    return ' '.join(valids)

def tweet_sentiment(x):
    """returns tweet sentiment for each tweet x"""
    if x > 0:
        return 'positive'
    elif x == 0:
        return 'neutral'
    else:
        return 'negative'

def match_pattern(input_list, pattern):
    import fnmatch
    return fnmatch.filter(input_list, pattern)

def get_tags(df, column):
    """gets all unique tags (hashtags or mentions) from a dataframe"""
    tag_list = []
    for tags in df[column]:
        if len(tags) != 0:
            for tag in tags:
                if tag not in tag_list:
                    tag_list.append(tag)
    return tag_list

def count_dictionary(lst):
    """gets count of all words in a list
    input: list of words
    return: dictionary of counts"""
    count_d = dict()
    for word in lst:
        if word not in count_d.keys():
            count_d[word] = 1
        else:
            count_d[word] += 1
    return count_d

def get_counts(x):
    count = 0
    if len(x) == 0:
        return 0
    for i in x:
        for j in i:
            count += 1
    return count

def get_unique_counts(x):
    unique_vals = []
    if len(x) == 0:
        return 0
    for i in x:
        for j in i:
            if j not in unique_vals:
                unique_vals.append(j)
    return len(unique_vals)