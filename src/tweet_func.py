def letters(input):
    """Filter out special characters or numbers
    input: a list of words
    output: a list of strings only containing letters"""
    valids = []
    for character in input:
        if character.isalpha():
            valids.append(character)
    return ''.join(valids)

def count_dictionary(lst):
    count_d = dict()
    for word in lst:
        if word not in count_d.keys():
            count_d[word] = 1
        else:
            count_d[word] += 1
    return count_d

def filter_df(df, column, offset=0, agg=max):
    if offset == 0:
        if agg == min:
            return df[df[column] == df[column].min()]
        elif agg == max:
            return df[df[column] == df[column].max()]
        elif agg == mean:
            return df[df[column] == df[column].mean()]
        else:
            return "Hey there buddy!"
    else:
        if agg == min:
            return df[df[column] < df[column].min() + offset]
        elif agg == max:
            return df[df[column] > df[column].max() - offset]
        elif agg == mean:
            return df[df[column] == df[column].mean()]
        else:
            return "Woah there pal!"
        
def filter_tweets(df, column, keyword):
    """filter tweets in a dataframe to only those that
    contain the keyword provided"""
    return df[df[column].str.contains(keyword)]

def remove_empties(x):
    res = []
    for val in x:
        if val != '' and val != ' ':
            res.append(val)
    return res

def remove_stopwords(x, stop_words):
    valids = []
    for word in x:
        if word not in stop_words:
            valids.append(word)
    return valids

def remove_phrase(x, leading_char):
    """Removes phrases like mentions or hashtags from a list
    input: x - list
           leading_char - character like @ or #
    output: list without phrases"""
    filtered_list = []
    for word in x:
        if word[0] != leading_char:
            filtered_list.append(word)
    return filtered_list

def process_tweets(df, *args):
    """process tweet data by applying filters specified in args.
    choices are:
        get_mentions     = create column with @twitter_user mentions
        get_hashtags     = create column with #hashtag(s)
        split_tweets     = create column with a list of words from tweet
        lowercase        = force all letters to lowercase in split_tweets list
        remove_nonalpha  = removes special characters and numbers from list
        remove_stopwords = removes common words referencing stop_words list
        
        return: processed dataframe"""
    
    if 'get_mentions' in args:
        df['mentions'] = df['tweets'].str.findall(r'@.*?(?=\s|$)')
    if 'get_hashtags' in args:
        df['hashtags'] = df['tweets'].str.findall(r'#.*?(?=\s|$)')
    if 'split_tweets' in args:
        df['split_tweets'] = df['tweets'].str.split(' ')
        df['split_tweets'] = df['split_tweets'].apply(lambda x: list(remove_empties(x)))
    if 'remove_mentions' in args:
        df['split_tweets'] = df['split_tweets'].apply(lambda x: list(remove_phrase(x, '@')))
    if 'remove_hashtags' in args:
        df['split_tweets'] = df['split_tweets'].apply(lambda x: list(remove_phrase(x, '#')))
    if 'lowercase' in args:
        df['split_tweets'] = df['split_tweets'].apply(lambda x: list(map(str.lower, x)))
    if 'remove_nonalpha' in args:
        df['split_tweets'] = df['split_tweets'].apply(lambda x: list(map(t.letters, x)))
    if 'remove_stopwords' in args:
        df['split_tweets'] = df['split_tweets'].apply(lambda x: list(remove_stopwords(x, stop_words)))
    return df