class style:
   BOLD = '\033[1m'
   END = '\033[0m'

def text_proess(test):

    greetings = ['morning,', 'night,', 'afternoon,', 'evening,','morning', 'night', 'afternoon', 'evening']
    greetings_re = ['morning!!', 'night!!', 'afternoon!!','evening!!','morning!!', 'night!!', 'afternoon!!','evening!!']
    greet1 = ['hows', 'whats', 'its']
    greet1_re = ["how's", "what's", "it's"]
    greet2 = ['welcome', 'hello', 'hi', 'hey']
    bold=['morning!!','hello,']

    list = test.split(" ")
    le_list = len(list)
    le_greetings = len(greetings)
    le_greet1 = len(greet1)
    le_greet2 = len(greet2)


    for i in range(0, le_list):
        for j in range(0, le_greetings):
            if list[i].lower() == greetings[j].lower():
                list[i] = greetings_re[j]

    for i in range(0, le_list):
        for j in range(0, le_greet1):
            if list[i].lower() == greet1[j].lower():
                list[i] = greet1_re[j]

    for i in range(0, le_list):
        for j in range(0, le_greet2):
            if list[i].lower() == greet2[j].lower():
                list[i] = list[i] + ','

    for i in range(0, le_list):
        if list[i].lower() in bold:
            print(style.BOLD + list[i] +style.END)
            sys.stdout.flush()
        else:
            print(list[i])
            sys.stdout.flush()
    

from gingerit.gingerit import GingerIt

text = 'good morning'
parser = GingerIt()
str=parser.parse(text)['result']
str1=parser.parse(str)['result']

if len(str)>len(str1):
    text_proess(str)
else:
    text_proess(str1)

