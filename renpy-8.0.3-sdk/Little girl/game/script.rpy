# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Joseph")
define r = Character('Conception')
define ch = Character("Teacher cho", image="temp")
image side temp chotipat = im.Scale("images/temp3 chotipat.png", 160, 165, xoffset=150, yoffset=-50)
define m = Character("Mother")

#image
image r_normal:
    "r_normal1.png"
    pause 0.4
    "r_normal2.png"
    pause 0.4
    repeat

image r_before_black = "r_before_tranform.png"

image r_lookup:
    "r_look_up.png"
    pause 0.4
    "r_look_up2.png"
    pause 0.4
    repeat

image r_explain:
    "r_explain1.png"
    pause 0.4
    "r_explain2.png"
    pause 0.4
    repeat

image r_repressed:
    "r_repressed1.png"
    pause 2
    "r_repressed2.png"
    pause 0.5

image r_fashion_glasses = "r_fashion_sunglasses.png"

image r_fashion = "r_fashion.png"

image r_fireeye:
    "r_fireeyes1.png"
    pause 0.4
    "r_fireeyes2.png"
    pause 0.4
    repeat

image r_shake:
    "r_shake_head1.png"
    pause 0.2
    "r_shake_head2.png"
    pause 0.2
    "r_shake_head3.png"
    pause 0.2
    "r_shake_head4.png"
    pause 0.2
    repeat

image r_fallear:
    "r_fallear1.png"
    pause 0.4
    "r_fallear2.png"
    pause 0.4
    repeat

image r_tranform:
    "r_normal1.png"
    pause 0.3
    "r_before_tranform.png"
    pause 0.2
    "r_normal1.png"
    pause 0.1
    "r_before_tranform.png"
    pause 0.1
    "r_normal1.png"
    pause 0.1
    "r_after_tranform.png"
    pause 0.1
    "r_normal_big1.png"
    pause 0.1

image r_clock:
    "r_clock1.png"
    pause 0.2
    "r_clock2.png"
    pause 0.2
    "r_clock3.png"
    pause 0.2
    "r_clock4.png"
    pause 0.2
    "r_clock5.png"
    pause 0.2
    repeat

image r_spirit_out = "r_oh.png"

image r_fallear:
    "r_fallear1.png"
    pause 0.4
    "r_fallear2.png"
    pause 0.4
    repeat

image r_ambulance:
    "r_ambulance1.png"
    pause 0.4
    "r_ambulance2.png"
    pause 0.4
    "r_ambulance3.png"
    pause 0.4
    repeat

image r_swing:
    "r_swing1.png"
    pause 0.4
    "r_swing2.png"
    pause 0.4
    "r_swing3.png"
    pause 0.4
    repeat

image r_swing_speed:
    "r_swing1.png"
    pause 0.1
    "r_swing2.png"
    pause 0.1
    "r_swing3.png"
    pause 0.1
    repeat

image r_cry_big = "r_cry.png"

image r_theft = "r_theft.png"

image r_scared = "r_scared.png"

image r_cool = "r_cool.png"

image r_health = "r_health.png"

image r_coffin:
    "r_coffin1.png"
    pause 0.4
    "r_coffin2.png"
    pause 0.4
    repeat

image r_after_black = "r_after_tranform.png"

image r_normal_big:
    "r_normal_big1.png"
    pause 0.4
    "r_normal_big2.png"
    pause 0.4
    repeat

image r_rip = "r_rip.png"

image hair_curler = 'bg_hair_curler.png'

image r_smile:
    "r_smile1.png"
    pause 0.4
    "r_smile2.png"
    pause 0.4
    repeat

image r_smile_angry:
    "r_smile_angry1.png"
    pause 0.4
    "r_smile_angry2.png"
    pause 0.4
    repeat

image r_sparkling_eye:
    "r_sparkling_eye1.png"
    pause 0.4
    "r_sparkling_eye2.png"
    pause 0.4
    repeat

image r_shock:
    "r_shock1.png"
    pause 0.4
    "r_shock2.png"
    pause 0.4
    repeat

image r_cry_little:
    "r_cry_little1.png"
    pause 0.3
    "r_cry_little2.png"
    pause 0.3
    "r_cry_little3.png"
    pause 0.3
    "r_cry_little4.png"
    pause 0.3
    "r_cry_little5.png"
    pause 0.3
    "r_cry_little6.png"
    pause 0.3
    repeat

image r_scared_little:
    "r_scared_little1.png"
    pause 0.4
    "r_scared_little2.png"
    pause 0.4
    repeat

image r_huh:
    "r_huh1.png"
    pause 0.4
    "r_huh2.png"
    pause 0.4
    repeat

image r_scaredlittle:
    "r_scared_little1"
    pause 0.4
    "r_scared_little2"
    pause 0.4
    repeat

image r_behind = "r_behind.png"

image r_j = "r_j.png"

image r_dad = "r_dad.png"

image r_aunt = "r_aunt.png"

image r_happy:
    "r_happy1.png"
    pause 0.4
    "r_happy2.png"
    pause 0.4
    repeat

image smile:
    "r_smile"
    zoom 0.8

init:
    $ fades = Fade(0, 0, 5) # Fade to black and back.
    $ dissolves = Dissolve(2)
    $ dissolvess = Dissolve(1)
# The game starts here.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #เพิ่ม credit front ท้ายเกม

