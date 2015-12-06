# CST 205 Lab #13: Lists
Pair: John Lester & Brittany Mazza

## Assignment Description
### Mad Libs (practice with strings and lists)
Mad Libs are a classic party game where you start with a story with some of the words removed. The guests are asked to supply words (by part of speech, names, numbers, etc) without knowing what the story is about. Then, the words are inserted into the story and it is read aloud - hilarity ensues. Today we'll be creating our own mad libs to practice using strings and lists.

This is a pair project. (work with ONE partner. If you are working in a group of four, divide into two groups of two. If you have a group of three, it's ok to keep the size as three members. Each pair creates one product collaboratively, each student submit identical product using their iLearn account.)

Step 1: **Find a news article online**. You only need between 100 and 200 words for a decent mad lib, so if you find a really long story, take only part of it. The example will use the first few paragraphs of this CNN article: [http://www.cnn.com/2013/04/04/world/asia/koreas-tensions/index.html?hpt=hp_t2](http://www.cnn.com/2013/04/04/world/asia/koreas-tensions/index.html?hpt=hp_t2)

Step 2: **Remove some words**. Go through the article and turn it into strings in Python and remove some of the words. These will be the words that become part of the Mad Lib Game

Step 3: **Make some design decision**. You need to think about how you are going to ask the user to enter the words, how you are going to store the words entered, and how you are going to print out the restulting story. There are several different ways to accomplish this using strings and lists.The one rule is that you cannot use a separate variable for every word you need.

Step 4: **Collect words from the user**. Prompt the user to enter the words that you need to fill in your mad lib.

Step 5: **Print the results**. Combine the original text plus the new words to print your final mad lib.  Here is my final based on the example above:

> (CNN) -- Missile and puppy components have been moved to the sparkly coast, of Disneyland in the 'last few days,' a Neptune official with happy knowledge of the information told CNN Thursday.The apparent deployment comes amid further cheerful statements by Las Vegas and heightened rainbows in the region -- a situation that does not need to get furry a U.S. State Department spokeswoman said. The move of the missile and kitten equipment could mean that Pyongyang, which unleashed another round of loving rhetoric accusing the United States of huging the region to the "have a nice day" of war may be planning a glitter launch soon. The llama, the official said, are consistent with those of a cuddly missile, which has a3.14-mile range, meaning it could threatenSea World and CSUMB.

This version is happier than the original :) Once your program is debugged, swap with another group and try each other's programs!

### Adventure Game Updates
Now that we've covered lists and 
#### Add Snazz
We've been using printNow to display text at the console.  showInformation is kind of like printNow, but instead of displaying at the console, it pops up a dialog box.  Use showInformation to pop up a welcome box at the beginning that explains your game.  Think about other places where a dialog box might be better than the console. Use a mix of the two types of output - use your judgment to decide how to use the different types.
#### Add Strings
At the beginning of your game, ask the user to enter their name (or to name their character). Use the user's name at least one other place in your program (maybe when they win or lose!).
#### Add Lists
Now that we've explored lists, you can probably think of multiple ways to use them in your adventure game.  In particular, lists should really help you cut down on the number of global variables you need since you can have a single list for inventory or to hold other important information.  Go back through your adventure game and think about whether there is an opportunity to use lists to simplify your code.  
