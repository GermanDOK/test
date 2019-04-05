#1 - начало
#2 - конец кода
import vk_api
import random
import joke
import infa
import coin
import coin2
import course
import subscribe
import key1
import key2
import key3
import key4
import key5
import key6
import key7
import key8
import steam
import pogodasan
import pogodamos
import pogodasochi
import pogodaekat
import pogodaomsk
import pogodasamara
import pogodasaratov
import pogodasan
import pogodavoronesh
import pogodaekat
import pogodasochi
import json
from datetime import datetime
import news
import game_news
import tech_news
import blogers_news
import music
 
TOKEN = "a0d1d279443bf040e73826d0a5f5e8c48be937e65489e4ef8237ffcadf6f96bf5c4d7ee47b0e9446385ff"
 
vk = vk_api.VkApi(token=TOKEN)
 
vk._auth_token()

while True:
    messages = vk.method("messages.getConversations", {"count":200, "filter":"unanswered"})
 
    bot_infa = """
Вот мои команды:
(Анекдот) - При вводе данной команды, бот мгновенно бежит на дно рунета и ищет именно для вас самые крутые анектоды :),
(Инфа) - Информация о мне(о боте),  
(Монетка) - Вы начанаете игру с ботом "Орел или решка", где решает чистый рандом,
(Курс) - Бот кидает вам нынешний курс валют,
(Мем) - Бот кидает вам мемчик, над которым даже моя бабушка не орнула бы,
(Видос) - Бот кидает вам видос, который украл с другого паблика,
(Музыка) - Мы заходите в подгруппу с жанрами песен,
(Новости) - Вы заходите в меню квестов, и выбирая любой, вы начинаете игру, 
(Погода) -  Вы заходите в меню погоды, и выбераете нужный вам город, и бот кидает вам погоду в этом городе,
(Подписчики) - Вы заходите в меню ютуберов и выберая одного, вам показывает сколько у него подписчиков в реальном времени,
(онлайн игроков steam) - Вы заходите в меню выбора игры, и после ввода нужной, вам кидает онлайн игроков в этой игре,

При повторении песни, видео, мема, просто напишите еще раз команду, это рандом, и что то может повторяться. 
   """
    bot_infaf = """ Чего, извини я не расслышал? """
 


    if messages["count"] > 0: 
        last_messages = messages["items"][0]["last_message"] 
        text = last_messages["text"] 
        user_id = last_messages["from_id"] 
        msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
 











#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 


        if text.lower() == "музыка":
 
            new_command = """
Вы вошли в подменю музыки, выберите жанр:
1 - Future Bass
2 - Pop
3 - Rap
4 - Bass House 
5 - Jazz
6 - Country
7 - Dance
8 - Hip Hop            
Выйти - выход в предыдущее меню
            """
            bot_infaf = """ Чего? Извини я не расслышал. """

            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":new_command})
 
            while True:
                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                if messages["count"] > 0: 
                    last_messages = messages["items"][0]["last_message"] 
                    text = last_messages["text"] 
                    user_id = last_messages["from_id"] 
                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
 
                    if text == "1":
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment":music.get_audio1()})


                    elif text == "2":
                        vk.method("messages.send",
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment":music.get_audio2()})


                    elif text == "3":
                        vk.method("messages.send",
                                 {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment":music.get_audio3()})


                    elif text == "4":
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment":music.get_audio4()})


                    elif text == "5":
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment":music.get_audio5()})


                    elif text == "6":
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment":music.get_audio6()})


                    elif text == "7":
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment":music.get_audio7()})


                    elif text == "8":
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment":music.get_audio8()})


                    elif text.lower() == "выход" or text.lower() == "выйти":
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из подгруппы," + bot_infa})
                        break #выход из вложенного бесконечного цикла while True

                    else:
                        vk.method("messages.send",
                                {"peer_id":user_id, "random_id":msg_id, "message":bot_infaf})

#2_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

        if text.lower() == "анекдот":
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":joke.get_joke()})
 
#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________  

        elif text.lower() == "подписчики":
            new_command = """
Вы вошли в подменю "Подписчики", выберите ютубера, который вас интересует:
1 - PewDiePie 
Выйти - выход в предыдущее меню
            """
            bot_infaf = """ Чего, извини я не расслышал? """

            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key8.keyboard, ensure_ascii=False).encode("utf-8"), "message":new_command})
 
            while True:
                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                if messages["count"] > 0: 
                    last_messages = messages["items"][0]["last_message"] 
                    text = last_messages["text"] 
                    user_id = last_messages["from_id"] 
                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
 
                    if text == "1":
                        sub = subscribe.get_subs_pewdiepie()
                        sub_msg = "{} подписчиков".format(sub)
                        vk.method("messages.send",
                            {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key8.keyboard, ensure_ascii=False).encode("utf-8"), "message":sub_msg})

                    elif text.lower() == "выйти":
                        vk.method("messages.send",
                            {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из подгруппы," + bot_infa})
                        break
                        
                    else:
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":bot_infaf})
             
#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

        elif text.lower() == "инфа":
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":infa.get_infa()})

#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

        elif text.lower() == "монетка":                                 
            new_command = """
Выберите Орел или Решка:
1.Орел
2.Решка
Выйти - выход из игры
            """
            bot_infaf = """ Чего, извини я не расслышал? """

            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id,"keyboard":json.dumps(key2.keyboard, ensure_ascii=False).encode("utf-8"), "message":new_command})
 
            while True:
                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                if messages["count"] > 0: 
                    last_messages = messages["items"][0]["last_message"] 
                    text = last_messages["text"] 
                    user_id = last_messages["from_id"] 
                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
                    if text.lower() == "1":
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key2.keyboard, ensure_ascii=False).encode("utf-8"), "message":coin.get_coin()})

                    elif text.lower() == "2":
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key2.keyboard, ensure_ascii=False).encode("utf-8"), "message":coin2.get_coin()})

                    elif text.lower() =="выйти":
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из подгруппы," + bot_infa})
                        break
                    else:
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":bot_infaf})   