label start:
    play music "audio/start label music audio.mp3" loop volume 0.25
    scene bg_dressuproom
    with fade
    #scene bg_dressuproom
    'เช้าวันหนึ่งของสาวน้อยที่ชื่อว่า"Joseph"'
    j "เอ๋ วันนี้จะแต่งตัวยังไงดีนะ"
    show j_normal part1
    with dissolve
    j "ใส่ตัวนี้แล้วกัน น่าจะเข้ากับบรรยากาศวันนี้นะ"#show j_normal part1
    play sound 'audio/ping.mp3' volume 0.5
    j "โอ้ 7 โมงแล้วหรอเนี่ย "
    j "โอเคๆ งั้นถึงเวลาที่ต้องทำผมแล้วสินะคะ"
    hide j_normal part1
    with dissolve
    show j_think v1 part1
    j "ไหน ดูซิ ทำผมทรงอะไรดีนะวันนี้"#show j_think v.1 part1
    hide j_think v1 part1
    with dissolve
    show j_normal part1
    j "ถักเปียดีกว่า"#show j_normal part1
    r "(แม่งเอ้ย จะทำผม***อะไรก็ทำไปเถอะ จะไปโรงเรียนไม่ทันอยู่และ)" #r_lookup (pop-rabbit)
    show r_lookup
    with zoomin
    # with dissolve
    play sound 'audio/magic.mp3' volume 0.5
    'กระต่ายตัวนี้เป็นความคิดในใจส่วนหนึ่งของJoseph'
    hide j_normal part1
    with dissolve
    show j_think v1 part1
    r "นี่ เธอคิดดีแล้วหรอ ถักเปียน่ะมันทั้งยุ่งยาก แบ่งช่อก็ยาก มัดตึงมากก็ไม่ได้เพราะมันจะทำให้เธอผมร่วง" #r_explain #show j_think v.1 part1
    hide r_lookup
    with dissolve
    show r_explain
    r "มัดหย่อนมากก็ไม่ดีเพราะมันหลุดง่ายแถมถ้ามัดไว้นานๆผมก็หยักอีก ไม่เป็นทรงด้วยนะเธอ"
    hide j_think v1 part1
    with dissolve
    show j_shock part1
    r "มันไม่สวย มันไม่สวยย เอาทรงอื่น!  ไม่รู้ว่าถักแล้วจะเบี้ยวรึป่าวด้วย อย่าถักเลย ทำทรงอื่นเหอะ"#show j_shock part1
    r "ถ้าเธอมัดผมดังโงะ คนอื่นเขาจะคิดว่าเธอไม่สระผมนะ แต่ถ้ามัดจุกสองข้างมันก็จะน่ารักเกินไปไม่เข้ากับชุดหรอก" #r_lookup
    hide r_explain
    with dissolve
    show r_lookup
    hide j_shock part1
    with dissolve
    show j_think v2 part1
    j "(ไม่ได้สิ ไม่ได้ ไปเรียนทั้งทีก็อยากจะทำผมน่ารักๆนะ)"#show j_think v.2 part1
    j "..."
    hide j_think v2 part1
    with dissolve
    show j_normal part1
    j "ถ้างั้นแล้ว ฉันควรจะทำทรงอะไรดีล่ะคะ"#show j_normal part1
    menu:
        "มัดรวบ":
            play sound 'audio/girl laugh.mp3' volume 0.5
            hide r_lookup
            with dissolve
            show r_fashion
            r "เธอจะดูไร้ตัวตนมากเลยนะ ถ้าเธอมัดรวบน่ะ คนอื่นเขาจะมองว่าการมัดรวบน่ะมันธรรมดามากเลยน่ะสิ คนส่วนใหญ่ก็มัดรวบกันทั้งนั้น" #r_fashion_glasses #show j_think v.1 part1
            r "มันช่างดูไม่มีสไตล์ที่โดดเด่นเอาซะเลย แล้วถ้าเธอได้เดินไปเจอคนที่เธอแอบชอบล่ะ เธออยากให้เขาเห็นเธอในสภาพนั้นหรอ"
            r "หรือถ้าเธอไปเดินกับเพื่อน เพื่อนๆต้องไม่อยากให้เธอมาเดินด้วยแน่ พวกเขาต่างมีสไตล์กันทั้งนั้น"
            hide j_normal part1
            with dissolve
            show j_think v2 part1
            r "โอ้ย แย่แน่ๆ เปลี่ยนทรงด่วน!"#show j_think v.2 part1
            hide r_fashion
            with dissolve
            show r_fashion_glasses
            play sound 'audio/Aha.mp3' volume 0.5
            r "(อย่างนี้เธอจะเปล่งปลั่งเปล่งประกายได้ยังไง ฉันต้องให้เธอทำทรงผมที่ดีกว่านี้อีก มันยังไม่พอหรอก)"
            menu:
                "หนังยางมัดผมธรรมดา":
                    hide j_think v2 part1
                    with dissolve
                    show j_think v1 part1
                    #show j_think v.1 part1
                    r "มันช่างไม่มีสีสันเอาซะเลย มัดธรรมดาเนี่ยนะ มุมมองแฟชั่นของเธอนี่ใช้ไม่ได้เลย"#r_fashion
                    hide r_fashion_glasses
                    with dissolve
                    show r_fashion
                    r "โธ่ มันไม่วิบๆวับๆเลย ไม่ฟรุ้งฟริ้งเลยอ่ะ"
                    hide j_think v1 part1
                    with dissolve
                    show j_think v2 part1
                    r "อีกอย่างนะ เธอคิดดูสิ หนังยางธรรมดาแบบนี้มันจะทำลายสุขภาพผมเธอ ถ้ามัดไปนานๆผมมันก็จะหักงอ"# show j_think v.2 part1
                    r "ผมของเธอจะเป็นรอย ไม่สวย ไม่งามเลย"#r_explain
                    hide r_fashion
                    with dissolve
                    show r_explain
                    r "ผมมันจะเสียได้นะเธอ"
                    r "และถ้าเธอมัดแน่นๆ เธอก็จะปวดหัว และยิ่งถ้าเธอปวดหัวมากๆเธอก็จะเรียนไม่รู้เรื่อง ถ้าเธอเรียนไม่รู้เรื่องเธอก็จะสอบตก ถ้าเธอสอบตกเธอแย่แน่ๆ"
                    hide j_think v2 part1
                    with dissolve
                    show j_normal part1
                    j "แต่ยังไงก็ตามฉันว่ามัดรวบมันก็โอเคนะคะ"#show j_normal part1
                    hide r_explain
                    with dissolve
                    show r_shake
                    r "ไม่ ฉันไม่โอเค เธอต้องเปลี่ยนทรง"#r_shake_head
                    hide j_normal part1
                    with dissolve
                    show j_think v1 part1
                    j "งั้นจะให้ฉันทำทรงอะไรล่ะคะ"#show j_think v.1 part1
                    hide r_shake
                    with dissolve
                    show r_fireeye
                    r "ฉันให้ลอนผม"#r_fireeyes
                    hide j_think v1 part1
                    with dissolve
                    show j_interest part1
                    j "หือ? ลอนผมหรอคะ"#show j_interested part1
                    r "ใช่"
                    j "แต่ว่า..มันทำนานนะคะ"
                    r "เชื่อฉันเถอะน่า มันสวย มันเริ่ด มันเชิด ต้องจัด"
                    j "อะ อ่า.. โอเคค่ะ ลอนผมก็ลอนผม"
                    hide j_interest part1
                    with dissolve
                    show j_happy part1
                    j "โอเคฉันลอนผมเลยแล้วกัน"#show j_happy part1
                "ที่รัดผมน่ารัก":
                    hide j_think v2 part1
                    with dissolve
                    show j_normal part1
                    r "ฉันรู้นะว่าที่รัดผมนี้มันเข้ากับเธอมาก"#r_explain #show j_normal part1
                    hide r_fashion_glasses
                    with dissolve
                    show r_explain
                    r "แต่เธอก็รู้ดีนี่ว่าที่มัดผมแบบนี้มันไม่เคยพอดีกับการมัดของเธอเลย"
                    hide j_normal part1
                    with dissolve
                    show j_think v1 part1
                    r "ถ้าเธอมัดสองทบมันก็จะไม่แน่นแล้วมันก็จะหลุดโxตรสุดบ่อย สุดท้ายเธอก็ต้องมัดใหม่ทั้งวันอยู่ดี"#show j_think v.1 part1
                    r "หรือถ้าเธอมัดสามทบ มันก็จะแน่นเกินไป"
                    r "สุดท้ายเธอก็จะปวดหัว และยิ่งถ้าเธอปวดหัวมากๆเธอก็จะเรียนไม่รู้เรื่อง ถ้าเธอเรียนไม่รู้เรื่องเธอก็จะสอบตก"
                    r "ถ้าเธอสอบตกเธอแย่แน่ๆ ฉันบอกเลย"
                    hide j_think v1 part1
                    with dissolve
                    show j_normal part1
                    j "แต่ยังไงก็ตามฉันว่ามัดรวบมันก็โอเคนะคะ"#show j_normal part1
                    hide r_explain
                    with dissolve
                    show r_shake
                    r "ไม่ ฉันไม่โอเค เธอต้องเปลี่ยนทรง"#r_shake_head
                    hide j_normal part1
                    with dissolve
                    show j_think v2 part1
                    j "งั้นจะให้ฉันทำทรงอะไรล่ะคะ"#show j_think v.2 part1
                    hide r_shake
                    with dissolve
                    show r_fireeye
                    r "ฉันให้ลอนผม"#r_fireeyes
                    hide j_think v2 part1
                    with dissolve
                    show j_interest part1
                    j "หือ? ลอนผมหรอคะ"#show j_interested part1
                    r "ใช่"
                    j "แต่ว่า..มันทำนานนะคะ"
                    r "เชื่อฉันเถอะน่า มันสวย มันเริ่ด มันเชิด ต้องจัด"
                    j "อะ อ่า.. โอเคค่ะ ลอนผมก็ลอนผม"
                    hide j_interest part1
                    with dissolve
                    show j_happy part1
                    j "โอเคฉันลอนผมเลยแล้วกัน"
                "หนังยางรัดแกง":
                    hide j_think v2 part1
                    with dissolve
                    show j_normal part1
                    r "โอ้มายก้อด เธอต้องบ้าไปแล้วแน่ๆ หนังยางรัดแกงเนี่ยนะ!"#r_fashion #show j_normal part1
                    hide r_fashion_glasses
                    with dissolve
                    show r_fashion
                    r "ขอร้องทีเถอะ ถ้าเป็นอย่างนั้นเธอทำผมทรงอื่นยังดีกว่า หนังยางรัดแกงมันคือปีศาจร้ายชัดๆ"
                    hide j_normal part1
                    with dissolve
                    show j_shock part1
                    r "ปีศาจร้ายที่จะคอยกินผมของเธอ ยิ่งเธอมัดแน่นเท่าไหร่มันก็ยิ่งจะกินผมของเธอไปมากเท่านั้น!"#show j_shock part1
                    r "การแกะผมที่มัดจากหนังยางนี้มันยากยิ่งซะกว่าการสอบ GAT PAT ซะอีก เธอต้องใช้เวลาเป็นชั่วโมงแน่เพื่อที่จะแกะมัน"
                    j "แต่ยังไงก็ตามฉันว่ามัดรวบมันก็โอเคนะคะ"
                    hide r_fashion
                    with dissolve
                    show r_shake
                    r "ไม่ ฉันไม่โอเค เธอต้องเปลี่ยนทรง"#r_shake_head
                    hide j_shock part1
                    with dissolve
                    show j_think v2 part1
                    j "งั้นจะให้ฉันทำทรงอะไรล่ะคะ"#show j_think v.2 part1
                    hide r_shake
                    with dissolve
                    show r_fireeye
                    r "ฉันให้ลอนผม"#r_fireeyes
                    hide j_think v2 part1
                    with dissolve
                    show j_interest part1
                    j "หือ? ลอนผมหรอคะ"#show j_interested part1
                    r "ใช่"
                    j "แต่ว่า..มันทำนานนะคะ"
                    hide r_fireeye
                    with dissolve
                    show r_fashion
                    r "เชื่อฉันเถอะน่า มันสวย มันเริ่ด มันเชิด ต้องจัด" #r_fashion
                    j "อะ อ่า.. โอเคค่ะ ลอนผมก็ลอนผม"
                    hide j_interest part1
                    with dissolve
                    show j_happy part1
                    j "โอเคฉันลอนผมเลยแล้วกัน"
        "หนีบผม":
            play sound 'audio/girl laugh.mp3' volume 0.5
            hide r_lookup
            with dissolve
            show r_fashion_glasses
            r "ผมเธอจะเสีย เพราะเธอใช้ความร้อนกับผมมากเกินไป ถ้าหนีบไม่ดีผมเธออาจจะขาดก็ได้นะ" #r_fashion_glasses
            r "ผมเธอมันตรงและถ้าหนีบผมน่ะ มันทำให้ผมเธอไม่มีวอลุ่ม มันไม่งดงามเลย เธอต้องทำทรงที่ดีกว่านี้"
            hide j_normal part1
            with dissolve
            show j_shock part1
            j "ฉันสับสนไปหมดแล้วล่ะค่ะ"#show j_shock part1
            hide j_shock part1
            with dissolve
            show j_interest part1
            j "โอ้ย ฉันจะทำยังไงดี หรือว่า..ฉันจะลอนผมดีคะ"#show j_interested part1
            hide r_fashion_glasses
            with dissolve
            show r_fashion
            play sound 'audio/Aha.mp3' volume 0.5
            r "เธอมั่นใจแล้วหรอว่าเธอจะลอนผมน่ะ มันทั้งร้อน ทำบ่อยๆผมก็เสีย มันไม่ดีหรอกนะเชื่อฉันสิ" #r_fashion
            hide j_interest part1
            with dissolve
            show j_think v1 part1
            j "แต่ว่ามันจะไม่มีเวลาแล้วนะ"#show j_think v.1 part1
            hide j_think v1 part1
            with dissolve
            show j_normal part1
            j "ฉันว่าทรงนี้แหละ เหมาะกับชุดแล้วก็ลุคที่สุดแล้ว"#show j_normal part1
            hide r_fashion
            with dissolve
            show r_swing_speed
            r "คิดสิ คิดสิ คิดสิ ทำอะไรดี ทำอะไรดี ทำอะไรดี"
            hide r_swing_speed
            with dissolve
            show r_fallear
            r "เอาอย่างนั้นก็ได้ ฉันว่ามันก็ไม่ได้แย่เท่าไหร่"
            hide r_fallear
            with dissolve
            show r_normal
            hide j_normal part1
            with dissolve
            show j_think v1 part1
            j "เอ๊ะ แต่มันก็ใช้ความร้อนเหมือนกันนี่นา แต่ทำไมยอมง่ายจังแฮะ"#show j_think v.1 part1
            hide j_think v1 part1
            with dissolve
            show j_happy part1
            j "ช่างเถอะ สายแล้วๆ โอเคฉันลอนผมเลยแล้วกัน"#show j_happy part1
    stop music fadeout 0.5

