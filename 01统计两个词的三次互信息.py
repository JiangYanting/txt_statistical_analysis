
#计算一段分词的文本中，5个词的距离内，两个词的三次互信息(忽略前后顺序)
import time
import math
start =time.clock()

def MI3(segment_txt):  #读入内容是一个txt文档
    segment_txt1 = open(segment_txt,"r",encoding="utf8")
    w_freq ={} #统计每个词出现的频次，存入一个dict，方便之后计算互信息概率.
    while(True):
        pagrah = segment_txt1.read(4096)
        if not pagrah:
            break
        pagrah_list = pagrah.split(" ")
        for w in pagrah_list:
            if w not in w_freq:
                w_freq[w] = 1
            else:
                w_freq[w] = w_freq[w] + 1   #"统计词频"
    segment_txt1.close()
    segment_txt1 = open(segment_txt,"r",encoding="utf8")
    bi_freq = {} #统计两个词相隔距离5以内的共现次数。
    while(True):
        pagrah = segment_txt1.read(4096)
        if not pagrah:
            break
        pagrah_list = pagrah.split(" ")
        for n in range(5,len(pagrah_list)-5,5):  #每隔5个确定一个坐标词，进行前后扫描
            for i in range(n,n+5,1):
                if pagrah_list[i] != "" and pagrah_list[n] != "" and pagrah_list[i] != " " and pagrah_list[n] != " ":
                    if (str(pagrah_list[n]) +" "+ str(pagrah_list[i]) not in bi_freq) and (str(pagrah_list[i]) +" "+ str(pagrah_list[n]) not in bi_freq):
                        bi_freq[str(pagrah_list[n]) +" "+str(pagrah_list[i])] = 1
                    else:  #正序、逆序不是都不在
                        if str(pagrah_list[n]) +" "+ str(pagrah_list[i]) in bi_freq: #正序在
                            bi_freq[str(pagrah_list[n]) +" "+ str(pagrah_list[i])] = bi_freq[str(pagrah_list[n]) +" " + str(pagrah_list[i])] + 1
                        else:  #逆序在
                            bi_freq[str(pagrah_list[i]) +" "+ str(pagrah_list[n])] = bi_freq[str(pagrah_list[i]) +" " + str(pagrah_list[n])] + 1
    mi3 = {}  #存储各搭配对的三次互信息值
    for k,v in bi_freq.items():
        two_words = str(k).split(" ")
        w1 = two_words[0]
        w2 = two_words[1]
        temp = math.pow(float(v),3) / float(w_freq[str(w1)]) / float(w_freq[str(w2)]) 
        mi3[str(w1)+"\t"+str(w2)] = temp
    output = r"/home/jiangyanting/宋代互信息.txt"
    output1 =open(output,"w",encoding="utf8")
    for k,v in mi3.items():
        k_list = k.split("\t")
        if k_list[0] != k_list[1]:  #是两个不同的词才输出
            output1.write(str(k)+"\t"+str(v)+"\n")
    output1.close()



txt = r"/home/jiangyanting/语料.txt"
MI3(txt)
        
        
end = time.clock()
print('Running time: %s Seconds'%(end-start))  #输出运行时间                    
                    
                
                
                
    
    
