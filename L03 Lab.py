# Excercise 1
# 1.1 
# Below is a variable containing a string of letters. Use the 
# .replace() method to remove all vowels from txt and then print the result
# (a, e, i, o, and u are vowels.)
# documentation: https://www.w3schools.com/python/ref_string_replace.asp
text = "The quick brown fox jumps over the lazy dog. Jackdaws love my big sphinx of quartz."
text = text.replace("a", "")
text = text.replace("e", "")
text = text.replace("i", "")
text = text.replace("o", "")
print(text)

# 1.2
# Separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
# Hint: look up the .split() method https://www.w3schools.com/python/ref_string_split.asp
text = 'I LOVE how spring is super late this year and there are no flowers and it is cold and rainy.'


# 1.3
# Sometimes data has a bunch of extra whitespaces at the start or end
# Use .strip() method to remove them from the string below.
# ref: https://www.w3schools.com/python/ref_string_strip.asp
text = " hello world "


# Excercise 2
# Did you know you can create a dictionary like this:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Try it!

# 2.1
# Pick a book. Create a dictionary named book1 that represents the book, including key values
# for title, author, and year of publication. Make the year of publication an INT
# You may look up the book on wikipedia. 

# 2.2
# Print the title. 


# 2.3
# create a format string that says "<name of the book>  by <author> was published in 
# <year of publication>"
# Reminder: if you use " on the outside, you need to use ' on the inside and vice versa

# 2.4
# Then, add another entry for genre to the existing dictionary. 
# Then, Print the dictionary.

# 2.5
# Import the datetime library. Create a datetime object storing the year of
# publication using the dictionary you created earlier i.e. don't enter the
# year directly. For month and day, use Jan 1. Print the object

# 2.6
# Now choose two more books. You may look them up on wikipedia. Create a list
# of dictionaries that contain the title, author, and date of publication.


# 2.7
# Wasn't that a lot of work? Maybe there's a easier way. Create two seperate 
# dictionaries named book2 and book3 that contain the details from earlier.
# Now create an empty list and use the .append() method to add the dictionaries
# from earlier. Ref: https://www.w3schools.com/python/ref_list_append.asp
# (Yes the purpose of making you write the thing out long form is to highlight
# how useful a method is. Sorry.)