label start2:
    play music "audio/start label music audio.mp3" loop volume 0.25
    $ score = 0
    scene bg_bus_stop
    with fade
    #เพิ่มฉาก
    show j_normal part2
    show r_normal
    with zoomin
    pause(0.25)
    # script
    j "จัดผมก็ได้ใช้เวลาไปสักพักแล้ว วันนี้จะเดินทางยังไงดีนะ"#j_normal
    menu:
        'รถเมล์':
            play sound "audio/traffic jam.mp3" volume 0.3
            hide r_normal
            with dissolve
            show r_lookup
            r "ฉันถามจริง? เธอก็รู้ตารางรถเมล์ไม่ใช่หรอ"
            hide j_normal part2 with dissolve
            show j_happy part2
            play sound "audio/girl laugh.mp3"
            j 'รู้ค่ะ'
            hide r_lookup
            with dissolve
            show r_repressed
            play sound "audio/angry rabbit.mp3"
            r 'รถเมล์เคยมาตรงเวลาซะที่ไหนล่ะ นี่อาจจะทำให้เธอมานั่งรอรถเมล์อย่างเสียเวลาเปล่าก็ได้!!!!'
            j 'ฉันว่าฉันคงจะไม่โชคร้ายขนาดที่ว่ารอครึ่งชั่วโมงหรอกมั้งคะ'
            hide r_repressed
            with dissolve
            show r_lookup
            r 'ถ้าเธอจะคิดในแง่ดีแบบนั้น'
            stop sound
            menu:
                'เพื่อนๆจะเกลียดเธอ เพราะกลิ่นเหงื่อ':
                    hide j_happy part2 with dissolve
                    show j_feel bad part2
                    r 'งั้นถ้ามีรถเมล์ ก็คงจะเบียดเป็นปลากระป๋อง'
                    r 'แดดร้อนๆ คนเยอะๆ กลิ่นจะเป็นยังไงกันนะ'
                    hide r_lookup
                    hide j_feel bad part2
                    with dissolve
                    show r_spirit_out
                    show j_start shock
                    r 'ใช่! เหม็น! มันเหม็นนนน เธอตัวจะเหม็นนนนนนนน'
                    r 'เพื่อนๆจะต้องรู้สึกรังเกียจเธอแน่เลย เธอจะโดนรังแก แล้วเธอก็จะตัวคนเดียว'
                    $ score += 1
                'เธอจะตายเพราะขาดออกซิเจน!':
                    hide j_happy part2 with dissolve
                    show j_feel bad part2
                    r 'งั้นถ้ามีรถเมล์ ก็คงจะเบียดเป็นปลากระป๋อง'
                    hide r_lookup
                    with dissolve
                    show r_swing
                    r 'ไม่มีที่นั่งอีก เธอต้องยืนจนขาเมื่อย ปวดขาตั้งแต่หัววัน'
                    r 'แล้วถ้ารถติด เธออาจจะต้องติดอยู่บนรถที่มีกลุ่มประชากรหนาแน่น'
                    r 'คิดดูสิ ติดอยู่กับกลุ่มประชากรเยอะเย้อะ'
                    r 'ออกซิเจนก็จะน้อยลง คาร์บอนไดออกไซด์ก็เยอะ ทั้งจากมนุษย์และควันรถ'
                    hide j_feel bad part2 with dissolve
                    show j_start shock
                    r 'เธออาจจะขาดอากาศหายใจ เป็นลมล้มพับไปก็ได้'
                    hide r_swing
                    with dissolve
                    show r_ambulance
                    play sound "audio/Ambulance  Sound (1).mp3" volume 1
                    r 'จากการที่เธอจะไปโรงเรียน ได้ไปโรงบาลแทนแน่'
                    stop sound
                    $ score += 1
                'เธอจะไม่ผ่านวิชาเรียนเพราะไปโรงเรียนสาย':
                    hide j_happy part2 with dissolve
                    show j_feel bad part2
                    hide r_lookup
                    with dissolve
                    show r_clock
                    play sound "audio/clock ticking.mp3" volume 0.7
                    r 'ถ้าเธอเอาแต่รอรถเมล์ รอไปเรื่อยๆ ทั้งๆที่ไม่รู้ว่าจะมาเมื่อไหร่'
                    r 'มันเสียเวลาโดยเปล่าประโยชน์ และจะทำให้เธอสาย'
                    hide r_clock
                    with dissolve
                    show r_spirit_out
                    stop sound
                    r 'อาจารย์ก็จะหักคะแนนเธอ แล้วถ้าคะแนนเธอไม่ดี เพราะจะติด F หรือไม่ก็ไม่ผ่านวิชานั้นๆ'
                    hide r_spirit_out
                    hide j_feel bad part2
                    with dissolve
                    show r_fallear
                    j 'ถึงแม้จะโดนหักคะแนน แต่ไม่ถึงกับติด F หรือไม่ผ่านหรอกนะคะ'#show j_dont worry part2
                    show j_dont worry part2
                    j 'แล้วฉันไม่เคยไปสายด้วย เพราะงั้นไม่ต้องกลัวค่ะ'
                    j 'ฉันจะขึ้นรถเมล์ อย่าขี้กลัวไปหน่อยเลย'
                    $score += 0
            if score > 0:
                menu:
                    'Toxic Level Up':
                        hide j_dont worry part2 with dissolve
                        hide j_start shock
                        show j_start shock
                        play sound "audio/rabbit transform.mp3" volume 0.5
                        hide r_ambulance
                        hide r_spirit_out
                        with zoominout
                        pause(0.5)
                        show r_tranform
                        with zoominout
                        with hpunch
                        with vpunch
                        pause(0.5)
                        r 'แล้วถ้ากรณีที่จราจรไม่ติดขัด บางครั้งคนขับก็จะขับซิ่ง เหมือนอย่างกับแข่งรถอย่างงั้นแหละ'
                        hide r_tranform
                        with dissolve
                        stop sound fadeout 0.5
                        show r_coffin
                        play sound "audio/funeral dance.mp3" volume 0.25
                        r 'แรงพุ่ง แรงเหวี่ยง แรงเบรก จะทำให้เธอกลิ้งหลุดออกจากหน้าต่างก็ได้นะ ยิ่งตัวเล็กๆอยู่ ไปสวรรค์ได้เลย'
                        r 'แล้วถ้าไม่ใช่ภัยจากอุบัติเหตุ เธออาจจะเจอภัยจากมนุษย์ด้วยกันเองก็ได้นะ'
                        stop sound
                menu:
                    'มีโรคจิตมาลวนลาม':
                        hide j_start shock
                        show j_start shock
                        hide r_coffin
                        with dissolve
                        show r_scared
                        r 'ความไม่คาดคิดของเธอ อาจจะทำให้เธอตกอยู่ในอันตรายเลยก็ได้'
                        hide j_start shock with dissolve
                        show j_shock part2
                        r 'มันมีโอกาสที่เธอจะเจอไอโรคจิตที่จะลวนลามเธอบนรถเมล์ก็ได้ ไม่ก็พวกแอบถ่ายใต้กระโปรง'
                        # show smile but angry rabbit
                        r 'เธอคงจะไม่อยากให้มีแผลใจที่โดนเจ้าพวกโรคจิตมากระทำต่อเธอใช่มั้ย'
                        # damage joseph
                    'โดนขโมยของ':
                        hide r_coffin
                        hide j_start shock
                        with dissolve
                        show r_theft
                        show j_shock part2
                        r 'เธออาจจะโดนโจรมาล้วงกระเป๋าก็ได้นะ'
                        r 'ของในกระเป๋าเธอก็มีของสำคัญมากมาย ไม่ก็ของที่มีมูลค่า'
                        r 'ถ้าเธอขัดขืน เธออาจจะโดนขู่จี้ก็ได้'
                        # spirit out
                        hide r_theft
                        with dissolve
                        show r_rip
                        play sound "audio/funeral dance.mp3" volume 0.25
                        r 'แล้วถ้าเหตุการณ์ร้ายแรง เธออาจจะโดนมีดจ้วง ไม่ก็โดนปาดคอ'
                        # damage joseph
                stop sound
                hide r_scared
                hide r_rip
                with dissolve
                show r_spirit_out
                r 'เธออาจจะโดนลูกหลงจากเหตุการณ์มีคนตีกันบนรถ'
                hide j_shock part2 with dissolve
                show j_dead part2
                r 'ถ้าเธอซวยจริงๆอย่างที่ฉันพูดมา เธออาจจะตายก็ได้เลยนะ'
                r 'ตายน่ะ ตายยยยยยยยยยยยยยยยยยยยย'
                hide r_spirit_out
                with dissolve
                show r_swing
                r 'เสียเวลา อันตราย​ เสียเวลา อันตราย เสียเวลา อันตราย เสียเวลา อันตราย​ เสียเวลา อันตราย เสียเวลา อันตราย เสียเวลา อันตรายยยยย'
                hide j_dead part2 with dissolve
                jump finish2
            else:
                hide j_dont worry part2
                $ renpy.movie_cutscene('images/lose.avi')
                jump start3
        'วินมอไซค์':
            hide j_normal part2
            show j_feel bad part2
            r 'เธอใจกล้าเกินไปหรือเปล่า'
            j 'แต่ว่านี่เป็นทางเลือกที่เร็วที่สุดแล้วนะ'
            show r_normal
            r 'ก็ใช่ แต่ ทางนี้ก็ใช้เงินมากที่สุดเหมือนกัน'
            hide r_normal
            with dissolve
            show r_shake
            r 'แถมยังสามารถโกงราคาได้อีก มันไม่ใช่ราคาที่ตรงตัวเลย'
            r 'กำหนดได้ตามใจพวกเขาอีก บางทีเธออาจจะโดนโกง 10-20 บาทเลยนะ'
            j 'ไม่เป็นไร วันนี้ฉันยอมเสียเงินได้'
            hide r_shake
            with dissolve
            show r_fireeye
            r '(โอ้ไม่ได้การแล้ว ถ้าเป็นแบบนี้เธอจะต้องตกอยู่ในอันตราย​แน่เลย ฉันจะต้องปกป้อง!)'
            menu:
                'Toxic Level up':
                    play sound "audio/rabbit transform.mp3" volume 0.5
                    hide r_fireeye
                    with zoominout
                    pause(0.5)
                    show r_cool
                    with zoominout
                    with hpunch
                    with vpunch
                    hide j_normal part2
                    hide j_feel bad part2 with dissolve
                    show j_start shock
                    r 'อย่างที่เธอบอกในตอนแรก ทางเลือกที่ "เร็วที่สุด" ที่เร็วที่สุดก็เพราะว่าเขาขับเร็วมากๆ'
                    r 'แล้วถ้าเกิดอุบัติเหตุ​ล่ะ บางทีเขาก็ไม่มีหมวกกัน​น็อค​ให้ใส่ป้องกันอีก'
                    r 'เธอก็เห็นข่าวที่เกี่ยวกับอุบัติเหตุ​ทางถนนอยู่บ่อยๆหนิ'
                    r 'ถ้าเธอนั่งวันนี้ เธออาจจะเกิดเหตุการณ์​ไม่คาดฝัน​ก็ได้นะ'
                    j 'คงไม่เกิดขึ้นหรอกมั้งคะ เปอร์เซ็นต์การเกิดอุบัติเหตุไม่ได้มากขนาดนั้นนะ'
                    hide r_cool
                    with dissolve
                    show r_normal_big
                    r 'แล้ว ถ้า เกิด เหตุ ขึ้น มา ล่ะ'
                    hide r_normal_big
                    with dissolve
                    show r_cry_big
                    play sound "audio/baddaugthermakeparentsad.mp3" volume 0.3
                    r 'เธอรู้มั้ยว่าพ่อแม่เธอจะเสียใจขนาดไหน'
                    r 'พวกท่านจะต้องโทษตัวท่านเองแน่ๆ ว่าทำไมถึงได้ปล่อยให้ลูกสุดที่รักเดินทางเอง ทำไมไม่ดูแลลูกให้ดีกว่านี้'
                    r 'เธออยากจะทำให้พวกท่านเสียใจหรอ'
                    hide j_start shock with dissolve
                    show j_shock part2
                    j 'ไม่ ฉันไม่ได้คิดจะให้เป็นแบบนั้น'
                    j 'ตะ แต่ว่า'
                    hide r_cry_big
                    with dissolve
                    show r_cool
                    r 'ไม่! มี! แต่!'
                    hide r_cool
                    with dissolve
                    show r_cry
                    play sound "audio/baddaugthermakeparentsad.mp3" volume 0.3
                    r 'ข้อเสียนี่ยังไม่หมดนะ เพื่อนที่รักเธอ และเพื่อนที่เธอรักอีกล่ะ ไหนจะความใฝ่ฝันของเธอที่ตั้งเป้าไว้ว่าจะทำให้สำเร็จ'
                    r 'แล้วถ้าเธอตัดสินใจเลือกวินมอไซค์ แล้วเกิดอะไรขึ้นมา สิ่งที่ตั้งเป้าจะทำให้สำเร็จ เธออาจจะทำให้สำเร็จไม่ได้อีกเลยนะ'
                    # damage joseph
                    hide j_shock part2 with dissolve
                    jump finish2
    label finish2:
        show j_start shock
        j 'แล้วฉันควรจะทำยังไง'
        hide r_swing
        with dissolve
        hide r_cry
        with dissolve
        show r_normal_big
        r 'เดิน'
        hide j_start shock with dissolve
        show j_shock part2
        j 'คะ'
        r 'เดินไปโรงเรียน'
        j 'แต่ว่านี่จะทำให้ไม่ทันเอานะ'
        hide r_normal_big
        with dissolve
        show r_health
        r 'เชื่อฉันแล้วเธอจะปลอดภัยจากอันตราย แล้วก็ใช้วิธีเดินเร็วๆนะ อย่าวิ่งละ ถ้าหกล้มขึ้นมาจะเป็นเรื่องอีก'
        hide j_shock part2 with dissolve
        show j_cry part2
        j 'ฮือ ทำไมฉันต้องมากลัวเรื่องพวกนี้ด้วย'
        $ renpy.movie_cutscene('images/win.avi')
