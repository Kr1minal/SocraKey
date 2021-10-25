from colored import fg
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

class correctAnswers:
    def __init__(self, questionId, answerId, questionNumber, questionType, answer, answerWritten):
        self.questionId = questionId
        self.answerId = answerId
        self.questionNumber = questionNumber
        self.questionType = questionType
        self.answer = answer
        self.answerWritten = answerWritten

red = fg(1)
lired = fg(9)
orange = fg(208)
liorange = fg(222)
yellow = fg(228)
limegreen = fg(40)
yellowlime = fg(191)
limegreen = fg(40)
green = fg(46)
print(f"{red}00%\n{lired}15%\n{orange}30%\n{liorange}45%\n{yellow}60%\n{yellowlime}75%\n{limegreen}90%\n{green}100%\n")


answerList = []
qNumbs = []
questionLength = ''
hori = "═"
space = " "

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


white = fg(15)
good = fg(10)
bloo = fg(27)
purp = fg(93)
room = input(f"{bloo}\n    ► Room Id: {white}")

# Login to room

data = '{"role":"student","name":"'+room+'","tz_offset":-480}'
roomLogin = requests.options('https://api.socrative.com/rooms/api/join/', headers=headers)
roomLogin = requests.post('https://api.socrative.com/rooms/api/join/', headers=headers2, data=data)

# Cookies :D
cookies = roomLogin.cookies

# GET Actviity
reponse = requests.get('https://api.socrative.com/rooms/api/current-activity/'+room+'', cookies=cookies, headers=headers3)

# ID of the user
try:
    activityInstanceId = json.loads(reponse.text)['id']
except:
    print("LINE 64, FUCK SHIT GOING ON IG")
    
# ID of the quiz
activityId = json.loads(reponse.text)['activity_id']

# GET Quiz Info
params = (('room', ''+room+''),)
response = requests.get('https://teacher.socrative.com/quizzes/'+str(activityId)+'/student', headers=headers4, params=params, cookies=cookies)

# Set Name
student_name = input(f"{bloo}\n    ► Fake Name: {white}")
print("")
setNamePayload = '{"activity_instance_id":'+str(activityInstanceId)+',"student_name":"'+student_name+'"}'
setName = requests.options('https://api.socrative.com/students/api/set-name/', headers=headers6)
setName = requests.post('https://api.socrative.com/students/api/set-name/', headers=headers7, cookies=cookies, data=setNamePayload)

optionsAnswer = requests.options('https://api.socrative.com/students/api/responses/', headers=headers8)

def bruteforceAnswers(response, headers9, cookies, activityInstanceId):
    global questionLength
    answered = 0
    quizData = json.loads(response.text)
    # Length of Quiz // Total Questions
    questionLength = len(quizData['questions'])
    for x in range(questionLength):
        questionType = json.loads(response.text)['questions'][x]['type']

        

        if questionType == "FR":
            questionNumber = json.loads(response.text)['questions'][x]['order']
            questionId = json.loads(response.text)['questions'][x]['question_id']
            data = '{"question_id":'+str(questionId)+',"activity_instance_id":'+str(activityInstanceId)+',"text_answers":[{"answer_text":"123"}],"check_activity":true,"selection_answers":[],"answer_ids":"","answer_text":"."}'
            postAnswer = requests.post('https://api.socrative.com/students/api/responses/', headers=headers9, cookies=cookies, data=data)

            a = json.loads(postAnswer.text)['correct_answer_ids']
            answerId = str(a).strip("[']")

            b = json.loads(postAnswer.text)['correct_answers']
            answerWritten = str(b).strip("[']")

            answer = "N/A"
            questionType = "Free Response"

            answered += 1
            print(f"    ► Answered {answered}/{questionLength}", end="\r")
            answerList.append(correctAnswers(questionId, answerId, questionNumber, questionType, answer, answerWritten))

        else:
            questionNumber = json.loads(response.text)['questions'][x]['order']
            questionId = json.loads(response.text)['questions'][x]['question_id']
            answerId = json.loads(response.text)['questions'][x]['answers'][0]['id']

            data = '{"question_id":'+str(questionId)+',"activity_instance_id":'+str(activityInstanceId)+',"selection_answers":[{"answer_id":'+str(answerId)+'}],"text_answers":[],"answer_ids":"'+str(answerId)+'"}'
            postAnswer = requests.post('https://api.socrative.com/students/api/responses/', headers=headers9, cookies=cookies, data=data)

            a = json.loads(postAnswer.text)['correct_answer_ids']
            answerId = str(a).strip("[]")

            b = json.loads(postAnswer.text)['correct_answers']
            answerWritten = str(b).strip("['<p>\/]")

            answerLength = len(quizData['questions'][x]['answers'])
            for i in range(answerLength):
                currentId = json.loads(response.text)['questions'][x]['answers'][i]['id']
                currentId = str(currentId).strip("[]")

                if answerId == currentId:
                    answer = json.loads(response.text)['questions'][x]['answers'][i]['order']

                    if answer == 1:
                        answer = "A"
                    elif answer == 2:
                        answer = "B"
                    elif answer == 3:
                        answer = "C"
                    elif answer == 4:
                        answer = "D"
                    elif answer == 5:
                        answer = "E"
                    elif answer == 6:
                        answer = "G"
            
            if questionType == "TF":
                questionType = "True or False"

                if answer == "A":
                    answer = "True"
                elif answer == "B":
                    answer = "False"
            
            elif questionType == "MC":
                questionType = "Multiple Choice"
            
            answered += 1
            print(f"{bloo}    ► Answered: {white}{answered}/{questionLength}", end="\r")
            answerList.append(correctAnswers(questionId, answerId, questionNumber, questionType, answer, answerWritten))