#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

        elif text.lower() == "курс":
            new_command = """
Вы вошли в подменю "Курса валют", выберите курс который вас интересует:
1 - Доллар
2 - Евро
3 - Фунт стерлингов 
4 - Швейцарский франк
Выйти - выход в предыдущее меню
            """
            bot_infaf = """ Чего, извини я не расслышал? """

            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key6.keyboard, ensure_ascii=False).encode("utf-8"), "message":new_command})
 
            while True:
                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                if messages["count"] > 0: 
                    last_messages = messages["items"][0]["last_message"]
                    text = last_messages["text"] 
                    user_id = last_messages["from_id"] 
                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
 
                    if text == "1":
                        usd = course.get_course("R01235")
                        course_msg = "{} дают за 1 доллар".format(usd)
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key6.keyboard, ensure_ascii=False).encode("utf-8"), "message":course_msg})
                        

                    elif text == "2":
                        eur = course.get_course("R01239")
                        course_msg2 = "{} дают за 1 евро".format(eur)
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key6.keyboard, ensure_ascii=False).encode("utf-8"), "message":course_msg2})
             

                    elif text == "3":
                        gbp = course.get_course("R01035")
                        course_msg3 = "{} дают за 1 фунт стерлингов".format(gbp)
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key6.keyboard, ensure_ascii=False).encode("utf-8"), "message":course_msg3}) 


                    elif text == "4":
                        gbp = course.get_course("R01775")
                        course_msg3 = "{} дают за 1 швейцарский франк".format(gbp)
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key6.keyboard, ensure_ascii=False).encode("utf-8"), "message":course_msg3})
                        

                    elif text.lower() == "выйти":                        
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из подгруппы," + bot_infa})
                        break

                    else:
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":bot_infaf})

#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

        elif text.lower() == "мем":
            memes = ["photo-155590170_456454320",
                     "photo-79145826_456302044",
                     "photo-79145826_456301995",
                     "photo-79145826_456301996",
                     "photo-79145826_456301992",
                     "photo-79145826_456301991",
                     "photo-79145826_456301990",
                     "photo-79145826_456301986",
                     "photo-79145826_456301985",
                     "photo-79145826_456301982",
                     "photo-155464693_456342948",
                     "photo-155464693_456342972",
                     "photo-155464693_456340988",
                     "photo-100477272_456407837",
                     "photo-139740824_456447984",
                     "photo-91050183_456668495",
                     "photo489279689_456243390",
                     "photo-84600270_456286693",
                     "photo-35294456_456799656",
                     "photo-117608250_456681132",
                     "photo-117608250_456681003",
                     "photo-117608250_456681022",
                     "photo-117608250_456681021",
                     "photo-117608250_456681012",
                     "photo-117608250_456681006",
                     "photo-117608250_456681004",
                     "photo-117608250_456680987",
                     "photo-117608250_456680965",
                     "photo-117608250_456680935",
                     "photo-117608250_456680880",
                     "photo-117608250_456680878",
                     "photo-117608250_456680876",
                     "photo-117608250_456680872",
                     "photo-117608250_456680867",
                     "photo-117608250_456680864",
                     "photo-117608250_456680849",
                     "photo-117608250_456680843",
                     "photo-117608250_456680747"]
            meme = random.choice(memes)
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment": meme})