label start3:
    play music "audio/start label music audio.mp3" loop volume 0.25
    $ score = 0
    scene bg_school
    with fade
    #เพิ่มฉาก
    show r_normal
    #school
    show j_normal part3
    with zoomin
    j 'ฟู่ว มาทันเวลาด้วยล่ะค่ะ'#show j_normal part3
    r 'เก่งมากสาวน้อย เข้าห้องเรียนกันเถอะ'
    #classroom
    scene bg_classroom_bg
    with fade
    show j_normal part3
    with dissolve
    show r_normal
    with dissolve
    ch chotipat 'นักเรียนจ๊ะ คะแนนสอบย่อยครั้งที่แล้วออกแล้วนะจ๊ะ'
    j 'เอ๊ะ!'
    ch 'พอครูเรียกชื่อแล้วก็ออกมารับนะจ๊ะ เด็กชายสมชาย...เด็กหญิงโฟกัส'
    j 'เอาล่ะๆ คะแนนออกแล้ว ลุ้นจังเลยค่ะ'
    hide r_normal
    with dissolve
    show r_swing
    r 'โอ๊ยๆๆๆ เมื่อไหร่จะถึง'
    ch 'เด็กหญิงแม่น้ำไนล์...เด็กหญิงไหมสาน...เด็กหญิงออมเงิน...เด็กชายแจ็คฟรุ๊ต'
    j 'ฉันเคยคิดว่าที่บ้านเขาต้องชอบกินขนุนมากแน่เลยถึงตั้งชื่อว่าแจ๊คฟรุ๊ต'
    ch 'เด็กหญิงโจเซฟ'
    j 'ตาฉันแล้วค่ะ'
    #j_give her score part3
    hide j_normal part3
    with dissolve
    show j_give her score part3
    #j_give her score part3
    play sound "audio/heart beat.mp3" loop volume 1.0
    j 'ฟู่ว ใจเต้นแรงไปหมดเลยค่ะ'
    hide r_swing
    with dissolve
    show r_swing_speed
    r 'รีบๆดูเร็วๆๆๆ'
    j 'โอเค นับ 3...2'
    r 'ฮึ่ยยย'
    hide j_give her score part3
    with dissolve
    show j_see scored first part3
    j '1....!!!'#j_see scored first part3
    hide j_see scored first part3
    with dissolve
    show j_see scored second part3
    stop sound
    stop music fadeout 2.0
    play sound "audio/label 2.mp3" fadein 7.0
    j 'ทำไมมัน...'#j_see scored second part3
    hide j_see scored second part3
    with dissolve
    show j_shocked her score part3
    j 'ออกมาเป็นแบบนี้ล่ะคะ'#j_shocked her score part3
    hide r_swing_speed
    with dissolve
    show r_spirit_out
    r 'โอ้วตายแล้ว งานนี้แย่แน่ๆ'
    j 'มะ ไม่ขนาดนั้นหรอกค่ะ..'
    hide j_shocked her score part3
    with dissolve
    show j_talk wit rabbit part3
    #j_talk with rabbit part3
    r 'ไม่ มันขนาดนั้นแหละ คิดดูสิมันจะเกิดอะไรขึ้นถ้าทุกคนรู้ว่าเธอได้เกรดเท่านี้'
    j 'เกรดมันก็แค่..ไม่ๆ ทุกคนไม่ใจร้ายขนาดนั้นหรอกค่ะ'
    r 'ทุกคนอย่างนั้นหรอ พอทุกคนรู้เกรดของเธอแล้วจะไม่มีอะไรเปลี่ยนแปลงเลยอย่างนั้นหรอ'
    $ score = 0
    menu:
        'อาจารย์':
            hide r_spirit_out
            show r_normal
            with dissolve
            r 'รู้อะไรมั๊ย คนแรกที่รู้คะแนนของเธอคืออาจารย์'
            j 'แน่นอนอยู่แล้วค่ะ เพราะเขาเป็นคนให้คะแนนหนิคะ'
            r 'และเขาก็จะรู้ว่า เด็กสาวคนนี้มันไม่เอาไหน'
            j 'คนเป็นอาจารย์เขาจะคิดแบบนั้นได้ยังไงล่ะคะ'
            hide r_normal
            with dissolve
            show r_lookup
            r 'เธออ่านใจเขาได้หรอ จะบอกอะไรให้นะ คนเป็นอาจารย์น่ะ เขาชอบและใส่ใจกับเด็กที่เรียนเก่งคะแนนดี'
            r 'หลังจากนี้เธอคงได้รับสายตาดูแคลนจากเขาแล้วล่ะ ระวังตอนเช็คชื่อให้ดีนะหรือเขาจะทำเป็นไม่เห็นชื่อเธอกันนะ'
            hide j_talk wit rabbit part3
            with dissolve
            show j_relax part3
            j 'ฉันเชื่อว่าอาจารย์ไม่ใจร้ายขนาดนั้นหรอกค่ะ เขามีบทบาทที่จะทำให้พวกเราเป็นคนที่ดีขึ้น เราต้องให้ใจกับเขาด้วย'
            r 'ตามใจเธอก็แล้วกัน'
            j 'ตั้งใจเรียนกันเถอะค่ะ'
            $ score += 0
        'เพื่อน':
            hide r_spirit_out
            show r_lookup
            with dissolve
            r '"ไม่เห็นจะเรียนเก่งเท่าไหร่เลย" เดินๆอยู่ประโยคนี้คงตามหลอกหลอนเธอไปสักพักเลยนะ'
            j 'นั่นมันใจร้ายเกินไปแล้ว ไม่ๆ ทุกคนต้องเข้าใจแน่นอนค่ะ'
            hide r_lookup
            with dissolve
            show r_spirit_out
            r 'นั่งกินข้าวคนเดียวก็คงจะเหงาแย่เลยนะ'
            r 'วันไหนลืมเอากระเป๋ามา ระวังไม่มีที่นั่งล่ะ'
            r 'ตอนขึ้นไปเรียนก็คงไม่มีที่นั่งดีๆสำหรับเธอแล้ว'
            j 'ไม่มีใครตัดสินคนจากความผิดพลาดเพียงครั้งเดียวหรอกค่ะ...'
            hide r_spirit_out
            with dissolve
            show r_swing
            r 'และงานกลุ่มก็จะไม่มีใครเอาเธอมาอยู่ด้วย!!'
            hide j_talk wit rabbit part3
            with dissolve
            show j_start scared part3
            r 'และไม่มีที่ไหนรับคนคะแนนน้อยเข้าทำงานแน่นอนนนนนน'#j_start scared part3
            hide j_start scared part3
            with dissolve
            show j_scared that it ppb happend part3
            j 'ฮือ นี่มันทำฉันรู้สึกแย่จนปวดท้องไปหมดแล้ว' #j_scared that it ppb happend part3
            r 'สาวน้อยคนนี้จะเป็นที่จดจำในงานเลี้ยงรุ่น'
            $ score += 1
        'ครอบครัว':
            hide r_spirit_out
            show r_j
            with dissolve
            r '"คุณพ่อคะคุณแม่คะ วันนี้คะแนนสอบย่อยออกแล้ว แต่มันไม่ค่อยดีเลยค่ะ"'
            hide r_j
            with dissolve
            show r_dad
            r '"ไม่เป็นไรหรอกลูก ครั้งหน้าเอาใหม่ได้นะ"'
            hide r_dad
            with dissolve
            show r_lookup
            r 'ถ้าพ่อกับแม่ตอบเธอมาแบบนี้ ลองหยิกตัวเองดูนะ เผื่อเธอกำลังฝันอยู่'
            j 'ฉันไม่อยากให้พวกท่านเสียใจเลยค่ะ ฉันไม่อยากบอก แต่ยังไงพวกท่านก็ต้องรู้'
            hide r_lookup
            with dissolve
            show r_smile
            r 'ไม่อยากบอกก็ไม่ต้องบอกสิ ไม่ใช่เรื่องที่ต้องกังวลเลย'
            j 'ทำยังไงดีล่ะคะ'
            r 'ทำลายมันสิ เผามัน ปั้นกลมๆแล้วโยนลงน้ำ'
            hide j_talk wit rabbit part3
            with dissolve
            show j_start scared part3
            j 'ฉันจะ....ไม่ ฉันจะไม่ทำอย่างนั้นค่ะ พวกท่านคือคนที่เข้าใจฉันที่สุด'
            hide r_smile
            with dissolve
            show r_lookup
            r 'แต่ไม่ใช่กับป้าข้างบ้าน'
            j 'คุณป้าข้างบ้านไม่เกี่ยวนะคะ'
            hide r_lookup
            with dissolve
            show r_aunt
            r 'โถ่ๆ มีะไรที่ป้าข้างบ้านไม่รู้บ้าง และเคยได้ยินประโยคนี้มั๊ย "ป้าข้างบ้านรู้ คนทั้งโลกรู้"'
            r 'วันนึงอาจจะมีคุณป้าที่ไหนไม่รู้มาทักทายเธอ แล้วคิดว่าป้ารู้จักเธอได้ยังไงล่ะ'
            j 'คุณป้าเป็นเพื่อนของคุณพ่อคุณแม่'
            r 'มั่วแล้ว ก็เธอคือยัยหนูที่คะแนนแย่ไงงงงง'
            r 'พ่อกับแม่คงเหนื่อยกับยัยหนูนั่นแย่เลยสินะเนี่ย ฮี่ๆๆๆๆ'
            menu :
                'บอกครอบครัว':
                    hide r_aunt
                    show r_smile
                    with dissolve
                    hide j_start scared part3
                    with dissolve
                    show j_relax part3
                    #j_ralax part3
                    j 'ขอแค่คุณพ่อกับคุณแม่เข้าใจฉันก็พอแล้วค่ะ บางทีเราไม่จำเป็นต้องใส่ใจว่าคนอื่นจะมองยังไง'
                    hide r_smile
                    with dissolve
                    show r_aunt
                    r 'ที่ฉันพูดไปเธอได้ฟังรึเปล่า รู้มั๊ยว่าเด็กเกือบ 90 เปอร์เซ็นต์ ของทั้งโลกจะเป็นโรคซึมเศร้าเพราะป้าข้างบ้าน'
                    j 'ฉันจะเป็นอีก 10 เปอร์เซ็นต์ที่เหลือเองค่ะ'
                    r 'เธอท้าทายอำนาจมืดแล้วล่ะ'
                    j 'แต่จริงๆแล้วไม่ใช่ว่าคุณป้าทุกคนจะใจร้ายเสมอไปนะคะ'
                    stop sound
                    $ score += 0
                'ครอบครัวคงไม่เข้าใจ':
                    hide r_aunt
                    show r_spirit_out
                    with dissolve
                    hide j_start scared part3
                    with dissolve
                    show j_scared that it ppb happend part3
                    j 'พวกท่านต้องไม่เข้าใจแน่ค่ะ'#j_scared that it ppb happend part3
                    r 'เราแค่ป้องกันกรณีที่ร้ายแรงที่สุด คือพวกเขาจะห้ามไม่ให้เธอทำงานอดิเรกอีกเลย'
                    r 'ไม่มีนิยายให้เธออ่าน ทุกอย่างถูกกีดกันเพื่อให้เธอมีเวลาโฟกัสกับเรื่องการเรียนให้มากที่สุด'
                    j 'นั่นมันแย่มาก ฉันจะไม่บอกพวกเขาเด็ดขาดเลยค่ะ'
                    $ score += 1
        'คนที่แอบชอบ':
            hide r_spirit_out
            with dissolve
            show r_normal
            j 'เขาเป็นคนดีนะคะ ฉันเคยเห็นเขาช่วยติวให้เพื่อนๆด้วย'
            r 'แสดงว่าเขาต้องเป็นคนที่เก่งมากๆ เธอหมดโอกาสแล้วล่ะ คนเก่งต้องชอบคนที่เก่งเหมือนกันสิ'
            hide j_talk wit rabbit part3
            with dissolve
            show j_start scared part3
            #j_start scared part3
            menu:
                'พลิกวิกฤตให้เป็นโอกาส':
                    hide j_start scared part3
                    with dissolve
                    show j_relax part3
                    #j_ralax part3
                    hide r_normal
                    with dissolve
                    show r_lookup
                    j 'ไม่หรอกค่ะ ไม่แน่ฉันอาจจะขอเข้าร่วมการติวในครั้งหน้าด้วย'
                    r 'เพ้อฝันจริงๆเลยยัยเด็กคนนี้'
                    $ score += 0
                'ตัดใจ':
                    hide r_normal
                    with dissolve
                    show r_behind
                    hide j_start scared part3
                    with dissolve
                    show j_scared that it ppb happend part3
                    #j_scared that it ppb happen part3
                    r 'ดูท่าทีเหงาหงอยนั่นสิ ไม่เป็นไรนะฉันจะอยู่กับเธอเอง'
                    $ score += 1
    #play music "audio/start label music audio.mp3" loop volume 0.25
    if score > 0:
        menu:
            'Toxic Level Up':
                play sound "audio/rabbit transform.mp3" volume 0.5
                play music "audio/label 2.mp3" fadein 7.0
                hide r_lookup
                hide r_swing
                hide r_behind
                hide r_spirit_out
                with zoominout
                pause(0.5)
                show r_tranform
                with zoominout
                with hpunch
                with vpunch
                pause(0.5)
                r 'ฉันฟันธงเลยว่าเธอคงอยากจะลาออกแน่นอน เป็นสาวน้อยที่แย่จังเลยน้าาา'
                hide r_tranform
                show r_smile_angry
                with dissolve
                r 'เงินค่าเทอมตรงนั้นสามารถเอาไปใช้ประโยชน์ได้หลายอย่างแต่เธอดันทำให้มันเสียเปล่าซะได้ ตัดสินใจผิดพลาดจริงๆ'
                hide r_smile_angry
                with dissolve
                show r_scared
                r 'ไม่ใช่เงินที่เธอหามาด้วยตัวเองอีก ได้ยินมั๊ยว่าเงินน่ะ! เป็นของมีค่าที่ถูกเธอผลาญไปอย่างเปล่าประโยชน์!!'
                r 'อนาคตของเธอคงมืดบอด ไร้จุดหมายและมีปลายทางที่เตียงนอนกับหมอนเน่า ฟังดูดีหรอ ไม่เลย เธอจะกลายเป็นตัวไร้ประโยชน์ในบ้าน'
                r 'อยู่ในห้องตลอดไป!!!!'
                stop sound fadeout 2.0
                # show j_dead part3
                jump finish3
    else:
        #show rabbit lose
        # play music "audio/start label music audio.mp3" loop volume 0.25
        stop sound
        $ renpy.movie_cutscene('images/lose.avi')
        jump start4
