"""Given a string s and an integer k, break up the string into multiple texts
such that each text has a length of k or less. You must break it up so that
words don't break across lines. If there's no way to break the text up, then 
return null.

You can assume that there are no spaces at the ends of the string and that 
there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and
k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy",
"dog"]. No string in the list has a length of more than 10."""

def formatter(string, k):
    words = string.split(" ")
    output = []
    prev_phrase = ""
    for idx, word in enumerate(words):
        if len(word) > k:
            return None
        cur_phrase = " ".join([prev_phrase, word]) if prev_phrase else word
        if len(cur_phrase) <= k:
            prev_phrase = cur_phrase
        else:
            output.append(prev_phrase)
            prev_phrase = word
    output.append(prev_phrase)
    return output

def test_formatter():
    assert formatter("the quick brown fox jumps over the lazy dog", 10) == \
    ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
    assert formatter("thequickbrownfox jumps over the lazy dog", 10) == \
    None
    assert formatter("the quick brown fox jumps over the lazy dog", 5) == \
    ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    assert formatter("the quick brown fox jumps over the lazy dog", 4) == \
    None

print(formatter("the quick brown fox jumps over the lazy dog", 10))
