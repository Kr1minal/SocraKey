from colored import fg
import random
import requests
import json

headers = {'authority': 'api.socrative.com','accept': '*/*','access-control-request-method': 'POST','access-control-request-headers': 'content-type','origin': 'https://b.socrative.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','sec-fetch-dest': 'empty','referer': 'https://b.socrative.com/','accept-language': 'en-US,en;q=0.9',}
headers2 = {'authority': 'api.socrative.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','content-type': 'application/json; charset=UTF-8','accept': '*/*','sec-gpc': '1','origin': 'https://b.socrative.com','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://b.socrative.com/','accept-language': 'en-US,en;q=0.9',}
headers3 = {'authority': 'api.socrative.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','accept': '*/*','sec-gpc': '1','origin': 'https://b.socrative.com','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://b.socrative.com/','accept-language': 'en-US,en;q=0.9',}
headers4 = {'Connection': 'keep-alive','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','Accept': '*/*','Sec-GPC': '1','Origin': 'https://b.socrative.com','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://b.socrative.com/','Accept-Language': 'en-US,en;q=0.9',}
headers5 = {'authority': 'api.socrative.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','accept': '*/*','sec-gpc': '1','origin': 'https://b.socrative.com','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://b.socrative.com/','accept-language': 'en-US,en;q=0.9',}
headers6 = {'authority': 'api.socrative.com','accept': '*/*','access-control-request-method': 'POST','access-control-request-headers': 'content-type','origin': 'https://b.socrative.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','sec-fetch-dest': 'empty','referer': 'https://b.socrative.com/','accept-language': 'en-US,en;q=0.9',}
headers7 = {'authority': 'api.socrative.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','content-type': 'application/json; charset=UTF-8','accept': '*/*','sec-gpc': '1','origin': 'https://b.socrative.com','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://b.socrative.com/','accept-language': 'en-US,en;q=0.9',}
headers8 = {'authority': 'api.socrative.com','accept': '*/*','access-control-request-method': 'POST','access-control-request-headers': 'content-type','origin': 'https://b.socrative.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','sec-fetch-dest': 'empty','referer': 'https://b.socrative.com/','accept-language': 'en-US,en;q=0.9',}
headers9 = {'authority': 'api.socrative.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','content-type': 'application/json; charset=UTF-8','accept': '*/*','sec-gpc': '1','origin': 'https://b.socrative.com','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://b.socrative.com/','accept-language': 'en-US,en;q=0.9',}

randomAnswers = False
correctAnswers = False

class correctAnswers:
    def __init__(self, questionId, answerId, questionNumber, questionType, answer, answerWritten):
        self.questionId = questionId
        self.answerId = answerId
        self.questionNumber = questionNumber
        self.questionType = questionType
        self.answer = answer
        self.answerWritten = answerWritten

class sessionCookies:
    def __init__(self, order, cookie):
        self.order = order
        self.cookie = cookie

names = ['Alex', 'Smith', 'John', 'Jane']
answerList = []
cookieList = []

def mainTitle():
    print("""%s\
        [====================================================================================]
    
         .oooooo..o                                        oooo    oooo                       
        d8P'    `Y8                                        `888   .8P'                        
        Y88bo.       .ooooo.   .ooooo.  oooo d8b  .oooo.    888  d8'     .ooooo.  oooo    ooo 
         `"Y8888o.  d88' `88b d88' `"Y8 `888""8P `P  )88b   88888[      d88' `88b  `88.  .8'  
             `"Y88b 888   888 888        888      .oP"888   888`88b.    888ooo888   `88..8'   
        oo     .d8P 888   888 888   .o8  888     d8(  888   888  `88b.  888    .o    `888'    
        8""88888P'  `Y8bod8P' `Y8bod8P' d888b    `Y888""8o o888o  o888o `Y8bod8P'     .8'     
                                                                                  .o..P'      
                                     Developed with love by KK <3                 `Y8P'       
        [====================================================================================]
    """ % (fg(218)))
    
def mainChoice():
    choice = input("    ► Choice: ")
    if choice == "1":
        answerKey()
    elif choice == "2":
        completeQuiz()
    elif choice == "3":
        bombQuiz()
    elif choice == "4":
        print("x")
    else:
        print("     ✖ Invalid Entry")

def mainMenu():
    print("""
       ╔════════════════════════════════════════════════╗
       ║ Choose Method:                                 ║
       ╠════════════════════════════════════════════════╣
       ║ 1. Get Answer Key                              ║
       ║ 2. Complete Quiz                               ║
       ║ 3. Bomb Quiz                                   ║
       ║ 4. Exit                                        ║
       ╚════════════════════════════════════════════════╝
       """)
    mainChoice()

def roomLogin(room, i):
    data = '{"role":"student","name":"'+room+'","tz_offset":-480}'
    roomLogin = requests.options('https://api.socrative.com/rooms/api/join/', headers=headers)
    roomLogin = requests.post('https://api.socrative.com/rooms/api/join/', headers=headers2, data=data)

    cookie = roomLogin.cookies

    cookieList.append(sessionCookies(str(i), cookie))
    print(cookieList[0].order[0])

def startBomb(room, name, i):
    roomLogin(room, i)

    


    cookies = cookieList[i]

    # GET Actviity
    response = requests.get('https://api.socrative.com/rooms/api/current-activity/'+room+'', cookies=cookies, headers=headers3)

    # ID of the user
    activityInstanceId = json.loads(response.text)['id']

    # Set Name
    namePayload = '{"activity_instance_id":'+str(activityInstanceId)+',"student_name":"'+name+'"}'
    setName = requests.options('https://api.socrative.com/students/api/set-name/', headers=headers6)
    setName = requests.post('https://api.socrative.com/students/api/set-name/', headers=headers7, cookies=cookies, data=namePayload)

    print(cookies, activityInstanceId)

def answerKey():
    return
def completeQuiz():
    return
def bombQuiz():
    print("""\r
       ╔════════════════════════════════════════════════╗
       ║ Quiz Bomb Method:                              ║
       ╠════════════════════════════════════════════════╣
       ║ 1. Random Answers                              ║
       ║ 2. Correct Answers                             ║
       ║ 3. Back                                        ║
       ║ 4. Exit                                        ║
       ╚════════════════════════════════════════════════╝
    """)

    choice = input("    ► Choice: ")

    if choice == "1":
        randomAnswers = True
    elif choice == "2":
        print("\n     ✓ Correct Answers Set To True")
        correctAnswers = True
    elif choice == "3":
        mainMenu()
    elif choice == "4":
        return
    else:
        print("     ✖ Invalid Entry")

    room = input("\n    ► Room Id: ")
    x = input("\n    ► Users: ")

    for i in range(int(x)):
        name = random.choice(names)+', '+random.choice(names)
        startBomb(room, name, i)


mainTitle()
mainMenu()