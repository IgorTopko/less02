value_one = "i Love Python"
value_two = "Thank You So Much"
value_three = "This Is Really Cool"

hashtag_one = "#" + "".join(value_one.split())
hashtag_two = "#" + "".join(value_two.split())
hashtag_three = "#" + "".join(value_three.split())

if len(hashtag_one) > 140:
    hashtag_one = hashtag_one[:140]
elif len(hashtag_two) > 140:
    hashtag_two = hashtag_two[:140]
elif len(hashtag_three) > 140:
    hashtag_three = hashtag_three[:140]
print(hashtag_one)
print(hashtag_two)
print(hashtag_three)