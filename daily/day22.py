"""
Given a dictionary of words and a string made up of those words (no spaces), return 
the original sentence in a list. If there is more than one possible reconstruction, 
return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words "quick", "brown", "the", "fox", and the string 
"thequickbrownfox", you should return ["the", "quick", "brown", "fox"].

Given the set of words "bed", "bath", "bedbath", "and", "beyond", and the string 
"bedbathandbeyond", return either ["bed", "bath", "and", "beyond] or ["bedbath", "and", "beyond"].
"""

def words(word_dict):
    string = word_dict["string"]
    word_set = word_dict["words"]
    out = []
    modified = True
    while modified:
        in_string = string
        remove = None
        for word in word_set:
            if string.startswith(word):
                out.append(word)
                string = string.replace(word, "", 1)
                remove = word
        if remove: word_set.remove(remove)
        if in_string == string: modified = False
    return out or None

def test_it():
    assert words({"words": {"quick", "brown", "the", "fox"}, "string": "thequickbrownfox"}) == ["the", "quick", "brown", "fox"]
    assert words({"words": {"bed", "bath", "bedbath", "and", "beyond"}, "string": "bedbathandbeyond"}) in [
        ["bed", "bath", "and", "beyond"],
        ["bedbath", "and", "beyond"]
    ]

# print(words({"words": {"quick", "brown", "the", "fox"}, "string": "thequickbrownfox"}))
# print(words({"words": {"bed", "bath", "bedbath", "and", "beyond"}, "string": "bedbathandbeyond"}))
