def mix(s1,s2):
    # Break strings into letters, keep only lowercase
    letters_one = [x for x in s1 if x.isupper() == False and x.isalpha() == True]
    letters_two = [x for x in s2 if x.isupper() == False and x.isalpha() == True]
    
    # Count and save letters that occur more than once
    dict_one = {}    
    for x in letters_one:
        count = letters_one.count(x)
        if count > 1:
            dict_one[x] = count
     
    dict_two = {} 
    for x in letters_two:
        count = letters_two.count(x)
        if count > 1:
            dict_two[x] = count
     
      
    # Find similarities and differences in dictionaries
    # Turn the differences into lists and then sort by their values      
    matches = set(dict_one.items()) & set(dict_two.items())
    diff1 = set(dict_one.items()) - set(dict_two.items())
    diff2 = set(dict_two.items()) - set(dict_one.items())
    diff1, diff2 = list(diff1), list(diff2)
    diff1.sort(key= lambda x: x[1], reverse=True)
    diff2.sort(key= lambda x: x[1], reverse=True)
    
    
    # Iterate through the differences and append the higher values into a list 
    # containing the string number it came from (1 or 2), the letter, and how many
    # occurances of the letter in the string
    collection = []
    
    # Index[0] set to 2 for easier sorting later
    for letter in diff1:
        if letter[0] in dict_two and dict_one[letter[0]] > dict_two[letter[0]]:
            collection.append([2, ord(letter[0]),dict_one[letter[0]]])
        elif letter[0] not in dict_two:
            collection.append([2, ord(letter[0]),dict_one[letter[0]]])
    
    # Index[0] set to 1 for easier sorting later
    for letter in diff2:
        if letter[0] in dict_one and dict_two[letter[0]] > dict_one[letter[0]]:
            collection.append([1, ord(letter[0]),dict_two[letter[0]]])
        elif letter[0] not in dict_one:
            collection.append([1, ord(letter[0]),dict_two[letter[0]]])
            
    for letter in matches:
        collection.append([0, ord(letter[0]), letter[1]])
       
    collection.sort(key=lambda x: x[1])
    collection.sort(key=lambda x: (x[2], x[0]), reverse=True)
    
    # Format data properly
    answer = []
    for item in collection:
        x = item[0]
        if x == 0:
            x = '='
        elif x == 1:
            x = '2'
        elif x == 2:
            x = '1'
        form = str(x) + ':' + str(chr(item[1])*item[2]) + '/'
        answer.append(form)
    try:
        answer[-1] = answer[-1][:-1]
    except IndexError:
        return ""
    
    return "".join(answer)


# Tests    
#mix("Are they here", "yes, they are here")
#mix("looping is fun but dangerous", "less dangerous than coding")
#mix(" In many languages", " there's a pair of functions")
#mix("Lords of the Fallen", "gamekult")
#mix("codewars", "codewars")
#mix("A generation must confront the looming ", "codewarrs")

# Test Answers    
'''
"2:eeeee/2:yy/=:hh/=:rr"
"1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
"1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
"1:ee/1:ll/1:oo")
""
"1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"
'''