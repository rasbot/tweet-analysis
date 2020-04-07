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