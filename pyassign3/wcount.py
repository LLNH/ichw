"""wcount.py: count words from an Internet file.

__author__ = "Huang Yihan"
__pkuid__  = "1700011798"
__email__  = "1924366526@pku.edu.cn"
"""
import sys
import urllib.request
from urllib.request import urlopen
def retrieve_page(url):
    """ Retrieve the contents(bytes) of a web page.
        The contents is decoded to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = my_socket.read().decode()
    my_socket.close()
    return dta


def icount(_list,_str):
    x = 0
    for m in _list:
        if len(m) == len(_str):
            n = 0
            while True:
                if n == len(m) or m[n] != _str[n]:
                    break
                if m[n] == _str[n] and n == len(m)-1:
                    x = x + 1
                n = n+1
    return x

def wcount(lines, topn):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    word = ''
    for i in lines:
        if 65<=ord(i) and ord(i)<=90:
            word = word + i 
        elif 97<=ord(i) and ord(i)<=122:
            word = word + i
        else:
            word = word + ' '     
    word = word.split()
    #提取不重复的单词
    alreadyknown = []
    for m in word:
        if m not in alreadyknown:
            alreadyknown.append(m)
    #分别数数，排序，建构字典
    empty = []
    final = {}
    final2 = {}
    for j in alreadyknown:
        number = icount(word,j)
        final[j]=number
        final2[str(number)]=j
        empty.append(number)
    empty.sort()
    empty.reverse()
    last_step = empty[:10]
    #通过数字找到对应word
    last_str = ''
    for y in last_step:
        z = final2[str(y)]
        last_str += z + "\t" + str(y) + "\n"
    return last_str    
        

pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)

