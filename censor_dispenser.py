#!/usr/bin/env  python

#The solution below has some problems due to the simplicity of the assignment, importing the "re"
#library and working with that would solve a lot of issues but this solution is supposed to showcase
#the basic things learned in the beginnings of the tutorial

#starting variables
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#lists to censor words or terms from
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]
terms_and_words = proprietary_terms + negative_words

#Included to exclude punctuation from being censored. Some things (like "'") are left out because it
#is better to censor them here
punctuation = [" ", ".", "," , ";", ":", "\n"]

#function to help with casing, extracted into a separate function for convenience
def lst_casing(lst):
    temp_lst = []
    for item in lst:
        temp_lst.append(item.title())
    lst += temp_lst
    return lst

#function to clean up the censoring of words, makes sure every character is actually censored
def censor_cleanup(email):
    email_chars = []
    email_cleaned = ""
    for i in range(len(email)):
        email_chars.append(email[i])
    for i in range(len(email_chars)-1):
        if email_chars[i] == "*" and email_chars[i+1] not in punctuation:
            email_chars[i+1] = "*"
    for i in email_chars:
        email_cleaned += i
    return email_cleaned

#first function, named censor_one for easier navigation
#Written so that it is reusable to censor different terms, slight deviation from the
#simpler requirements of the original assignment

def censor_one(email, term):
    temp = email
    term_cased = [word, term.title()]
    for term in term_cased:
        email_censored = temp.replace(term, len(term)*"*")
        temp = email_censored
    email_censored = censor_cleanup(temp)
    return email_censored

#print-statements for testing purposes
#print("EMAIL ONE: \n", email_one)
#print("EMAIL ONE, CENSORED: \n"censor_one(email_one, "learning algorithms"))

def censor_two(email, term_lst):
    temp = email
    cased_lst = lst_casing(term_lst) #lst_casing is a separate function found at the bottom of the code
    for item in cased_lst:
        email_censored = temp.replace(item, len(item)*"*")
        temp = email_censored
    email_censored = censor_cleanup(temp)
    return email_censored

#print-statements for testing purposes
#print("EMAIL TWO: \n", email_two)
#print("EMAIL TWO, CENSORED: \n" , censor_two(email_two, proprietary_terms))

def censor_three(email, word_lst, term_lst):
    counter = 0
    temp = email
    cased_word_lst = lst_casing(word_lst)
    cased_term_lst = lst_casing(term_lst)
    for word in cased_word_lst:
        if counter < 2 and email.find(word) != -1:
            counter += 1
        else: 
            email_censored = temp.replace(word, len(word)*"*")
            temp = email_censored
    for term in cased_term_lst:
        email_censored = temp.replace(term, len(term)*"*")
        temp = email_censored
    email_censored = censor_cleanup(temp)
    return email_censored

#print-statements for testing purposes
#print("EMAIL THREE: \n", email_three)
#print("EMAIL THREE, CENSORED: \n", censor_three(email_three, negative_words, proprietary_terms))

def censor_four(email, lst):
    temp = censor_two(email, lst) #calling function censor_two instead of writing the same code twice
    email_lst = temp.split(" ")
    pos_marker = []
    email_censored = ""
    for i in range(len(email_lst)-1):
        if "*" in email_lst[i]:
            pos_marker.append(i-1)
            pos_marker.append(i+1)
    for pos in pos_marker:
        email_lst[pos] = len(email_lst[pos])*"*"
    for item in email_lst:
        email_censored += item
        email_censored += " "
    return email_censored

#print-statements for testing purposes, inlcuding using censor_two on email_four to showcase the functionality of censour_four
#print("EMAIL FOUR:\n", email_four)
#print("EMAIL FOUR, LIGHTLY CENSORED:\n", censor_two(email_four, terms_and_words))
#print("EMAIL FOUR, CENSORED:\n", censor_four(email_four, terms_and_words))

