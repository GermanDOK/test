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
import pogodasan
import key1
import key2
import key3
import key4
import key5
import key6
import steam
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
import kvest1
import kvest12
import kvest13
import kvest14
import kvest15
import kvest16
import kvest17
import kvest18
import kvest19
import kvest20
import news
import top



 
TOKEN = "a0d1d279443bf040e73826d0a5f5e8c48be937e65489e4ef8237ffcadf6f96bf5c4d7ee47b0e9446385ff"
 
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
  (погода) -  Вы заходите в меню погоды, и выбераете нужный вам город, и бот кидает вам погоду в этом городе,
  (подписчики) - Вы заходите в меню ютуберов и выберая одного, вам показывает сколько у него подписчиков в реальном времени,
  (онлайн игроков steam) - Вы заходите в меню выбора игры, и после ввода нужной, вам кидает онлайн игроков в этой игре,

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
5 - Jazz
6 - Country
7 - Dance
8 - Hip Hop            
выйти или выход - выход в предыдущее меню
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
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment": audios})

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
                                  "audio-2001368620_40368620",
                                  "audio272549451_456239757",
                                  "audio474499146_456281742",
                                  "audio474499203_456311081",
                                  "audio371745455_456487607"]
                        audios = random.choice(audios)
                        vk.method("messages.send",
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment": audios})

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
                                  "audio-2001506990_40506990",
                                  "audio-2001506989_40506989",
                                  "audio-2001506987_40506987",
                                  "audio-2001506986_40506986",
                                  "audio-2001506985_40506985",
                                  "audio-2001506984_40506984",
                                  "audio-2001506983_40506983",
                                  "audio-2001506982_40506982",
                                  "audio-2001506981_40506981",
                                  "audio-2001506980_40506980",
                                  "audio-2001764352_6764352",
                                  "audio-2001764353_6764353",
                                  "audio-2001455432_40455432",
                                  "audio-2001455431_40455431",
                                  "audio-2001455430_40455430",
                                  "audio-2001455429_40455429",
                                  "audio-2001455428_40455428",
                                  "audio-2001455427_40455427"]
                        audios = random.choice(audios)
                        vk.method("messages.send",
                                 {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment": audios})

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
                                  "audio2000256869_456242761"]
                        audios = random.choice(audios)
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment": audios})
                    elif text == "5":
                        audios = ["audio-2001059535_10059535",
                                  "audio-2001059553_10059553",
                                  "audio-2001059552_10059552",
                                  "audio-2001059550_10059550",
                                  "audio-2001059549_10059549",
                                  "audio-2001059547_10059547",
                                  "audio-2001059545_10059545",
                                  "audio-2001059544_10059544",
                                  "audio-2001059543_10059543",
                                  "audio-2001059542_10059542",
                                  "audio-2001059541_10059541",
                                  "audio-2001059540_10059540",
                                  "audio-2001059539_10059539",
                                  "audio-2001059538_10059538",
                                  "audio-2001059537_10059537",
                                  "audio-2001582214_36582214",
                                  "audio-2001582213_36582213",
                                  "audio-2001582212_36582212"]
                        audios = random.choice(audios)
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment": audios})
                    elif text == "6":
                        audios = ["audio-2001773228_10773228",
                                  "audio-2001773226_10773226",
                                  "audio-2001773224_10773224",
                                  "audio-2001773220_10773220",
                                  "audio-2001773218_10773218",
                                  "audio-2001773192_10773192",
                                  "audio-2001773195_10773195",
                                  "audio-2001773196_10773196",
                                  "audio-2001773199_10773199",
                                  "audio-2001773205_10773205",
                                  "audio-2001773208_10773208",
                                  "audio-2001773211_10773211",
                                  "audio-2001104767_40104767",
                                  "audio-2001104766_40104766",
                                  "audio-2001104765_40104765",
                                  "audio-2001104764_40104764",
                                  "audio-2001104763_40104763",
                                  "audio-2001104762_40104762",
                                  "audio-2001104761_40104761"]
                        audios = random.choice(audios)
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment": audios})

                    elif text == "7":
                        audios = ["audio-2001287709_38287709",
                                  "audio-2001287708_38287708",
                                  "audio-2001287707_38287707",
                                  "audio-2001287706_38287706",
                                  "audio-2001287705_38287705",
                                  "audio-2001287704_38287704",
                                  "audio-2001287703_38287703",
                                  "audio-2001287702_38287702",
                                  "audio-2001287701_38287701",
                                  "audio-2001287700_38287700",
                                  "audio-2001287699_38287699",
                                  "audio-2001287698_38287698",
                                  "audio-2001287697_38287697",
                                  "audio-2001287696_38287696",
                                  "audio-2001287695_38287695",
                                  "audio-2001287694_38287694",
                                  "audio-2001287693_38287693",
                                  "audio-2001287692_38287692",
                                  "audio-2001287691_38287691",
                                  "audio-2001287690_38287690",
                                  "audio-2001287689_38287689",
                                  "audio-2001287688_38287688",
                                  "audio-2001287687_38287687",
                                  "audio-2001287686_38287686",
                                  "audio-2001287685_38287685",
                                  "audio-2001287684_38287684"]
                        audios = random.choice(audios)
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment": audios})

                    elif text == "8":
                        audios = ["audio-2001611440_36611440",
                                  "audio-2001456051_33456051",
                                  "audio-2001821456_32821456",
                                  "audio-2001722671_41722671",
                                  "audio-2001722677_41722677",
                                  "audio-2001821458_32821458",
                                  "audio-2001722676_41722676",
                                  "audio-2001611437_36611437",
                                  "audio-2001722675_41722675",
                                  "audio-2001722674_41722674",
                                  "audio-2001722673_41722673",
                                  "audio-2001611439_36611439",
                                  "audio-2001722672_41722672",
                                  "audio-2001722670_41722670",
                                  "audio-2001722669_41722669",
                                  "audio-2001722668_41722668",
                                  "audio-2001722667_41722667",
                                  "audio-2001722666_41722666",
                                  "audio-2001722665_41722665",
                                  "audio-2001722664_41722664",
                                  "audio-2001722663_41722663",
                                  "audio-2001722662_41722662",
                                  "audio-2001722661_41722661",
                                  "audio-2001722660_41722660",
                                  "audio-2001722659_41722659",
                                  "audio-2001722658_41722658",
                                  "audio-2001722657_41722657",
                                  "audio-2001722656_41722656",
                                  "audio-2001722655_41722655",
                                  "audio-2001722654_41722654",
                                  "audio-2001722653_41722653",
                                  "audio-2001722652_41722652",
                                  "audio-2001722651_41722651"]
                        audios = random.choice(audios)
                        vk.method("messages.send", 
                                  {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key5.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Лови", "attachment": audios})

                    elif text.lower() == "выход" or text.lower() == "выйти":
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из подменю"})
                        break #выход из вложенного бесконечного цикла while True

                    else:
                        vk.method("messages.send",
                                {"peer_id":user_id, "random_id":msg_id, "message":bot_infaf})
























        if text.lower() == "анекдот":
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":joke.get_joke()})
 




















        elif text.lower() == "подписчики":
            new_command = """
            Вы вошли в подменю "Подписчики", выберите ютубера, который вас интересует:
            1 - PewDiePie 
            выйти или выход - выход в предыдущее меню
            """
            bot_infaf = """ Чего, извини я не расслышал? """

            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key2.keyboard, ensure_ascii=False).encode("utf-8"), "message":new_command})
 
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
                            {"peer_id":user_id, "random_id":msg_id, "message":sub_msg})
                    if text == "2":
                        sub = subscribes.get_subs_tseries()
                        sub_msg = "{} подписчиков".format(sub)
                        vk.method("messages.send",
                            {"peer_id":user_id, "random_id":msg_id, "message":sub_msg})

                    elif text.lower() == "выйти":
                        vk.method("messages.send",
                            {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":bot_infa})
                        break
                        
                    else:
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":bot_infaf})
             
     
                        

















        elif text.lower() == "инфа":
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":infa.get_infa()})

























        elif text.lower() == "монетка":                                 #vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":coin.get_coin()})
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
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из игры"})
                        break
                    else:
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":bot_infaf})
   
                        





















        elif text.lower() == "курс":
            new_command = """
Вы вошли в подменю "Курса валют", выберите курс который вас интересует:
1 - Доллар
2 - Евро
3 - Фунт стерлингов 
4 - Швейцарский франк
Выйти или Выход - выход в предыдущее меню
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
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из подменю"})
                        break

                    else:
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":bot_infaf})
   
                        















            


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



















        elif text.lower() == "погода":
            new_command = """
            Выберите город или регион:
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
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":pogoda_msg})

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
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из подменю"})
                        break

 
    
                    
















        elif text.lower() == "квест":
 
            new_command = """
Выбери квест
1.Огромный дом
2.Пустыный город <<еще нету :)>>
            """
            bot_infafаf = """ Чего, извини я не расслышал? """

            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key3.keyboard, ensure_ascii=False).encode("utf-8"), "message":new_command})
 



            while True:
                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                if messages["count"] > 0: 
                    last_messages = messages["items"][0]["last_message"] 
                    text = last_messages["text"] 
                    user_id = last_messages["from_id"] 
                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)


                    if text.lower() == "выйти":
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                        break


                    elif text == "1":
                        new_command = """
Ну окей начнем, обьясняю правила, в каждом мною отправленном тексте есть выбор куда пойти или что сделать, читайте вдумчиво, так как от ваших решений зависит построенние истории. 
Ну чтож, если что, ты можешь в любой момент выйти, просто напиши ВЫЙТИ
Если готов пиши 1, если нет и хочешь выйти пиши 2.
                        """
                        bot_1 = """ Читай правила) """
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key3.keyboard, ensure_ascii=False).encode("utf-8"), "message":new_command})
                        

                        while True:
                            messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                            if messages["count"] > 0: 
                                last_messages = messages["items"][0]["last_message"] 
                                text = last_messages["text"] 
                                user_id = last_messages["from_id"] 
                                msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)


                                if text.lower() == "2":
                                    vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                                    break


                                elif text.lower() == "1":
                                    bot_5 = " Читай текст) "
                                    vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key4.keyboard, ensure_ascii=False).encode("utf-8"), "message":kvest1.new_command})

                                    
                                    while True:
                                        messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                        if messages["count"] > 0: 
                                            last_messages = messages["items"][0]["last_message"] 
                                            text = last_messages["text"] 
                                            user_id = last_messages["from_id"] 
                                            msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000) 


                                            if text.lower() == "выйти":
                                                vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из квеста"})
                                                break
                                            

                                            elif text.lower() == "1":
                                                bot_5 = " Читай текст) "
                                                vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key4.keyboard, ensure_ascii=False).encode("utf-8"), "message":kvest12.new_command})

                                                
                                                while True:
                                                    messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                    if messages["count"] > 0: 
                                                        last_messages = messages["items"][0]["last_message"] 
                                                        text = last_messages["text"] 
                                                        user_id = last_messages["from_id"] 
                                                        msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)


                                                        if text.lower() == "выйти":
                                                            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из квеста"})
                                                            break


                                                        elif text.lower() == "1":                                                            
                                                            bot_5 = " Читай текст) "
                                                            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key4.keyboard, ensure_ascii=False).encode("utf-8"), "message":kvest13.new_command})

                                                            
                                                            while True:
                                                                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                                if messages["count"] > 0: 
                                                                    last_messages = messages["items"][0]["last_message"] 
                                                                    text = last_messages["text"] 
                                                                    user_id = last_messages["from_id"] 
                                                                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000) 
                                                                    if text.lower() == "выйти":
                                                                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":"Вы вышли из квеста"})
                                                                        break
                                
                                                                    elif text.lower() == "1":
                                                                        bot_6 = " Читай текст) "                                                                       
                                                                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key4.keyboard, ensure_ascii=False).encode("utf-8"), "message":kvest14.new_command})


                                                                        while True:
                                                                            messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                                            if messages["count"] > 0: 
                                                                                last_messages = messages["items"][0]["last_message"] 
                                                                                text = last_messages["text"] 
                                                                                user_id = last_messages["from_id"] 
                                                                                msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000) 


                                                                                if text.lower() == "выйти":
                                                                                     vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из квеста"})
                                                                                     break
                                                                           
                               
                                                                                elif text.lower() == "1":
                                                                                    bot_5 = " Читай текст)"                                                                                    
                                                                                    vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key4.keyboard, ensure_ascii=False).encode("utf-8"), "message":kvest15.new_command})


                                                                                    while True:
                                                                                        messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                                                        if messages["count"] > 0:                                                                                            
                                                                                            last_messages = messages["items"][0]["last_message"]                                                                                           
                                                                                            text = last_messages["text"] 
                                                                                            user_id = last_messages["from_id"] 
                                                                                            msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000) 


                                                                                            if text.lower() == "выйти":
                                                                                                  vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из квеста"})
                                                                                                  break
                                                                                                                    
                                                                                            elif text.lower() == "1":
                                                                                                bot_7 = " Читай текст) "
                                                                                                vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key4.keyboard, ensure_ascii=False).encode("utf-8"), "message":kvest16.new_command})

                                                                                                
                                                                                                while True:
                                                                                                    messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"})                                                                                                     
                                                                                                    if messages["count"] > 0: 
                                                                                                        last_messages = messages["items"][0]["last_message"]                                                                                                         
                                                                                                        text = last_messages["text"] 
                                                                                                        user_id = last_messages["from_id"]                                                                                                         
                                                                                                        msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)


                                                                                                        if text.lower() == "выйти":
                                                                                                            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из квеста"})
                                                                                                            break
                                                                                                                  
                                                                                                        
                                                                                                        elif text.lower() == "1":
                                                                                                            bot_5 = " Читай текст) "
                                                                                                            vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key4.keyboard, ensure_ascii=False).encode("utf-8"), "message":kvest18.new_command})

                                                                                                            
                                                                                                            while True:
                                                                                                                messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"})                                                                                                     
                                                                                                                if messages["count"] > 0: 
                                                                                                                    last_messages = messages["items"][0]["last_message"]                                                                                                        
                                                                                                                    text = last_messages["text"] 
                                                                                                                    user_id = last_messages["from_id"]                                                                                                         
                                                                                                                    msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)


                                                                                                                    if text.lower() == "выйти":
                                                                                                                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из квеста"})
                                                                                                                        break


                                                                                                                    elif text.lower() == "1":                                                                                                                       
                                                                                                                        bot_5 = " Читай текст) "
                                                                                                                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key4.keyboard, ensure_ascii=False).encode("utf-8"), "message":kvest19.new_command})
     
                                                                                                                        
                                                                                                                        while True:
                                                                                                                            messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"})                                                                                                     
                                                                                                                            if messages["count"] > 0: 
                                                                                                                                last_messages = messages["items"][0]["last_message"]                                                                                                       
                                                                                                                                text = last_messages["text"] 
                                                                                                                                user_id = last_messages["from_id"]                                                                                                         
                                                                                                                                msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)

                                                                                                                                if text.lower() == "выйти":
                                                                                                                                    vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из квеста"})
                                                                                                                                    break


                                                                                                                                elif text.lower() == "1":
                                                                                                                                    bot_5 = " Читай текст) "
                                                                                                                                    vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key4.keyboard, ensure_ascii=False).encode("utf-8"), "message":kvest20.new_command})
                                                                                                                                    break


                                                                                                                                elif text.lower() == "2":
                                                                                                                                    new_command = """
                                                                                                                                    Надо и правда сходить к психологу, за консультацией, а то вдруг я сума сошел, какие то проклятые бабки, ор на улице, просмотр телика, 
                                                                                                                                    Это уже слишком, запишусь к самому лучшему, к Др. Дрексон, но он не брал тручку, и я вспомнил, что получил скидку к какому то психологу 
                                                                                                                                    Мисис Чаклинс. У меня какое то плохое притчуствие, что же я сделаю...
                                                                                                                                    1.Позвоню
                                                                                                                                    2.Не буду звонить вообще, вдруг меня в психушку отправят с такими <<Выдумками>>
                                                                                                                                   """
                                                                                                                                    bot_11 = " Читай текст) "

                                                                                                                                    vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                                                                                                                        
                                                                                                                                    while True:
                                                                                                                                        messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                                                                                    
                                                                                                                                        if messages["count"] > 0: 
                                                                                                                                            last_messages = messages["items"][0]["last_message"] 
                                                                                                        
                                                                                                                                            text = last_messages["text"] 
                                                                                                                                            user_id = last_messages["from_id"] 
                                                                                                        
                                                                                                                                            msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)
                                                                                                                                            if text.lower() == "1":
                                                                                                                                                new_comand = """
                                                                                                                                                пиииииип.... пиииип.... пииииип.... Здравствуйте, вас приветствует компания ПСИХМОЛГ, вы хотели записаться?
                                                                                                                                                Да я бы хотел записаться к Доктору...Чаклинс, да к Чаклинс.
                                                                                                                                                Хорошо мы вас запишем, на какое время вы бы хотели?
                                                                                                                                                Сегодня в 3 можно?
                                                                                                                                                Щас посморим... Да конечно, вас на это время записать?
                                                                                                                                                Дадада...
                                                                                                                                                Хорошо, тогда Мисис Чаклинс будет ждать.
                                                                                                                                                А может имя у меня спросите или фамилию?
                                                                                                                                                Не, у нас все по номеру телефона)
                                                                                                                                                Все хорошо, тогда досвидание.
                                                                                                                                                Досвидание.
                                                                                                                                                Вот и отлично, схожу, может быть пойму что со мной твориться.
                                                                                                                                                Я оделся, поел и отправился к психологу...
                                                                                                                                                Приехав и зайдя уже в здание и увидев ресепшен, я решил...
                                                                                                                                                1.Пойти на ресепшен,(логично, хех)
                                                                                                                                                2.Пойти налево в коридор
                                                                                                                                                3.Пойти направо на лестницу
                                                                                                                                                4. Стоять как столб и никуда не идти.                                                                                                                                           
                                                                                                                                                """
                                                                                                                                                bot_12 = " Читай текст) "

                                                                                                                                                vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})
                                                                                                                                            if text.lower() == "выйти":
                                                                                                                                                vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из квеста"})
                                                                                                                                                break
                                                        
                                                                                                                                           
                                                                                                                    
                                                                                                                                                

                                                                                                                                
                                                                                                                    
                                                                                                                        break
                                                                                                                           

                                                                                                        break


                                                                                            break


                                                                                break


                                                                    break


                                                        break


                                            break


                                

                                if text.lower() == "2":
                                      bot_11 = """ Читай текст) """
                                      vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key2.keyboard, ensure_ascii=False).encode("utf-8"), "message":new_command})


                                      while True:
                                          messages = vk.method("messages.getConversations", {"count":20, "filter":"unanswered"}) 
                                          if messages["count"] > 0: 
                                            last_messages = messages["items"][0]["last_message"] 
                                            text = last_messages["text"] 
                                            user_id = last_messages["from_id"] 
                                            msg_id = random.randint(1, 200000000000000000000000000000000000000000000000000000000)


                                            if text.lower() == "1":
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

                                                         elif text.lower() == "2":
                                                              new_command = """
                                                                        
                                                                        
                                                                        
                                                                        """
                                                              bot_4 = " Читай текст) "

                                                              vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":new_command})                              

                                break            

                    break                            
     
                                















        elif text == "клава":
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message": "HELLO"})



















        elif text.lower() == "онлайн игроков steam":
            new_command = """
            Вы вошли в подменю "онлайн игроков steam", выберите игру, которая вас интересует:
            1 - Dota 2
            2 - PUBG
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
                        dota = steam.get_dota()
                        sub_msg = "{} игроков".format(dota)
                        vk.method("messages.send",
                            {"peer_id":user_id, "random_id":msg_id, "message":sub_msg})
                                          
                    if text == "2":
                        pubg = steam.get_pubg()
                        sub_msg1 = "{} игроков".format(pubg)
                        vk.method("messages.send",
                            {"peer_id":user_id, "random_id":msg_id, "message":sub_msg1})
                        
                    elif text.lower() == "выйти":                        
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":"Вы вышли из подменю"})
                        break

                    else:
                        vk.method("messages.send", {"peer_id":user_id, "random_id":msg_id, "message":bot_infaf})

        
           
                        





        elif text.lower() == "новости":
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "message":news.format_news()})








        elif text.lower() == "игры":
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "message":top.format_n()})

            









        else:
            vk.method("messages.send",
                        {"peer_id":user_id, "random_id":msg_id, "keyboard":json.dumps(key1.keyboard, ensure_ascii=False).encode("utf-8"), "message":bot_infa})





















       
        print(user_id, "написал нам", text, datetime.today())
        












    