bruteforceAnswers(response, headers9, cookies, activityInstanceId)

def newUser(room, answerList):
    global questionLength
    # Login to room
    data = '{"role":"student","name":"'+room+'","tz_offset":-480}'
    roomLogin = requests.options('https://api.socrative.com/rooms/api/join/', headers=headers)
    roomLogin = requests.post('https://api.socrative.com/rooms/api/join/', headers=headers2, data=data)

    # Cookies :D
    cookies = roomLogin.cookies

    # GET Actviity
    response = requests.get('https://api.socrative.com/rooms/api/current-activity/'+room+'', cookies=cookies, headers=headers3)

    # ID of the user
    activityInstanceId = json.loads(response.text)['id']

    name = input(f"{bloo}\n\n    ► Real Name: {white}")
    setNamePayload = '{"activity_instance_id":'+str(activityInstanceId)+',"student_name":"'+name+'"}'
    setName = requests.options('https://api.socrative.com/students/api/set-name/', headers=headers6)
    setName = requests.post('https://api.socrative.com/students/api/set-name/', headers=headers7, cookies=cookies, data=setNamePayload)

    print(f"""{purp}
╔═════╦═════════════════╦════════╦═══════════╦═════════════════════════════════════════════╗
║ {white}Q # {purp}║ {white}Question Type   {purp}║ {white}Chosen {purp}║ {white}Status    {purp}║ {white}Answer                                      {purp}║
╠═════╬═════════════════╬════════╬═══════════╬═════════════════════════════════════════════╣
╚═════╩═════════════════╩════════╩═══════════╩═════════════════════════════════════════════╝""", end="\r")

    answered = 0
    y = 1
    while answered < questionLength:

        for obj in answerList:
            answerWritten = str(obj.answerWritten)
            questionNumber = str(obj.questionNumber)
            questionType = str(obj.questionType)
            answer = str(obj.answer)

            for i in range(questionLength):
                if y == int(questionNumber):
                    y += 1
                    data = '{"question_id":'+str(obj.questionId)+',"activity_instance_id":'+str(activityInstanceId)+',"selection_answers":[{"answer_id":'+str(obj.answerId)+'}],"text_answers":[],"answer_ids":"'+str(obj.answerId)+'"}'
                    postAnswer = requests.post('https://api.socrative.com/students/api/responses/', headers=headers9, cookies=cookies, data=data)

                    # Causes shit to break sometimes D: - KK, plz fix <3
                    """ x = json.loads(postAnswer.text)['is_correct']
                    if x == True:
                        correct = "Correct"
                    elif x == False:
                        correct = "Incorrect" """

                    correct = "Correct"

                    if len(questionNumber) < 3:
                        x = 3 - len(questionNumber)
                        questionNumber = questionNumber + " "*x

                    if len(questionType) < 15:
                        x = 15 - len(questionType)
                        questionType = questionType + " "*x

                    if len(answerWritten) < 55:
                        x = 43 - len(answerWritten)
                        answerWritten = answerWritten + " "*x

                    if len(answer) < 6:
                        x = 6 - len(answer)
                        answer = answer + " "*x

                    if len(correct) < 9:
                        x = 9 - len(correct)
                        correct = correct + " "*x

                    print(f"║ {white}{questionNumber} {purp}║ {white}{questionType} {purp}║ {white}{answer} {purp}║ {good}{correct} {purp}║ {white}{answerWritten} {purp}║") 
                    print(f"{purp}╚═════╩═════════════════╩════════╩═══════════╩═════════════════════════════════════════════╝", end="\r")

                    answered += 1

    headers10 = {
    'authority': 'api.socrative.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'accept': '*/*',
    'sec-gpc': '1',
    'origin': 'https://b.socrative.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://b.socrative.com/',
    'accept-language': 'en-US,en;q=0.9',
}

    response = requests.get(f'https://api.socrative.com/students/api/student-score/{activityInstanceId}/', headers=headers10, cookies=cookies)
    totalQuestions = json.loads(response.text)['total']
    studentScore = json.loads(response.text)['correct']
    result = f"{studentScore}/{totalQuestions}"
    percent = str(round(studentScore / totalQuestions * 100)) + "%"


    # if exceeds, it does not space after the name D: fix fix fix :DDD
    if len(name) < 9:
        studentLine = 9
        y = 8 - len(name)
        z = 1
    elif len(name) > 9:
        studentLine = 2 + len(name)
        y = 1
        z = len(name) - 6

    print(len(result))

    if len(result) <= 5:
        resultLine = 7
        resultSpace = 1
        blankSpace = 6 - len(result)
    elif len(result) > 5:
        resultLine = len(result) + 2
        resultSpace = len(result) - 4

    if len(percent) == 4:
        percentLine = 6
        percentSpace = 4
    elif len(percent) == 3:
        percentLine = 5
        percentSpace = 3
    elif len(percent) == 2:
        percentLine = 4
        percentSpace = 2


    
    yello = fg(226)

    print(f"""\n{purp}
╔{hori*studentLine}╦{hori*resultLine}╦{hori*percentLine}╗
║{space}{yello}Student{space*z}{purp}║{space}{white}Score{space*resultSpace}{purp}║ {white}%{space*percentSpace}{purp}║
╠{hori*studentLine}╬{hori*resultLine}╬{hori*percentLine}╣
║ {white}{name}{space*y}{purp}║{space}{white}{result}{space*blankSpace}{purp}║ {white}{percent}{space}{purp}║
╚{hori*studentLine}╩{hori*resultLine}╩{hori*percentLine}╝
    """)

newUser(room, answerList)