#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

        elif text.lower() == "видос":
            videos = ["video-57876954_456281366",
                     "video-101063295_456239363",
                     "video-167127847_456240392",
                     "video-57876954_456281201",
                     "video-101063295_456239384",
                     "video-57876954_456281299",
                     "video-57876954_456281243",
                     "video-57876954_456281284",
                     "video-57876954_456281013",
                     "video-91895023_456247657",
                     "video-120254617_456242255",
                     "video-66678575_456264819",
                     "video-66678575_456265282",
                     "video-66678575_456265483",
                     "video-66678575_456265692",
                     "video-65596623_456256621",
                     "video-30316056_456298248",             
                     "video-30316056_456298300",
                     "video-30316056_456291877",
                     "video-30316056_456291905",
                     "video-57876954_456281331",
                     "video-57876954_456281194",
                     "video-57876954_456281242",
                     "video-57876954_456281474",
                     "video-57876954_456282681",
                     "video-57876954_456282603",
                     "video-57876954_456282613",
                     "video-146305289_456239250",
                     "video-167127847_456241503",
                     "video-167127847_456241501",
                     "video-167127847_456241500"]
            video = random.choice(videos)
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment": video})

#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

        elif text.lower() == "погода":
            new_command = """
Вы вошли в подменю "Погода", выберите город который вас интересует:
1.Москва
2.Санкт-Петербург
3.Сочи
4.Екатеринбурге
5.Саратов
6.Самара
7.Воронеж
8.Омск
            """
            bot_infafаfа = """ Чего, извини я не расслышал? """

            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":new_command})
 
            while True:
                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                if messages["count"] > 0: 
                    last_messages = messages["items"][0]["last_message"] 
                    text = last_messages["text"] 
                    user_id = last_messages["from_id"] 
                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
                    if text == "1":
                        temp = pogodamos.get_temp()           
                        cond = pogodamos.get_condition()
                        wind = pogodamos.get_wind_speed()
                        fact = pogodamos.get_fact_unit()
                        time = pogodamos.get_time()
                        term = pogodamos.get_term()            
                        pogoda_msg = " {}, {}, {}, Скорость ветра {} {} ".format(time, cond, temp, wind, fact, term)
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":pogoda_msg})

                    elif text == "2":
                        temp = pogodasan.get_temp()           
                        cond = pogodasan.get_condition()
                        wind = pogodasan.get_wind_speed()
                        fact = pogodasan.get_fact_unit()
                        time = pogodasan.get_time()
                        term = pogodasan.get_term()            
                        pogoda_msg = " {}, {}, {}, Скорость ветра {} {} ".format(time, cond, temp, wind, fact, term)
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":pogoda_msg})

                    elif text == "3":
                        temp = pogodasochi.get_temp()           
                        cond = pogodasochi.get_condition()
                        wind = pogodasochi.get_wind_speed()
                        fact = pogodasochi.get_fact_unit()
                        time = pogodasochi.get_time()
                        term = pogodasochi.get_term()            
                        pogoda_msg = " {}, {}, {}, Скорость {} {} ".format(time, cond, temp, wind, fact, term)
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":pogoda_msg})

                    elif text == "4":
                        temp = pogodaekat.get_temp()           
                        cond = pogodaekat.get_condition()
                        fact = pogodaekat.get_fact_unit()
                        time = pogodaekat.get_time()
                        term = pogodaekat.get_term()            
                        pogoda_msg = " {}, {}, {}, Скорость ветра {} {} ".format(time, cond, temp, fact, term)
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":pogoda_msg})

                    elif text == "5":
                        temp = pogodasaratov.get_temp()           
                        cond = pogodasaratov.get_condition()
                        wind = pogodasaratov.get_wind_speed()
                        fact = pogodasaratov.get_fact_unit()
                        time = pogodasaratov.get_time()
                        term = pogodasaratov.get_term()            
                        pogoda_msg = " {}, {}, {}, Скорость ветра {} {} ".format(time, cond, temp, wind, fact, term)
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":pogoda_msg})

                    elif text == "6":
                        temp = pogodasamara.get_temp()           
                        cond = pogodasamara.get_condition()
                        wind = pogodasamara.get_wind_speed()
                        fact = pogodasamara.get_fact_unit()
                        time = pogodasamara.get_time()
                        term = pogodasamara.get_term()            
                        pogoda_msg = " {}, {}, {}, Скорость ветра {} {} ".format(time, cond, temp, wind, fact, term)
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":pogoda_msg})

                    elif text == "7":
                        temp = pogodavoronesh.get_temp()           
                        cond = pogodavoronesh.get_condition()
                        wind = pogodavoronesh.get_wind_speed()
                        fact = pogodavoronesh.get_fact_unit()
                        time = pogodavoronesh.get_time()
                        term = pogodavoronesh.get_term()            
                        pogoda_msg = " {}, {}, {}, Скорость ветра {} {} ".format(time, cond, temp, wind, fact, term)
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":pogoda_msg})

                    elif text == "8":
                        temp = pogodaomsk.get_temp()           
                        cond = pogodaomsk.get_condition()
                        wind = pogodaomsk.get_wind_speed()
                        fact = pogodaomsk.get_fact_unit()
                        time = pogodaomsk.get_time()
                        term = pogodaomsk.get_term()            
                        pogoda_msg = " {}, {}, {}, Скорость ветра {} {} ".format(time, cond, temp, wind, fact, term)
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":pogoda_msg})

                    elif text.lower() == "выйти":                        
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из подгруппы," + bot_infa})
                        break

