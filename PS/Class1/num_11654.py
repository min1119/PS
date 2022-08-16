#아스키코드 ord()-알파벳to숫자,chr()-숫자to알파벳
#65~90는 알파벳 대문자AtoZ
#97~122는 알파벳 소문자atoz
while True:
    try:
        x=input()
        if type(x) ==str:
            print(ord(x))
    except:
        break
