from re import search
import re
 
#텍스트 정제(전처리)
def cleanText(readData):
    #텍스트에 포함되어 있는 특수 문자 제거
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text

f= open("text.txt", encoding='utf-8')
n= open("kakaochat_parsed.txt", "w",encoding='utf-8')

lines = f.readlines()[5:] #unneccesary information deleting (ex) export date)
i=0
for line in lines:
 
    if line =="\n": continue
    line = line.replace('\n',"")
    if line == None : continue
    if line.isspace() == True: continue
    if search('\d{4}년 \d{1}월 \d{1}일', line)!=None: continue
    if ("님이 들어왔습니다." in line): continue
    if ("님이 나갔습니다." in line): continue
    if ("삭제된 메시지" in line): continue
    if "운영정책을 위반한 메시지로 신고 접수 시 카카오톡 이용에 제한이 있을 수 있습니다" in line: continue
    if line=="사진": continue
    if (search('\d{4}. \d{1}. \d{1}. 오', line) or search('\d{4}. \d{1}. \d{2}. 오', line)) or (search('\d{4}. \d{2}. \d{1}. 오', line) or search('\d{4}. \d{2}. \d{2}. 오', line))!=None:
        line=line.split(" : ")[1]
        if line=="사진": continue
        elif line.isspace() == True: continue
    line= cleanText(line)
    n.write(line+"\n")
    
f.close()
n.close()
