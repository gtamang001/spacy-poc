with open('./data/Answers.csv','r',encoding='ISO-8859-1') as ans:
    line_count = 0
    for i in range(101):
        print(ans.readline())
        line_count +=1
