# The Country Letters Riddle Checker

My partner always tells people this riddle when she first meets them, if things are a little awkward, and now so do I.

It's a quality riddle and leaves people stumped for a while, allowing you to either lavish in their pain or make a quiet escape from the conversation.

Problem is, especially if you message people the riddle, they'll just bombard you with countries. So I've written this handy script to check countries better.
But first...

## The Riddle

Capital letters can either be closed or open. A letter is closed if any part of the letter is entirely enclosed. The closed letters are:
- A
- B
- D
- O
- P
- Q
- R

There are five countries that when written out entirely in capital letters, only contain **OPEN** letters. Remember, we only consider capital letters here.

## The Script

You'll need Python to run it. You can find how to do that at: https://www.python.org/downloads/.

To run the script, enter your terminal from this directory and run:
```
./check.py ANY Country here "or if the country is many words"
```

The script will take a list of however many countries you want. The script will also capitalise the country for you.

As shown, if the country's name contains more than one word, you will need to put quotes around the name.

___

_**NOTE:** The script does not confirm you have entered a valid country and it will not correct typos. You need to know how to spell the country to get the correct answers._

_**MORE AGGRESSIVE NOTE:** I am very aware one could make an API call to grab the name of every country and then automate the check across all countries. This is cheating. Do not do this. Stop it._