label finish3:
    hide r_scared
    hide j_scared that it ppb happend part3
    with dissolve
    show r_normal
    show j_cry part3
    play sound "audio/girl crying.mp3"
    j 'ฉันไม่ควรบอกความจริงกับทุกคนในห้องนี้'# #j_cry part3
    r 'ใช่แล้วสาวน้อย ทุกคนจะปฏิบัติกับเธอแบบเดิม'
    j 'ฉันจะบอกกับทุกคนว่าฉันจะเก็บกลับไปดูกับพ่อแม่'
    r 'นั่นดีมาก และพอกลับบ้านก็ผลัดวันไปเรื่อยๆ แน่นอนว่าจะไม่มีใครได้เห็นใบกระดาษใบนั้นอีก happy ending!!'
    j 'ฉันไม่ชอบแบบนี้เลยค่ะ'
    $ renpy.movie_cutscene('images/win.avi')
    # This ends the game

label start4:
    play music "audio/start label music audio.mp3" loop volume 0.25
    scene bg_bedroom with fade
    show r_normal
    show j_relax part4
    with zoominout
    j 'จบภารกิจของวันนี้แล้วสินะคะ'#show j_relax part4
    r 'ได้เวลานอนกันแล้ว มีความฝันที่อยากได้มั๊ยสาวน้อย'
    hide r_normal
    hide j_relax part4
    with dissolve
    show j_talk part4
    show r_happy
    j 'ฉันอยากฝันว่าได้เล่นกับกระต่าย'
    hide r_happy
    with dissolve
    show r_scaredlittle
    j 'บางทีถ้ากระต่ายตัวนั้นกัดฉัน ฉันจะขโมยแครอทเขา'
    hide j_talk part4 with dissolve
    show j_relax part4
    j 'แต่ฉันหวังว่ากระต่ายจะดีกับฉันนะคะ ดังนั้นเราจะมีความสุขอยู่ด้วยกัน'
    hide r_scaredlittle
    with dissolve
    show r_normal
    r 'ฉันก็หวังแบบนั้น'
    show j_look down part4 with dissolve
    j 'โอ๊ะ เกือบลืมเลย ตั้งปลุกกี่โมงดีนะ'#show j_look down part4
    menu:
        '4.00':
            hide r_scaredlittle
            with dissolve
            show r_normal
            r 'เดี๋ยวก่อนนะ แล้วเวลาอีก 120 นาทีสำหรับการนอนอันมีค่าล่ะ'
            j 'บางทีฉันก็อยากเปลี่ยนไลฟ์สไตล์ชีวิตดูบ้าง'
            r 'ไหนบอกฉันหน่อยสิว่าเธอตั้งใจจะทำอะไร'
            menu:
                'ออกกำลังกายตอนเช้า':
                    play sound "audio/Aha.mp3"
                    hide r_normal
                    hide j_look down part4
                    hide j_relax
                    with dissolve
                    show r_huh
                    show j_talk part4
                    j 'เพื่อนฉันบอกว่าการออกกำลังกายนอกจากจะส่งผลดีต่อสุขภาพแล้ว ยังทำให้สมองเราทำงานได้ดีขึ้นอีกด้วยนะคะ'
                    r 'อย่างนั้นหรอ เธอมั่นใจได้ยังไงว่าไม่ใช่แผนทำให้เธอเหนื่อยจนไปหลับในห้องเรียนน่ะ'
                    j 'เพื่อนคนนี้เขาเรียนเก่งมากๆเลยนะคะ'
                    r 'แล้วเธอรู้ได้ยังไงว่าเพื่อนคนนั้นเรียนเก่งเพราะออกกำลังกาย'
                    j 'ฉันเห็นเขาลงรูปในโซเชียลค่ะ'
                    hide r_huh
                    with dissolve
                    show r_shock
                    r 'อะไรนะ!!'
                    hide r_shock
                    with dissolve
                    show r_lookup
                    r 'ให้ตายเถอะสาวน้อย เธอกำลังบอกว่าเธอเชื่อสิ่งที่อยู่ในโซเชียลอย่างนั้นหรอ'
                    r 'เธอไม่เคยเห็นพวกคนที่แต่งชุดออกกำลังกายตามแฟชั่นบ้างหรอ แท้จริงแล้วหุ่นดีๆพวกนั้นก็มาจากยาลดความอ้วนทั้งนั้นแหละ'
                    r 'สาวน้อยอ่อนต่อโลกอย่างเธอตามเรื่องพวกนี้ไม่ทันหรอก อยากเรียนเก่งก็แค่อ่านหนังสือก็พอแล้ว เอาเวลา 120 นาทีที่เหลือไปนอนพักสมองดีกว่า'
                    j 'ออกกำลังกายแบบไม่ให้เหนื่อยมากก็ได้หนิคะ แต่ยังไงก็ตาม ฉันอยากจะลองออกกำลังกายดูสักครั้งค่ะ'
                    r 'งั้นบอกมาสิว่าเธอตั้งใจจะออกกำลังกายยังไง'
                    menu:
                        'วิ่ง':
                            play sound "audio/ara ara.mp3" volume 0.2
                            hide r_lookup
                            hide j_talk
                            with dissolve
                            show j_relax part4
                            show r_shock
                            r 'วิ่งงั้นหรอ!!!! เธอไม่กลัวสะดุดล้มรึไง สะดุดล้ม เข่าถลอก แผลติดเชื้อ บาดทะยัก ตัดขา!!!'
                            j 'ไม่ได้วิ่งเร็วขนาดนั้นนะคะ'
                            hide r_shock
                            with dissolve
                            show r_spirit_out
                            r 'การวิ่งของเธออาจจะไปยั่วโมโหหมาเจ้าถิ่นจนพวกมันพาพวกมาวิ่งไล่กวดเธอ!!!'
                            r 'หรือไม่เธออาจจะเจอเจ้าแมวน่ารักๆ ซึ่งนั่นดึงดูดให้เธอเข้าไปเล่นด้วย แต่เจ้าแมวตัวนี้กลัวเธอและตวัดเล็บใส่!!'
                            r 'ที่น่ากลัวกว่านั้น ถ้าเธอโดนแมวกัดล่ะก็ รู้มั๊ยว่านั่นร้ายแรงกว่าโดนหมากัดอีกนะ เชื้อโรคในปากแมวมันน่ากลัวมาก เธอรู้บ้างรึเปล่า!!!'
                            hide j_relax part4
                            with dissolve
                            show j_look up part4
                            play sound "audio/ehh.mp3"
                            j 'ฉะ ฉันไม่เล่นกับพวกน้องแมวก็ได้ค่ะ'
                            hide r_spirit_out
                            with dissolve
                            show r_sparkling_eye
                            r 'เธออดใจไหวหรอ!! เจ้าสัตว์หน้าขนปุกปุย อุ้งเท้านุ่มนิ่ม เสียงร้องน่าเอ็นดู แต่ในร่างกายไหลเวียนด้วยเลือดนักสู้ไทยพวกนั้นน่ะ มีใครอดใจไม่สัมผัสได้บ้าง!!!'
                            hide j_look up part4
                            with dissolve
                            show j_cry part4
                            j 'ฮืออออ ฉันจะไม่เข้าใกล้สัตว์น่ารักแล้ว'
                            hide r_sparkling_eye
                            with dissolve
                            show r_swing
                            r 'ยังไม่หยุดแค่นี้นะ ถ้าวิ่งๆอยู่ฝนเกิดตกขึ้นมาล่ะ แล้วก็ตกหนักขึ้นเรื่อยๆ ทีนี้แหละเธอจะไม่มีทางเลือก นอกจากรีบวิ่งกลับบ้าน สุดท้ายก็มีโอกาสสะดุดล้มอยู่ดีแถมเปอร์เซ็นต์มากกว่าเดิมอีก!!'
                            r 'ฝนที่อยู่ๆก็ตกจะพาฝุ่นละอองที่ลอยอยู่บนท้องฟ้ามากระทบโดนเธอซึ่งนั่นอันตรายมาก ถ้าเธออาบน้ำไม่ทันเธอมีโอกาสเสี่ยงไม่สบายสูงมากๆๆๆๆๆ'
                            r 'สุดท้ายนี้เธอก็ต้องหยุดเรียนไปเป็นสัปดาห์!!!'
                            hide r_swing
                            with dissolve
                            show r_normal
                            r 'period!'
                            j 'อะไรคือ period ล่ะคะนั่น'
                            r 'ฉันคงบอกเธอได้แค่'
                            jump finish4
                        'เต้น':
                            play sound "audio/ara ara.mp3" volume 0.2
                            hide j_talk part4
                            hide r_lookup
                            with dissolve
                            show j_relax part4
                            show r_normal
                            j 'ฉันมีคลิปนึงที่อยากเต้นตามอยู่'
                            hide r_normal
                            with dissolve
                            show r_spirit_out
                            r 'ข้อมือเธอจะเหวี่ยงไปฟาดอะไรสักอย่างจนกระดูกหักได้นะ'
                            j 'ท่าเต้นไม่ค่อยมีเหวี่ยงแขนขนาดนั้นหรอกค่ะ'
                            r 'หรืออาจจะลื่นล้มหัวฟาดพื้น!!!'
                            hide j_relax part4
                            with dissolve
                            show j_look up part4
                            play sound "audio/ehh.mp3"
                            r 'เสียงล้มของเธอจะทำให้พ่อแม่ตื่นและรีบวิ่งมาดู และพอรู้ว่าเกิดอะไรขึ้น พวกเขาจะแบนการเต้น'
                            hide r_spirit_out
                            with dissolve
                            show r_dad
                            r '"มันเป็นอันตรายต่อลูก ต่อไปนี้เราจะยึดมือถือไม่ให้ลูกดูอะไรพวกนี้อีก และเราจะคอยจับตาดูลูกด้วย"'
                            hide r_dad
                            with dissolve
                            show r_spirit_out
                            r 'สุดท้ายนี้เธอจะเกลียดการเต้น และคิดว่าถ้าย้อนเวลากลับไปได้ ฉันจะไม่ทำแบบนั้น!!!'
                            hide r_spirit_out
                            hide j_look up part4
                            with dissolve
                            show r_normal
                            show j_cry part4
                            r 'ฉะนั้นแล้ว วิธีคงอิสรภาพไว้คือตั้งปลุกแบบเดิมซะ'
                            jump finish4
                        'โยคะ':
                            play sound "audio/ara ara.mp3" volume 0.2
                            hide r_lookup
                            hide j_talk part4
                            with dissolve
                            show r_normal
                            show j_relax part4
                            #show j_relax part4
                            j 'โยคะดูทำง่ายดีนะคะ ใช้พื้นที่ไม่เยอะด้วย'
                            r 'ฟังดูดีนะ ไหนฉันขอคำนวณความเสี่ยงให้เธอหน่อย'
                            hide r_normal
                            hide j_relax part4
                            with dissolve
                            show r_shock
                            show j_look up part4
                            play sound "audio/ehh.mp3"
                            r 'เธอเสี่ยงเป็นอัมพาตจากโยคะผิดท่า'
                            r 'โอ้ว ไหนจะตะคริวตัวร้าย'
                            r 'หรือเธออาจจะทำไม่ถูกวิธี ซึ่งนั่นทำให้การออกกำลังกายตอนเช้ามันสูญเปล่า'
                            hide r_shock
                            with dissolve
                            show r_rip
                            r 'เธออาจจะตายได้เพราะไม่รู้วิธีจัดการตัวเองเมื่อร่างกายเหนื่อยเกินไป'
                            hide j_look up part4
                            with dissolve
                            show j_cry part4
                            r 'สุดท้ายนี้ไม่ว่ายังไงก็ตาม มันจะส่งผลต่อการเรียนของเธอ'
                            hide r_rip
                            with dissolve
                            show r_normal
                            r 'ตั้งปลุกแบบเดิมซะ'
                            jump finish4

                'กินข้าวเช้าที่โรงเรียน':
                    play sound "audio/Aha.mp3"
                    hide r_normal
                    hide j_look down part4
                    hide j_relax part4
                    with dissolve
                    show r_lookup
                    show j_talk part4
                    r 'ฉันรู้สึกว่านี่เป็นเรื่องที่บ้ามาก ข้าวที่บ้านไม่อร่อยหรอ'
                    j 'อร่อยที่สุดอยู่แล้วค่ะ'
                    hide r_lookup
                    with dissolve
                    show r_normal
                    r 'ทั้งอร่อยและไม่ต้องเสียเงิน แล้วเธอจะตื่นเช้าไปทำไมกัน'
                    j 'ฉันยังพอมีเงินเก็บอยู่นะคะ ลองสักครั้งคงไม่เป็นอะไร'
                    hide r_normal
                    with dissolve
                    show r_explain
                    r 'ฉันไม่อยากจะพูดแบบนี้หรอกนะ แต่การใช้เวลาอยู่กับครอบครัวเป็นสิ่งที่เราไม่สามารถย้อนกลับมาเรียกคืนได้หรอกนะ'
                    hide r_explain
                    with dissolve
                    show r_cry_little
                    stop music
                    play sound "audio/cry.mp3" volume 1
                    r 'แม่ของเธอจะตรอมใจเพราะคิดว่าฝีมือทำอาหารของตัวเองแย่มาก จนลูกสาวต้องรีบตื่นเช้าไปกินข้าวที่โรงเรียนแทน'
                    r 'แม่ของเธออาจจะแอบไปร้องไห้ซึ่งนั่นทำให้พ่อทุกข์ใจที่ตนเองไม่สามารถทำอาหารได้อยู่แล้ว'
                    hide r_cry_little
                    with dissolve
                    show r_repressed
                    r 'เกิดความร้าวฉานในครอบครัวเพราะเธอ! ไม่! ยอม! กิน! อาหาร! ฝี! มือ! แม่!!!!!'
                    # น้อนร้องห้ายยยยยยยย
                    hide j look up part4
                    show j_cry part4 with dissolve
                    stop sound fadeout 1
                    play music "audio/start label music audio.mp3" loop volume 0.25
                    j 'ฉันรักคุณแม่ รักคุณพ่อด้วย'#show j_cry part4
                    hide r_repressed
                    with dissolve
                    show r_happy
                    r 'ไว้บอกพวกเขาอีกทีบนโต๊ะอาหาร'
                    hide r_happy
                    jump finish4

                'แค่อยากตื่นเช้า':
                    play sound "audio/Aha.mp3"
                    hide r_normal
                    hide j_look down part4
                    hide j_relax
                    with dissolve
                    show r_lookup
                    show j_talk part4
                    r 'นั่นมันบ้ามาก เธอจะตื่นมารอสังเคราะห์แสงแรกของวันหรอ เสียเวลาชีวิตเกินไปแล้ว'
                    j 'บางทีฉันอาจจะลองทำข้าวเช้า'
                    hide r_lookup
                    with dissolve
                    show r_normal
                    r 'เมนูอะไร ทอด ต้ม นึ่งหรือย่างล่ะ'
                    menu:
                        'ขนมปังปิ้งกับไข่ดาว':
                            play sound "audio/ara ara.mp3" volume 0.2
                            hide j_look up part4 with dissolve
                            show j_relax part4
                            j 'แค่ขนมปังปิ้งกับไข่ดาวธรรมดาก็พอแล้วค่ะ'
                            hide r_normal
                            with dissolve
                            show r_repressed
                            r 'นี่มีปิ้งด้วยหรอ โอ้วให้ตายเถอะ ไข่ดาวนั่นเธอรู้รึเปล่าว่ามีอัตราการบาดเจ็บจากการทำอาหารเป็นจำนวนเท่าไหร่ โดยเฉพาะเมนูที่ใช้น้ำมัน!!!'
                            hide r_repressed
                            hide j_relax part4
                            hide j_talk part4
                            with dissolve
                            show r_spirit_out
                            show j_silent part4
                            r 'น้ำมันที่กระเด็นด้วยความร้อนสูงแบบนั้นสามารถละลายผิวหนังเธอจนเป็นแผลเป็นได้เลยนะ'
                            hide j_slient part4 with dissolve
                            show j_cry part4
                            r 'ระหว่างนั้นมันจะเจ็บปวดแค่ไหน หรือบางทีอาจจะไม่ใช่น้ำมันที่กระเด็นมาโดนแต่มีอะไรบางอย่างไปเกี่ยวกระทะจนน้ำมันหกราดใส่ตัวเธอ น้ำมันร้อนๆ!! กับค่ารักษาที่ตามมา!!!'
                            hide r_spirit_out
                            with dissolve
                            show r_shake
                            r 'เอาเป็นว่าเราจะไม่พูดถึงเรื่องนี้อีก แบบนี้ปลอดภัยกับเธอแล้ว'
                            hide r_shake
                            jump finish4
                        'ไข่ต้มยามเช้า':
                            play sound "audio/ara ara.mp3" volume 0.2
                            hide j_relax part4
                            hide j_talk part4
                            with dissolve
                            show j_relax part4
                            #show j_relax part4
                            j 'ไข่ต้มก็ดีนะคะ ดีต่อสุขภาพด้วย'
                            hide r_normal with dissolve
                            show r_lookup
                            r 'เธอกะเวลาต้มได้อย่างนั้นหรอ ถ้าโชคร้ายมากจับได้ไข่ที่ไม่ปกติขึ้นมา และโชคร้ายอีกที่เธอต้มมันนานเกินไปจนมันระเบิดออกมา!!'
                            r 'ให้ตายสิ ฉันจินตนาการกลิ่นออกเลย นี่มันสมรภูมิชัดๆ'
                            hide j_look up part4
                            hide j_relax part4
                            with dissolve
                            show j_silent part4
                            j 'ไข่เน่ามาได้ยังไงคะนั่น'#show j_silent part4
                            r 'ใครจะรู้ หรือเธอสามารถมองทะลุผ่านเปลือกไข่ได้อย่างนั้นหรอ'
                            hide r_lookup
                            with dissolve
                            show r_smile_angry
                            r 'เอ๊ะๆๆๆๆ หรือว่า'
                            r 'เธออาจจะต้มมันออกมาได้ดีมาก แต่มารู้ตัวอีกทีตอนเธอปลอกมันแล้วมันระเบิดใส่หน้าเธอ!!!'
                            hide j_silent part4
                            hide j_relax part4
                            with dissolve
                            show j_cry part4
                            r 'โอ้วว ยกเลิกแผนนี้เถอะ มันเสี่ยงเกินไป เธอแค่ตั้งเวลาตามปกติแล้วนอนอย่างสบายใจก็พอแล้ว'#show j_cry part4
                            j 'ฮื่ออออ'
                            hide r_smile_angry
                            jump finish4
                        'มาม่า':
                            play sound "audio/ara ara.mp3" volume 0.2
                            hide j_look up part4
                            hide j_talk part4
                            with dissolve
                            show j_relax part4
                            #show j_relax part4
                            j 'ฉันไม่ได้ใช้โควตาทานมาม่ามานานแล้ว บางทีทำมาม่าทรงเครื่องตอนเช้าก็ดีนะคะ'
                            hide r_normal
                            with dissolve
                            show r_explain
                            r 'เอาล่ะ ฉันคงพูดได้แค่ว่า ผู้คนมากมายป่วยเป็นโรคไตเพราะการทานมาม่า'
                            hide j_relax part4 with dissolve
                            show j_look up part4
                            play sound "audio/ehh.mp3"
                            j 'นั่นเพราะพวกเขาทานแบบแห้งไม่ใช่หรอคะ ฉันตั้งใจจะต้มนะ'#show j_look up part4
                            r 'ใครบอกเธอแบบนั้นน่ะ'
                            j 'ผู้คนแชร์เรื่องนี้กันในโซเชียล'
                            hide r_explain
                            hide j_look up part4
                            with dissolve
                            show r_repressed
                            show j_silent part4
                            r 'เธอ! หยุด! เชื่อ! ทุก! อย่าง! ใน! โซเชียลเดี๋ยวนี้!!!!!'
                            hide r_repressed
                            with dissolve
                            show r_swing
                            r 'ผู้คนเป็นโรคไตเพราะโซเดียมในมาม่า เธอบอกว่าเธอเอาไปต้มแล้วคิดว่าโซเดียมจะหายไปอย่างนั้นหรอ'
                            r 'ยังไงเธอก็ต้องใส่เครื่องปรุงและซดน้ำทุกหยดอยู่ดีนั่นแหละ'
                            r 'และโรคไตน่ะ มันทรมาณแค่ไหนรู้มั๊ย เธอจะอ่อนเพลียไม่มีแรง ปวดหลังปวดเอวปวดหัวไปหมด!!!'
                            r 'และเธอจะต้องขาดเรียนไปรักษาตัวด้วย'
                            j 'แต่ฉันไม่ได้กินมันบ่อยๆนะคะ'
                            hide r_swing
                            with dissolve
                            show r_shake
                            r 'เธออาจจะติดใจจนเป็นอันกินอะไรไม่ได้ถ้าไม่ใช่เมนูนี้ โอ้ พระเจ้า ฉันไม่อยากคิดถึงตอนที่เธอตัวบวมเพราะแค่มาม่ามื้อเช้านั่น'
                            r 'เอาล่ะสาวน้อยคิดถึงพ่อกับแม่ไว้สิ ตื่นเวลาเดิมและรอทานมื้อเช้าแสนอร่อยทรงคุณค่าของแม่ก็พอแล้ว ไม่เสียเวลานอน ไม่เสียสุขภาพ'
                            hide j_silent part4 with dissolve
                            show j_cry part4
                            j 'โถ่ มาม่าฉัน..'
                            hide r_shake
                            with dissolve
                            show r_lookup
                            r 'ตั้งเวลาเดิม แล้วนอนซะ'
                            j 'ฮื่ออออ'
                            hide r_lookup
                            jump finish4
        '5.55':
            play sound "audio/Aha.mp3"
            hide r_scaredlittle
            hide j_look down part4
            hide j_relax part4
            with dissolve
            show r_normal
            show j_talk part4
            j 'จะเป็นยังไงนะถ้าตื่นก่อนเวลาสัก 5 นาที'
            hide r_normal
            with dissolve
            show r_repressed
            r 'มีเวลาอีกแค่ 5 นาทีจะตื่นขึ้นมาทำไม!!! นอนต่อไปเถอะ!!!'#แค่ 5
            hide j_relax part4
            hide j_talk part4
            with dissolve
            show j_cry part4
            j 'ฮื่ออออ'
            hide r_repressed
            jump finish4
        '6.00':
            play sound "audio/Aha.mp3"
            hide r_scaredlittle
            hide j_look down part4
            with dissolve
            show r_normal
            show j_relax part4
            j 'ฉันว่าตื่นเวลาเดิมน่ะดีแล้ว'
            jump finish4
