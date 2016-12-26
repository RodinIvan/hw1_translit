__author__ = 'Ivan'
import re
regrus = '[a-яёА-ЯЁ]'
reglat = '[a-zA-Z]'
regtags = '[><]'
regonlyrus = '[йцгшщзъфыплджэячьбюёЙЦГШЩЗЪФЫПЛДЖЭЯЧЬБЮЁ]'

filename = input("Введите название файла: ")

lines = open(filename + ".xhtml", encoding="utf8").readlines()
Cntlines = 1
d = {'e':'е', 'y':'у', 'u':'и', 'o':'о', 'p':'р', 'a':'а', 'k':'к', 'x':'х', 'c':'с', 'E':'Е', 'T':'Т', 'Y':'У', 'O':'О', 'P':'Р', 'A':'А', 'H':'Н', 'K':'К', 'X':'Х', 'C':'С', 'B':'В', 'M':'М'}
logfile = open(filename + "-log.txt", 'w', encoding = 'utf-8')
corrfile = open(filename + "-corr.txt", 'w', encoding = 'utf-8')
for line in lines:
    words = line.split(' ')
    Cntwords = 1
    for word in words:
        rus = False
        lat = False
        onlyrus = False
        onlylat = False
        tags = False
        if(re.search(regrus, word)):
            rus = True
            if(re.search(regonlyrus, word)):
                onlyrus = True
        if (re.search(reglat, word)):
            lat = True
        if(re.search(regtags, word)):
            tags = True
        if (onlyrus and lat):
            wt = []
            IsTagElement = False
            cnttagopen = 0
            cnttagclose = 0
            firstclosetagind = 0
            firstopentagind = 0
            for i in range(len(word)):
                if(word[i] == '>'):
                    firstclosetagind = i
                    break
            for i in range(len(word)):
                if(word[i] == '<'):
                    firstopentagind = i
                    break
            # print(firstclosetagind)
            for i in range(len(word)):
                if(word[i] == '<'):
                    IsTagElement = True
                    cnttagopen +=1
                if(word[i] == '>'):
                    IsTagElement = False
                    cnttagclose +=1
                if (IsTagElement):
                    wt.append(1)
                else:
                    wt.append(0)
            if((firstclosetagind<firstopentagind) or ((cnttagclose > cnttagopen)and cnttagopen == 0)):
                for j in range(0, firstclosetagind):
                    wt[j] = 1
            for i in range(len(word)):
                if((word[i] in d.keys() and wt[i] == 0)):
                    list1 = list(word)
                    list1[i] = d[word[i]]
                    word = ''.join(list1)
                    #word = word[0:i]+d[word[i]]+word[i+1:]
                    print ("В слове " + word + " на строке " + str(Cntlines) + " заменили букву " + word[i])
                    logfile.write("В слове " + word + " на строке " + str(Cntlines) + " заменили букву " + word[i] +"\n")
                    #print (wt)
                    #print (word)
        Cntwords += 1
    linecorr = " ".join(words)
    corrfile.write(linecorr + '\n')
    Cntlines+=1