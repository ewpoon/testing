print("trying to push some code")
print("try to edit")
print("whyyyy")
print('try')
print("cool")
print("shrimpy is so cool")
print("I agree")


# def read_file(file):
#     f = open(file, 'r')
#     lines = f.readlines()

#     f.close()
#     return lines


# from bs4 import BeautifulSoup

# def getSumSpanText(soup): #1
#     total = 0 #5
#     tagList = soup.find_all('span') #4

#     for tag in tagList: #2
#         total += int(tag.text) #9
#     return total #8

# <!DOCTYPE html> #4
# <html lang="en"> #10
# <head> #2
# <title>HTML Tutorial</title> #3
# </head> #9

# <body> #7
# <h1> This is a heading 1</h1> #8
# <p> THis is a paragraph </p> #5
# </body> #1
# </html> #6

# def user_counts(filename): #11
#     dir = os.path.dirname(__file__)
#     user_dict = dict() #6

#     with open(os.path.join(dir, fiilename)) as csv_file: #4
#         csv_reader = csv.reader(csv_file) #5 (this is wrong, should be 8)

#         for cols in csv_reader: #3
#             user = cols[3] #7 (should be 10)
#             user_dict[user] = user_dict.get(user,0) + 1 #2
#     return user_dict #1