label finish4:
    # hide r_scaredlittle
    # hide r_repressed
    # hide r_lookup
    # hide r_smile_angry
    # hide r_shake
    # # with dissolve
    show r_normal
    r 'Good night little girl'
    show j_relax part4
    play sound "audio/girl laugh.mp3"
    j 'บางทีฉันอาจจะเปลี่ยนเป็นดึงหางเจ้ากระต่ายในฝันแทน'
    hide r_normal
    show r_scared_little
    hide r_scared little
    hide j_talk part4 with dissolvess
    'กดรัน 1 ครั้งและกรุณารอสักครู่เพื่อรับชมบรรยากาศในฉากถัดไป'
    play music "audio/crow.mp3" volume 0.8 fadein 1
    scene bg_sunrise part4 with fades
    stop music fadeout 2
    show j_wake up part4 with dissolves
    play sound "audio/magic.mp3"
    j 'เยี่ยมเลยค่ะ วันนี้รู้สึกเต็มอิ่มมากๆ'
    r 'ไม่นอนต่อหรอ นาฬิกายังไม่ปลุกเลยนะ'
    j 'ไม่แล้วค่ะ ตอนนี้กำลังดีมากเลย'
    j 'ว่าแต่วันนี้พระอาทิตย์ขึ้นเร็วจังเลยนะคะ'
    j '(เดี๋ยวก่อนนะ แบบนี้มันแปลกๆแล้ว)'
    'ก๊อก..ก๊อก...'
    m 'ลูกรัก อีก 15 นาทีจะ 7 โมงแล้วนะ ยังไม่ลงมาทานข้าวอีกหรอจ๊ะ'
    play sound "audio/girl crying.mp3"
    show j_poor joshep part4
    with dissolve
    show smile at right
    j 'อะไรนะคะ!!! อีก 15 นาทีจะ 7 โมง มะ มะ ไม่นะ!!!!!!!'
    r 'ฮี่ฮี่ โทษทีนะ พึ่งนึกได้ว่าเมื่อคืนเธอลืมเสียบหัวชาร์จ'
    #The End
    $ renpy.movie_cutscene('images/End-Creedit-final.avi')
    return
