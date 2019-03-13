#1 - начало
#2 - конец кода
import vk_api
import random
import joke
import infa
import coin
import course
import pogoda



 
TOKEN = "fa6e8710c05b13e8ecaca4b7da6af35a3f8cc18309bb8fcf850a69bf7d73310ce899f39c28533c7c40d62"
 
vk = vk_api.VkApi(token=TOKEN)
 
vk._auth_token()

while True:
    messages = vk.method("messages.getConversations", {"count":200, "filter":"unanswered"})
 
    bot_infa = """
   Вот мои команды:
  (анекдот) - При вводе данной команды, бот мгновенно бежит на дно рунета и ищет именно для вас самые крутые анектоды :),
  (инфа) - Информация о мне(о боте),  
  (монетка) - Вы начанаете игру с ботом "Орел или решка", где решает чистый рандом,
  (курс) - Бот кидает вам нынешний курс валют,
  (мем) - Бот кидает вам мемчик, над которым даже моя бабушка не орнула бы,
  (видос) - Бот кидает вам видос, который украл с другого паблика,
  (музыка) - Мы заходите в подгруппу с жанрами песен,
  (привет) - Вы начинаете разговор с ботом(улудшение этой функции в активной разработке)
  (квест) - Вы заходите в меню квестов, и выбирая любой, вы начинаете игру, 
  При повторении песни, видео, мема, просто напишите еще раз команду, это рандом, и что то может повторяться. 
   """
 


    if messages["count"] > 0: 
        last_messages = messages["items"][0]["last_message"] 
        text = last_messages["text"] 
        user_id = last_messages["from_id"] 
        msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
 





        if text.lower() == "музыка":
 
            new_command = """
            Вы вошли в подменю музыки, выберите жанр:
            1 - Future Bass
            2 - Pop
            3 - Rap
            4 - Bass House           
            выйти или выход - выход в предыдущее меню
            """
            bot_infaf = """ Чего, извини я не расслышал? """

            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
 
            while True:
                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                if messages["count"] > 0: 
                    last_messages = messages["items"][0]["last_message"] 
                    text = last_messages["text"] 
                    user_id = last_messages["from_id"] 
                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
 
                    if text == "1":
                        audios = ["audio-41139501_456241404",
                                  "audio-41139501_456241282",
                                  "audio-41139501_456241220",
                                  "audio-41139501_456241189",
                                  "audio-41139501_456241143",
                                  "audio-41139501_456241029",
                                  "audio-41139501_456240941",
                                  "audio-41139501_456240938",
                                  "audio-41139501_456240894",
                                  "audio-41139501_456240892",
                                  "audio-41139501_456240849",
                                  "audio-41139501_456240820",
                                  "audio-41139501_456240819",
                                  "audio-41139501_456240818",
                                  "audio-41139501_456240784",
                                  "audio-41139501_456240509"]
                        audios = random.choice(audios)
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "message":"Лови", "attachment": audios})

                    elif text == "2":
                        audios = ["audio2000254810_456242888",
                                  "audio2000255074_456242780",
                                  "audio2000258170_456242159",
                                  "audio2000256332_456242547",
                                  "audio2000257242_456242378",
                                  "audio2000249440_456242818",
                                  "audio2000226996_456242822",
                                  "audio2000227387_456242897",
                                  "audio2000243059_456242876",
                                  "audio-2001368625_40368625",
                                  "audio-2001368623_40368623",
                                  "audio-2001368620_40368620"]
                        audios = random.choice(audios)
                        vk.method("messages.send",
                                  {"peer_id":user_id, "random_id":msg_id, "message":"Лови", "attachment": audios})

                    elif text == "3":
                        audios = ["audio272549451_456239220",
                                  "audio272549451_456239221",
                                  "audio272549451_456239062",
                                  "audio272549451_456239063",
                                  "audio272549451_456239064",
                                  "audio272549451_456239222",
                                  "audio272549451_456239379",
                                  "audio272549451_456239380",
                                  "audio272549451_456239398",
                                  "audio272549451_456239449",
                                  "audio272549451_456239450",
                                  "audio272549451_456239452",
                                  "audio371745457_456510577",
                                  "audio371745465_456453795",
                                  "audio371745444_456398253",]
                        vk.method("messages.send",
                                 {"peer_id":user_id, "random_id":msg_id, "message":"Лови", "attachment": audios})

                    elif text == "4":
                        audios = ["audio2000254210_456242555",
                                  "audio2000254338_456242692",
                                  "audio2000254025_456242683",
                                  "audio2000254535_456242501",
                                  "audio2000255252_456242406",
                                  "audio2000256612_456242269",
                                  "audio2000255567_456242364",
                                  "audio2000254159_456242634",
                                  "audio2000252804_456242709",
                                  "audio2000250876_456242537",
                                  "audio2000256681_456242944",
                                  "audio2000257901_456242715",
                                  "audio2000259995_456242185",
                                  "audio2000259158_456242307",
                                  "audio2000256869_456242761",]
                        audios = random.choice(audios)
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "message":"Лови", "attachment": audios})

                    elif text.lower() == "выход" or text.lower() == "выйти":
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"вы вышли из подменю"})
                        break #выход из вложенного бесконечного цикла while True
                    else:
                        vk.method("messages.send",
                                {"peer_id":user_id, "random_id":msg_id, "message":bot_infaf})


        if text.lower() == "анекдот":
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "message":joke.get_joke()})


        elif text.lower() == "инфа":
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "message":infa.get_infa()})


        elif text.lower() == "монетка":
            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":coin.get_coin()})


        elif text.lower() == "курс":
            usd = course.get_course("R01235")            
            eur = course.get_course("R01239")
            gbp = course.get_course("R01035")
            course_msg = "{} дают за 1 доллар, {} дают за 1 евро, {} дают за 1 фунт стерлингов".format(usd, eur, gbp)
            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":course_msg})


        elif text.lower() == "мем":
            memes = ["photo-155590170_456454320","photo-79145826_456302044","photo-79145826_456301995","photo-79145826_456301996","photo-79145826_456301992","photo-79145826_456301991","photo-79145826_456301990","photo-79145826_456301986","photo-79145826_456301985","photo-79145826_456301982","photo-155464693_456342948","photo-155464693_456342972","photo-155464693_456340988","photo-100477272_456407837","photo-139740824_456447984","photo-91050183_456668495","photo489279689_456243390","photo-84600270_456286693","photo-35294456_456799656","photo-117608250_456681132","photo-117608250_456681003","photo-117608250_456681022","photo-117608250_456681021","photo-117608250_456681012","photo-117608250_456681006","photo-117608250_456681004","photo-117608250_456680987","photo-117608250_456680965","photo-117608250_456680935","photo-117608250_456680880","photo-117608250_456680878","photo-117608250_456680876","photo-117608250_456680872","photo-117608250_456680867","photo-117608250_456680864","photo-117608250_456680849","photo-117608250_456680843","photo-117608250_456680747"]
            meme = random.choice(memes)
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "message":"Лови", "attachment": meme})

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
                     "video-57876954_456281474"]
            video = random.choice(videos)
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "message":"Лови", "attachment": video})
        elif text.lower() == "погода":
            temp = pogoda.get_temp            
            cond = pogoda.get_condition
            wind = pogoda.get_wind_speed
            fact = pogoda.get_fact_unit
            time = pogoda.get_time
            term = pogoda.get_term            
            pogoda_msg = "Сейчас {}, {}, {}, {} ".format(time, cond, temp, wind )
            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":pogoda_msg})
 
            

        elif text.lower() == "квест":
 
            new_command = """
            Выбери квест
            1.Огромный дом
            2.Пустыный город
            """
            bot_infafаf = """ Чего, извини я не расслышал? """

            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
 



            while True:
                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                if messages["count"] > 0: 
                    last_messages = messages["items"][0]["last_message"] 
                    text = last_messages["text"] 
                    user_id = last_messages["from_id"] 
                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
                    if text.lower() == "Выйти":
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                        break
                    elif text == "1":
                        new_command = """
                        Ну окей начнем, обьясняю правила, в каждом мною отправленном тексте есть выбор куда пойти или что сделать, читайте вдумчиво, так как от ваших решений зависит построенние истории. 
                        Ну чтож, если ты готов напиши ГОТОВ, если нет, то ВЫЙТИ, если хочешь пройти обучение напиши ОБУЧЕНИЕ.
                        """
                        bot_1 = """ Читай правила) """
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})                                                    
                        while True:
                            messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                            if messages["count"] > 0: 
                                last_messages = messages["items"][0]["last_message"] 
                                text = last_messages["text"] 
                                user_id = last_messages["from_id"] 
                                msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
                                if text.lower() == "Выйти":
                                    vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                                    break
                                elif text.lower() == "готов":
                                    new_command = """
                                   Я проснулся как всегда в 7 утра, впринципе обычная погода и все было по обычному, но я испытовал какое-то негодование, что то меня пугало чтоли, и кстати, меня зовут Джон, я обычный фермер, и живу на улице <<Страшного Робберта>>. Почему его так назвали, не знаю, но возможно потому что в этом районе в 1989 году жили прииииизраки, уууу, вам наверное страшно, но мы уже привыкли. Ладно, пойду собераться на работу, куда же я пойду?
                                   1.На кухню
                                   2.В туалет
                                   3.На балкон
                                   4.На улицу
                                    """
                                    bot_2 = """ Читай текст) """

                                    vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                                    
                                    while True:
                                        messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                        if messages["count"] > 0: 
                                            last_messages = messages["items"][0]["last_message"] 
                                            text = last_messages["text"] 
                                            user_id = last_messages["from_id"] 
                                            msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000) 
                                            if text.lower() == "Выйти":
                                                vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                                                break
                                            
                                            elif text.lower() == "1":
                                                new_command = """
                                               Я решил пойти на кухню, и сделав себе бодрящего кофе и пару бутербродов я решил пойти одеться, а то идти в трусах на работу не самая лучшая идея.
                                               Одевшись я решил... 
                                               1.Идти в туалет
                                               2.Не идти, до работы дотерплю                                          
                                                """

                                                bot_3 = """ Читай текст) """

                                                vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                                                
                                                while True:
                                                    messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                    if messages["count"] > 0: 
                                                        last_messages = messages["items"][0]["last_message"] 
                                                        text = last_messages["text"] 
                                                        user_id = last_messages["from_id"] 
                                                        msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
                                                        if text.lower() == "Выйти":
                                                            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                                                            break
                                                        elif text.lower() == "1":
                                                            new_command = """
                                                           Я решил сходить, вдруг не дойду. Вышол я из туалета и посмотрел на часы:<<ЧЕГОООООООО, ВСМЫСЛЕ 12 ЧАСОВ, У МЕНЯ ЖЕ СМЕНА НАЧИНАЕТСЯ В 12. НЕНЕНЕНЕ, МЕНЯ ЖЕ МОГУТ УВОЛИТЬ>>. 
                                                           Я быстро взял сумку и еще быстрее побежал на остановку.
                                                           На остановке я встретил бабушку, у которой выпали из чемодана выпали какие-то странные мистичиские штуки: Черный череп, Разноцветный тотем и какие-то записки.
                                                           Она мне кричит: <<Помоги пожалуйста внучек, благодарна тебе буду>>.
                                                           И в этот момент подъехал автобус.
                                                           Как же я поступлю...
                                                           1.Помогу старушке
                                                           2.Поеду на автобусе
                                                            """

                                                            bot_5 = " Читай текст) "
                                                            
                                                            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                                                            
                                                            while True:
                                                                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                                if messages["count"] > 0: 
                                                                    last_messages = messages["items"][0]["last_message"] 
                                                                    text = last_messages["text"] 
                                                                    user_id = last_messages["from_id"] 
                                                                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000) 
                                                                    if text.lower() == "Выйти":
                                                                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                                                                        break
                                
                                                                    elif text.lower() == "1":
                                                                        new_command = """
                                                                       Ладн, помогу человеку, думаю за первое опаздание меня не уволят:
                                                                       <<Ох, спасибо вам, молодой человек>>, Да какой я молодой, 45 лет мне уже.<<Да ладно, как же пожелому человеку не помочь.
                                                                       Ладно, я пойду на работу... И вдруг она резко перебила и схватила меня за руку <<В один час ты получишь все, но если используешь не по назначение, убьешь себя>>
                                                                       Хех, вот же бабки пошли поехавшие. Она отпустила мою руку и сказала только <<Прощай>>. Странная бабка но вдруг подъехал мой автобус и я поехал на работу.
                                                                       /ПРОШЛО 6 ЧАСОВ/
                                                                       Я уже ехал домой на последнем автобусе, и уже проезжал мой любимый магазинчик, потом проехал местную школу, а потом уже приехал домой.
                                                                       Весь день меня беспокоили слова старухи, <<В один час все получу и потеряю, но если типо это не по назначению буду использовать, убью себя>>.
                                                                       Ну ладно, завтра выясню, как раз завтра выходной, и может быть пойму.
                                                                       Так, теперь я наверное пойду
                                                                       1.В дом
                                                                       2.В магазин
                                                                       3.На парк
                                                                       4.Посижу на лавочке;                                                                                                                                                                                                           
                                                                        """
                                                                        bot_6 = " Читай текст) "
                                                                        
                                                                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                                                                        while True:
                                                                            messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                                            if messages["count"] > 0: 
                                                                                last_messages = messages["items"][0]["last_message"] 
                                                                                text = last_messages["text"] 
                                                                                user_id = last_messages["from_id"] 
                                                                                msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000) 
                                                                                if text.lower() == "Выйти":
                                                                                     vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                                                                                     break
                                
                                                                                elif text.lower() == "1":
                                                                                    new_command ="""
                                                                                   Подойдя к дому я понял что что-то забыл, а, ну да, ключи, возможно я их оставил на работе,
                                                                                   Но вдруг ко мне подошли какие то человек и сказал мне <<Здравствуйте, меня зовут Робберт, Робберт Страшный.
                                                                                   Это не ваши ли ключи>> Он мне протянул мои же ключи, я был немного в шоке.
                                                                                   Я спросил <<Спасибо вам, но у меня есть вопрос, а у вас в доме есть например, призраки там ну или другие духи>>
                                                                                   <<хахахаха>> засмеялся он <<Ну был один, ну он быстро ушел>>.
                                                                                   Странный молодой человек, но я просто с ним попрощался и мы разошлись,
                                                                                   Теперь, когда ключи у меня, я могу зайти в дом,
                                                                                   (кррррррррм)- звук двери, Эххх, наконец я дома, и я решил первым делом...
                                                                                   1.Пойду в гостинную и ключу телек
                                                                                   2.Пойду в комнату спать
                                                                                   3.Пойду на кухню, поем что нибудь
                                                                                   4.Посижу и подумаю о сегоднешнем дне
                                                                                   """
                                                                                    bot_4 = " Читай текст)"
                                                                                    
                                                                                    vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                                                                                    while True:

                                                                                        messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                                                        if messages["count"] > 0:                                                                                            
                                                                                            last_messages = messages["items"][0]["last_message"]
                                                                                            
                                                                                            text = last_messages["text"] 
                                                                                            user_id = last_messages["from_id"] 

                                                                                            msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000) 
                                                                                            if text.lower() == "Выйти":
                                                                                                  vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                                                                                                  break
                                                                                                                    
                                                                                            elif text.lower() == "1":
                                                                                                new_command ="""
                                                                                                Пойду ка телек посмотрю, может что-то интересное услышу, ведь после такого дня ничего не может удивить,
                                                                                                Корреспондент:<<Здравствуйте, это программа вести, сегодня разбился самолет, в котором было 147 человек>>
                                                                                                <<Ужас>>, сказал я,<<Жалко людей, ведь они не в чем не виноваты что умерли из за неисправности самолета,
                                                                                                Корреспондент:<<В нем погибли такие личности как Андриано Муэрто, Дейф Вашингтон и Робберт Страшный,
                                                                                                Вот их фотографии>> /вывод фотографий/ <<Так стоп, как погиб, я же с ним только что общался, такого не может быть, 
                                                                                                ну хотя могло быть, если на углу у нас был аэропорт, и он бы успел на самолет,
                                                                                                Но у нас блин самый блежайший аэропорт через 47 км, поэтому я не знаю, как это возможно.
                                                                                                Может быть было возможно если это был другой Робберт, но фото один в один с тем Роббертом, с которым я общался.
                                                                                                Ооооох, мне пора спать, завтра разберусь.
                                                                                                Я разделся и лег в постель, и уже через несколько минут заснул.
                                                                                                кхххххххм.... фууууу.... кхххххххм... фууууууу...
                                                                                                На утро я встал и пошел...
                                                                                                1.На кухню 
                                                                                                2.В туалет                                                                                       
                                                                                             """
                                                                                                bot_7 = " Читай текст) "

                                                                                                vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                                                                                                
                                                                                                while True:
                                                                                                    messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                                                                    
                                                                                                    if messages["count"] > 0: 
                                                                                                        last_messages = messages["items"][0]["last_message"] 
                                                                                                        
                                                                                                        text = last_messages["text"] 
                                                                                                        user_id = last_messages["from_id"] 
                                                                                                        
                                                                                                        msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
                                                                                                        if text.lower() == "Выйти":
                                                                                                            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                                                                                                            break
                                                                                                                    
                                                                                                        elif text.lower() == "1":
                                                                                                            new_command ="""
                                                                                                           Я пришел на кухню и глянул в окно, на улице стояла какая-то женщина, похожая на мою мертвую мать, 
                                                                                                           Которая умерла в 1999 в автокатострофе, но вдруг женщина повернулась ко мне, и это была она,
                                                                                                           <<Этого не может быть! Ты же мертва>>, я повертел головой, но она не исчезла, она и правда жива,
                                                                                                           А вдруг я сплю, и чтобы это проверить, я себя ушепнул,<<АЙ!>> мне стало больно, и получается я не сплю,
                                                                                                           Что же я сделаю...
                                                                                                           1.Выйду на улицу
                                                                                                           2.Позвоню в полицию, вдруг это маньяк так надо мной издевается
                                                                                                            
                                                                                                           """
                                                                                                            bot_8 = " Читай текст) "

                                                                                                            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                                                                                                            
                                                                                                            while True:
                                                                                                                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                                                                    
                                                                                                                if messages["count"] > 0: 
                                                                                                                    last_messages = messages["items"][0]["last_message"] 
                                                                                                        
                                                                                                                    text = last_messages["text"] 
                                                                                                                    user_id = last_messages["from_id"] 
                                                                                                        
                                                                                                                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
                                                                                                                    if text.lower() == "Выйти":
                                                                                                                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                                                                                                                        break
                                                                                                                    elif text.lower() == "1":
                                                                                                                        new_command = """
                                                                                                                        Выйдя на улицу, я просто был в шоке, ее не было.<<КАК, Я ЖЕ ТОЛЬКО ЧТО ВИДЕЛ, ЧТО СО МНОЙ ТВОРИТЬСЯ!!!>> орал я на всю улицу,
                                                                                                                        пока не прибежали менты, меня успокоили и посоветовали пойти к психологу, но я просто сел на лавочку и задумался...
                                                                                                                        1. Cамоубийство
                                                                                                                        2. Пойти к психологу
                                                                                                                        """
                                                                                                                        bot_9 = " Читай текст) "

                                                                                                                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                                                                                                                        
                                                                                                                        while True:
                                                                                                                            messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                                                                    
                                                                                                                            if messages["count"] > 0: 
                                                                                                                                last_messages = messages["items"][0]["last_message"] 
                                                                                                        
                                                                                                                                text = last_messages["text"] 
                                                                                                                                user_id = last_messages["from_id"] 
                                                                                                        
                                                                                                                                msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
                                                                                                                                if text.lower() == "1":
                                                                                                                                    new_command = """
                                                                                                                                    Я решил завершить свою жизнь, зная, что я проклят той самой бабкой, и ведь я даже не понял ее фразу,
                                                                                                                                    Я пошел домой, взял из сейфа свой P99, и, зная что все, жизнь щас закончиться, я нажал на курок.
                                                                                                                                    (БААААААМ), вибил дверь спецназ, и видя мое мертвое тело, вызвали скорую, надеясь что как то смогут помочь они,
                                                                                                                                    но... было... уже... поздно...........
                                                                                                                                    ЕСЛИ ВАМ ПОНРАВИЛСЯ КВЕСТ ТО ПОДПИШИТЕСЬ НА ГРУППУ , ТАК КАК Я ЕГО БУДУ ДОРОБАТОВАТЬ, И ПОСТОЯННО МЕНЯТЬ СЮЖЕТ, ДО СОВЕРШЕНСТВА, СПАСИБО ВАМ ЗА
                                                                                                                                    ВРЕМЯ, УДЕЛЕННОЕ МОЕМУ КВЕСТУ :), напишите любое слово"""
                                                                                                                                    bot_10 = " Читай текст) "

                                                                                                                                    vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                                                                                                                                    break
                                                                                                                                
                                                                                                                    
                                                                                                                        break
                                                                                                                           

                                                                                                        break

                                                                                            break

                                                                                break


                                                                    break


                                                        break


                                            break


                                

                                if text.lower() == "2":
                                      new_command = """
                                        Я решил пойти в тубзик, ведь сходить туда это святое.
                                        Умылся, сходил отлил, и одев халат я вышел в коридор.
                                        Куда же я пойду...
                                        1.На кухню
                                        2.В гостную
                                        3.В комнату
                                        4.На балкон
                                                """
                                      bot_11 = """ Читай текст) """

                                      vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})

                                      while True:
                                          messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                          if messages["count"] > 0: 

                                            last_messages = messages["items"][0]["last_message"] 
                                            text = last_messages["text"] 
                                            user_id = last_messages["from_id"] 
                                            msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
                                            if text.lower() == "1":
                                                new_command = """
                                               Я решил пойти на кухню, и сделав себе бодрящего кофе и пару бутербродов я решил пойти одеться, а то идти в трусах на работу не самая лучшая идея. Одевшись я решил... 
                                               1.Идти в туалет. 
                                               2.Не идти, до работы дотерплю.
                                               """
                                                bot_6 = " Читай текст) "
                                                vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})

                                                while True:
                                                   messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                   if messages["count"] > 0: 
                                                         last_messages = messages["items"][0]["last_message"] 
                                                         text = last_messages["text"] 
                                                         user_id = last_messages["from_id"] 
                                                         msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)  
                                
                                                         if text.lower() == "1":
                                                             new_command = """
                                                                        
                                                                        
                                                                        
                                                                        """
                                                             bot_4 = " Читай текст) "

                                                             vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})         



                                if text.lower() == "3":
                                     vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})            



                                if text.lower() == "4":
                                     vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})


                                if text.lower() == "Выйти":
                                      vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                                      break
                                            

                                                
                                                       
                                                        

        elif text.lower() == "привет":
 
            new_command = """
            Привет, как дела:
            1 Отлично
            2 Хорошо
            3 Нормально
            4 Плохо

            """
            bot_infafаf = """ Чего, извини я не расслышал? """

            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
 



            while True:                                                   
                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                if messages["count"] > 0: 
                    last_messages = messages["items"][0]["last_message"] 
                    text = last_messages["text"] 
                    user_id = last_messages["from_id"] 
                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)                                                                                                                               
                    if text == "1":
                        new_command = """
                        Круто, тогда сыграй в новую игру КВЕСТ, я старался сделать её интересной
                        """
                        bot_pomogi = """ Чего? Извини не раслышал """

                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                        

                        while True:
                            messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                            if messages["count"] > 0: 
                                last_messages = messages["items"][0]["last_message"] 
                                text = last_messages["text"] 
                                user_id = last_messages["from_id"] 
                                msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)                                
                                                                   
                                if text.lower() == "выход" or text.lower() == "выйти":
                                    vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":bot_infa})
                                    break 

                                else:
                                    vk.method("messages.send",
                                                {"peer_id":user_id, "random_id":msg_id, "message":bot_pomogi})
                                    break
                        break
                        


                    
                    if text == "2":
                        new_command = """
                        Классно, если хочешь быть счастливым напиши ВИДОС или МЕМ и радуйся жизни
                        """
                        bot_pomogi = """Чего? Извини не раслышал"""

                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                        

                        while True:
                            messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                            if messages["count"] > 0: 
                                last_messages = messages["items"][0]["last_message"] 
                                text = last_messages["text"] 
                                user_id = last_messages["from_id"] 
                                msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)                                                                                                                                   
                                  
                                
                        break  
                        


                    if text == "3":
                        new_command = """
                    Понял, ну ты поднимешь себе настроение благодаря мне, напиши МЕМ и все будет чики-пуки
                        """
                        bot_pomogi = """ Понял, ну ты не переживай, все будет хорошо, у меня есть решение, напиши команду МЕМ и радуйся жизни) """

                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                        

                        while True:
                            messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                            if messages["count"] > 0: 
                                last_messages = messages["items"][0]["last_message"] 
                                text = last_messages["text"] 
                                user_id = last_messages["from_id"] 
                                msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)                                
                                                                   
                                                                                                                                                                                                                                                            
                        break
                        
                       
                    if text == "4":
                            new_command = """
                            Эх, жалко, а хоть из за чего?
                            """
                            bot_pomogi = """ Понял, ну ты не переживай, все будет хорошо, у меня есть решение, напиши команду МЕМ и радуйся жизни) """

                            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                        

                            while True:
                                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                if messages["count"] > 0: 
                                    last_messages = messages["items"][0]["last_message"] 
                                    text = last_messages["text"] 
                                    user_id = last_messages["from_id"] 
                                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)                                
                                                                   
                                    if text.lower() == "выход" or text.lower() == "выйти":
                                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":bot_infa})
                                        break 

                                    else:
                                        vk.method("messages.send",
                                                {"peer_id":user_id, "random_id":msg_id, "message":bot_pomogi})
                                        break
                            break





                    elif text.lower() == "выйти":
                        vk.method("messages.send",
                                                {"peer_id":user_id, "random_id":msg_id, "message":"Рад был с тобой поболтать {}".format(bot_infa)})
                        break
                       
        else:
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "message":bot_infa})

       
        print(user_id, "написал нам", text)












    







