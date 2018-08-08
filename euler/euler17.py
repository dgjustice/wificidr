num_words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    15: "fifteen",
    18: "eighteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    80: "eighty",
}

def print_tens(i):
    ones = i % 10
    if (i - ones) in num_words:
        tens = num_words[(i - ones)]
        return f"{tens}{num_words[ones]}"
    else:
        tens = i // 10
        one_str = str(num_words[ones]) if ones else ""
        return f"{num_words[tens]}ty{one_str}"

output = ""
for i in range(1, 1001):
    if i in num_words:
        output += num_words[i]
    elif i < 20:
        output += f"{num_words[i % 10]}teen"
    elif i < 100:
        output += print_tens(i)
    elif i < 1000:
        hundreds = i // 100
        tens = i % 100
        output += f"{num_words[hundreds]}hundred"
        if tens:
            output += "and"
            if tens in num_words:
                output += f"{num_words[tens]}"
            elif tens < 20:
                output += f"{num_words[i % 10]}teen"
            else:
                output += print_tens(tens)
    elif i == 1000:
        output += "onethousand"
    else:
        print("OOOOPS!")

print(output)
print(len(output))