#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

        elif text == "клава":
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message": "HELLO"})

#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

        elif text.lower() == "онлайн игроков steam":
            new_command = """
Вы вошли в подменю "онлайн игроков steam", выберите игру, которая вас интересует:
1 - Dota 2
2 - PUBG
3 - CSGO
4 - Warframe
Выйти - выход в предыдущее меню
            """
            bot_infaf = """ Чего, извини я не расслышал? """

            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key7.keyboard, ensure_ascii=False).encode("utf-8"), "message":new_command})
 
            while True:
                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                if messages["count"] > 0: 
                    last_messages = messages["items"][0]["last_message"] 
                    text = last_messages["text"] 
                    user_id = last_messages["from_id"] 
                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
 
                    if text == "1":
                        dota2 = steam.get_dota2()
                        sub_msg = "{} игроков".format(dota2)
                        vk.method("messages.send",
                            {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key7.keyboard, ensure_ascii=False).encode("utf-8"), "message":sub_msg})
                                          
                    elif text == "2":
                        pubg = steam.get_pubg()
                        sub_msg1 = "{} игроков".format(pubg)
                        vk.method("messages.send",
                            {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key7.keyboard, ensure_ascii=False).encode("utf-8"), "message":sub_msg1})

                    elif text == "3":
                        csgo = steam.get_csgo()
                        sub_msg2 = "{} игроков".format(csgo)
                        vk.method("messages.send",
                            {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key7.keyboard, ensure_ascii=False).encode("utf-8"), "message":sub_msg2})

                    elif text == "4":
                        warframe = steam.get_warframe()
                        sub_msg3 = "{} игроков".format(warframe)
                        vk.method("messages.send",
                            {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key7.keyboard, ensure_ascii=False).encode("utf-8"), "message":sub_msg3})
                        
                    elif text.lower() == "выйти":                        
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из подгруппы," + bot_infa})
                        break

                    else:
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":bot_infaf})

#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

        elif text.lower() == "новости":
            new_command = """
Вы вошли в подменю "Новости", выберите, что вас интересует:
1 - Политика
2 - Игры
3 - Технологии
4 - Блогеры
Выйти - Выход в предыдущее меню
            """
            bot_infaf = """ Чего, извини я не расслышал? """

            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key7.keyboard, ensure_ascii=False).encode("utf-8"), "message":new_command})
            while True:
                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                if messages["count"] > 0: 
                    last_messages = messages["items"][0]["last_message"] 
                    text = last_messages["text"] 
                    user_id = last_messages["from_id"] 
                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
 
                    if text == "1":
                        vk.method("messages.send",
                                {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key7.keyboard, ensure_ascii=False).encode("utf-8"), "message":news.format_news()})

                    elif text == "2":
                        vk.method("messages.send",
                                {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key7.keyboard, ensure_ascii=False).encode("utf-8"), "message":game_news.format_news()})

                    elif text == "3":
                        vk.method("messages.send",
                                {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key7.keyboard, ensure_ascii=False).encode("utf-8"), "message":tech_news.format_news()})

                    elif text == "4":
                        vk.method("messages.send",
                                {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key7.keyboard, ensure_ascii=False).encode("utf-8"), "message":blogers_news.format_news()})

                    elif text.lower() == "выйти":
                        vk.method("messages.send",
                                {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из подгруппы," + bot_infa})
                        break

                    else:
                        vk.method("messages.send",
                                {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key4.keyboard, ensure_ascii=False).encode("utf-8"), "message":bot_infaf})
#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

        elif text.lower() == "vkcoin":
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message": "Вот, играй :D \n https://vk.com/app6915965"}) 
#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

        else:
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":bot_infa})

#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#1________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________    

        print(user_id, "написал нам", text, datetime.today())

#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#2________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

        












    







