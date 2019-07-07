
#2-gram模型
import time
import re
start =time.clock()
txt = r"E:\新建文件夹\春秋左传.txt"  #以《春秋左传》文档为例。

txt1 = open(txt,"r",encoding="utf8")


#第一步，统计每个字出现的频次，存入一个dict.方便之后计算n-gram概率时作为除数。
char_freq ={}



for char in txt1.read():
    han=re.sub(r'[^\u4e00-\u9fff]',"",char)
    if han != "":                    #如果是汉字
        if han not in char_freq:  
            char_freq[str(han)] = 1
        else:
            char_freq[str(han)] = char_freq[str(han)] + 1



double_dic={}

#字典值初始化置零
for i in char_freq.keys():
    for j in char_freq.keys():
        double_dic[str(i)+str(j)] = 0

#print(double_dic["王"])

#read()一次后，要先关闭文件再打开，之后才能再read。
txt1.close()
txt1 = open(txt,"r",encoding="utf8")

string = txt1.read()

for x in range(len(string)-1):
    ix = string[x]
    ix_han = re.sub(r'[^\u4e00-\u9fff]',"",ix)
    jx = string[x+1]
    jx_han = re.sub(r'[^\u4e00-\u9fff]',"",jx)
    if (ix_han !="") and (jx_han !=""):
        double_dic[str(ix_han)+str(jx_han)] = double_dic[str(ix_han)+str(jx_han)] + 1

for key,value in double_dic.items():
    former_char = key[0]  #记录二字组的第一个字
    #print(former_char)
    double_dic[str(key)] = float(value) / float(char_freq[str(former_char)])  #从二元组的频次，到bi-gram的概率。
    




sorted_dic = sorted(double_dic.items(), key = lambda asd:asd[1], reverse = True)  #使得字典按value降序排列

output_txt = r"E:\新建文件夹\output.txt"
out = open(output_txt,"w",encoding="utf8")

for i in range(1000):
    bigram = sorted_dic[i][0]
    probability = sorted_dic[i][1]
    out.write(str(bigram)+"\t"+str(probability)+"\n")
         
end = time.clock()
time=end-start
print('Running time: %s Seconds'%(end-start))
txt1.close()
out.close()
