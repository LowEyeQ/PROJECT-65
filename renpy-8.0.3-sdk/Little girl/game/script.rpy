﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Joseph")
define r = Character('Conception')
define ch = Character("Teacher cho")
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
    pause 1
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

image r_smile_angry:
    "r_smile_angry1.png"
    pause 0.4
    "r_smile_angry2.png"
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

image r_behind = "r_behind.png"

image r_j = "r_j.png"

image r_dad = "r_dad.png"

image r_aunt = "r_aunt.png"

# The game starts here.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #เพิ่ม credit front ท้ายเกม
label start:
    j "เอ๋ วันนี้จะแต่งตัวยังไงดีนะ"
    j "ใส่ตัวนี้แล้วกัน น่าจะเข้ากับบรรยากาศวันนี้นะ"
    j "โอ้ 7 โมงแล้วหรอเนี่ย "
    j "โอเคๆ งั้นถึงเวลาที่ต้องทำผมแล้วสินะคะ"
    j "ไหน ดูซิ ทำผมทรงอะไรดีนะวันนี้"
    j "ถักเปียดีกว่า"
    r "(แม่งเอ้ย จะทำผม***อะไรก็ทำไปเถอะ จะไปโรงเรียนไม่ทันอยู่และ)"
    r "นี่ เธอคิดดีแล้วหรอ ถักเปียหน่ะมันทั้งยุ่งยาก แบ่งช่อก็ยาก มัดตึงมากก็ไม่ได้เพราะมันจะทำให้เธอผมร่วง"
    r "มัดหย่อนมากก็ไม่ดีเพราะมันหลุดง่ายแถมถ้ามัดไว้นานๆผมก็หยักอีก ไม่เป็นทรงด้วยนะเธอ"
    r "มันไม่สวย มันไม่สวยย เอาทรงอื่น!  ไม่รู้ว่าถักแล้วจะเบี้ยวรึป่าวด้วย อย่าถักเลย ทำทรงอื่นเหอะ"
    r "ถ้าเธอมัดผมดังโงะ คนอื่นเขาจะคิดว่าเธอไม่สระผมนะ แต่ถ้ามัดจุกสองข้างมันก็จะน่ารักเกินไปไม่เข้ากับชุดหรอก"
    j "(ไม่ได้สิ ไม่ได้ ไปเรียนทั้งทีก็อยากจะทำผมน่ารักๆนะ)"
    j "..."
    j "ถ้างั้นแล้ว ฉันควรจะทำทรงอะไรดีล่ะคะ"
    menu:
        "มัดรวบ":
            r "เธอจะดูไร้ตัวตนมากเลยนะ ถ้าเธอมัดรวบหน่ะ คนอื่นเขาจะมองว่าการมัดรวบหน่ะมันธรรมดามากเลยน่ะสิ คนส่วนใหญ่ก็มัดรวบกันทั้งนั้น"
            r "มันช่างดูไม่มีสไตล์ที่โดดเด่นเอาซะเลย แล้วถ้าเธอได้เดินไปเจอคนที่เธอแอบชอบหล่ะ เธออยากให้เขาเห็นเธอในสภาพนั้นหรอ"
            r "หรือถ้าเธอไปเดินกับเพื่อน เพื่อนๆต้องไม่อยากให้เธอมาเดินด้วยแน่ พวกเขาต่างมีสไตล์กันทั้งนั้น"
            r "โอ้ย แย่แน่ๆ เปลี่ยนทรงด่วน!"
            r "(อย่างนี้เธอจะเปล่งปรั่งเปร่งประกายได้ยังไง ฉันต้องให้เธอทำทรงผมที่ดีกว่านี้อีก มันยังไม่พอหรอก)"
            j "แต่ฉันว่ามัดรวบมันก็โอเคนะคะ"
            r "ไม่ ฉันไม่โอเค เธอต้องเปลี่ยนทรง"
            j "งั้นจะให้ฉันทำทรงอะไรล่ะคะ"
            r "ฉันให้ลอนผม"
            j "หือ? ลอนผมหรอคะ"
            r "ใช่"
            j "แต่ว่า..มันทำนานนะคะ"
            r "เชื่อฉันเถอะน่า มันสวย มันเริ่ด มันเชิด ต้องจัด"
            j "อะ อ่า.. โอเคค่ะ ลอนผมก็ลอนผม"
        "หนีบผม":
            r "ผมเธอจะเสีย เพราะเธอใช้ความร้อนกับผมมากเกินไป ถ้าหนีบไม่ดีผมเธออาจจะขาดก็ได้นะ"
            r "ผมเธอมันตรงและถ้าหนีบผมหน่ะ มันทำให้ผมเธอไม่มีวอลุ่ม มันไม่งดงามเลย เธอต้องทำทรงทีดีกว่านี้"
            j "ฉันสับสนไปหมดแล้วหล่ะค่ะ"
            j "โอ้ย ฉันจะทำยังไงดี หรือว่า..ฉันจะลอนผมดีคะ"
            r "เธอมั่นใจแล้วหรอว่าเธอจะลอนผมหน่ะ มันทั้งร้อน ทำบ่อยๆผมก็เสีย มันไม่ดีหรอกนะเชื่อฉันสิ"
            j "แต่ว่ามันจะไม่มีเวลาแล้วนะ"
            j "ฉันว่าทรงนี้แหละ เหมาะกับชุดแล้วก็ลุคที่สุดแล้ว"
            r "คิดสิ คิดสิ คิดสิ ทำอะไรดี ทำอะไรดี ทำอะไรดี"
            r "เอาอย่างนั้นก็ได้ ฉันว่ามันก็ไม่ได้แย่เท่าไหร่"
            j "เอ๊ะ แต่มันก็ใช้ความร้อนเหมือนกันนี่นา แต่ทำไมยอมง่ายจังแฮะ"
            j "ช่างเถอะ สายแล้วๆ โอเคฉันลอนผมเลยแล้วกัน"
label start2:
    $ score = 0
    scene road
    #เพิ่มฉาก

    show eileen happy #เดินเข้ามา

    # script

    j "จัดผมก็ได้ใช้เวลาไปสักพักแล้ว วันนี้จะเดินทางยังไงดีนะ"
    menu:
        'รถเมล์':
            r "ฉันถามจริง? เธอก็รู้ตารางรถเมล์ไม่ใช่หรอ"
            j 'รู้ค่ะ'
            r 'รถเมล์เคยมาตรงเวลาซะที่ไหนล่ะ นี่อาจจะทำให้เธอมานั่งรอรถเมล์อย่างเสียเวลาเปล่าก็ได้!!!!'
            j 'ฉันว่าฉันคงจะไม่โชคร้ายขนาดที่ว่ารอครึ่งชั่วโมงหรอกมั้งคะ'
            r 'ถ้าเธอจะคิดในแง่ดีแบบนั้น'
            menu:
                'เพื่อนๆจะเกลียดเธอ เพราะกลิ่นเหงื่อ':
                    r 'งั้นถ้ามีรถเมล์ ก็คงจะเบียดเป็นปลากระป๋อง'
                    r 'แดดร้อนๆ คนเยอะๆ กลิ่นจะเป็นยังไงกันนะ'
                    r 'ใช่! เหม็น! มันเหม็นนนน เธอตัวจะเหม็นนนนนนนน'
                    r 'เพื่อนๆจะต้องรู้สึกรังเกียจเธอแน่เลย เธอจะโดนรังแก แล้วเธอก็จะตัวคนเดียว'
                    $ score += 1
                'เธอจะตายเพราะขาดออกซิเจน!':
                    r 'งั้นถ้ามีรถเมล์ ก็คงจะเบียดเป็นปลากระป๋อง'
                    r 'ไม่มีที่นั่งอีก เธอต้องยืนจนขาเมื่อย ปวดขาตั้งแต่หัววัน'
                    r 'แล้วถ้ารถติดเธอ อาจจะต้องติดอยู่บนรถที่มีกลุ่มประชากรหนาแน่น'
                    r 'คิดดูสิ ติดอยู่กับกลุ่มประชากรเยอะเย้อะ'
                    r 'ออกซิเจนก็จะน้อยลง คาร์บอนไดออกไซด์ก็เยอะ ทั้งจากมนุษย์และควันรถ'
                    r 'เธออาจจะขาดอากาศหายใจ เป็นลมล้มพับไปก็ได้'
                    r 'จากการที่เธอจะไปโรงเรียน ได้ไปโรงบาลแทนแน่'
                    $ score += 1
                'เธอจะไม่ผ่านวิชาเพราะไปโรงเรียนสาย':
                    # show clock rabbit
                    r 'ถ้าเธอเอาแต่รอรถเมล์ รอไปเรื่อยๆ ทั้งๆที่ไม่รู้ว่าจะมาเมื่อไหร่'
                    r 'มันเสียเวลาโดยเปล่าประโยชน์ และจะทำให้เธอสาย'
                    r 'อาจารย์ก็จะหักคะแนนเธอ แล้วถ้าคะแนนเธอไม่ดี เพราะจะติด F หรือไม่ก็ไม่ผ่านวิชา'
                    j 'ถึงแม้จะโดนหักคะแนน แต่ไม่ถึงกับติด F หรือไม่ผ่านวิชาหรอกนะคะ'
                    j 'แล้วฉันไม่เคยไปสายด้วย เพราะงั้นไม่ต้องกลัวค่ะ'
                    j 'ฉันจะขึ้นรถเมล์ อย่าขี้กลัวไปหน่อยเลย'
                    $score += 0
            if score > 0:
                menu:
                    'Toxic Level Up':
                        r 'แล้วถ้ากรณีที่จราจรไม่ติดขัด บางครั้งคนขับก็จะขับซิ่ง เหมือนอย่างกับแข่งรถอย่างงั้นแหละ'
                        r 'แรงพุ่ง แรงเหวี่ยง แรงเบรก จะทำให้เธอกลิ้งหลุดออกจากหน้าต่างก็ได้นะ ยิ่งตัวเล็กๆอยู่ ไปสวรรค์ได้เลย'
                        r 'ถ้าแล้วถ้าไม่ใช่ภัยจากอุบัติเหตุ เธออาจจะเจอภัยจากมนุษย์ด้วยกันเองก็ได้นะ'
                menu:
                    'มีโรคจิตมาลวนลาม':
                        r 'ความไม่คาดคิดของเธอ อาจจะทำให้เธอตกอยู่ในอันตรายเลยก็ได้'
                        r 'มันมีโอกาสที่เธอจะเจอไอโรคจิตที่จะลวนลามเธอบนรถเมล์ก็ได้ ไม่ก็พวกแอบถ่ายใต้กระโปรง'
                        # show smile but angry rabbit
                        r 'เธอคงจะไม่อยากให้มีแผลใจที่โดนเจ้าพวกโรคจิตมากระทำต่อเธอใช่มั้ย'
                        # damage joseph
                    'โดนขโมยของ':
                        r 'เธออาจจะโดนโจรมาล้วงกระเป๋าก็ได้นะ'
                        r 'ของในกระเป๋าเธอก็มีของสำคัญมากมาย ไม่ก็ของที่มีมูลค่า'
                        r 'ถ้าเธอขัดขืน เธออาจจะโดนขู่จี้ก็ได้'
                        # spirit out
                        r 'แล้วถ้าเหตุการณ์ร้ายแรง เธออาจจะโดนมีดจ้วง ไม่ก็โดนปาดคอ'
                        # damage joseph
                r 'เธออาจจะโดนลูกหลงจากเหตุการณ์มีคนตีกันบนรถ'
                r 'ถ้าเธอซวยจริงๆอย่างที่ฉันพูดมา เธออาจจะตายก็ได้เลยนะ'
                r 'ตายน่ะ ตายยยยยยยยยยยยยยยยยยยยย'
                r 'เสียเวลา อันตราย​ เสียเวลา อันตราย เสียเวลา อันตราย เสียเวลา อันตราย​ เสียเวลา อันตราย เสียเวลา อันตราย เสียเวลา อันตรายยยยย'
                #show rabbit win
                jump finish2
            else:
                #show rabbit lose
                jump start3
        'วินมอไซค์':
            r 'เธอใจกล้าเกินไปหรือเปล่า'
            j 'แต่ว่านี่เป็นทางเลือกที่เร็วที่สุดแล้วนะ'
            r 'ก็ใช่ แต่ ทางนี้ก็ใช้เงินมากที่สุดเหมือนกัน'
            r 'แถมยังสามารถโกงราคาได้อีก มันไม่ใช่ราคาที่ตรงตัวเลย'
            r 'กำหนดได้ตามใจพวกเขาอีก บางทีเธออาจจะโดนโกง 10-20 บาทเลยนะ'
            j 'ไม่เป็นไร วันนี้ฉันยอมเสียเงินได้'
            r '(โอ้ไม่ได้การแล้ว ถ้าเป็นแบบนี้เธอจะต้องตกอยู่ในอันตราย​แน่เลย ฉันจะต้องปกป้อง!)'
            menu:
                'Toxic Level up':
                    r 'อย่างที่เธอบอกในตอนแรก ทางเลือกที่ "เร็วที่สุด" ที่เร็วที่สุดก็เพราะว่าเขาขับเร็วมากๆ'
                    r 'แล้วถ้าเกิดอุบัติเหตุ​ล่ะ บางทีเขาก็ไม่มีหมวกกัน​น็อค​ให้ใส่ป้องกันอีก'
                    r 'เธอก็เห็นข่าวที่เกี่ยวกับอุบัติเหตุ​ทางถนนอยู่บ่อยๆหนิ'
                    r 'ถ้าเธอนั่งวันนี้ เธออาจจะเกิดเหตุการณ์​ไม่คาดฝัน​ก็ได้นะ'
                    j 'คงไม่เกิดขึ้นหรอกมั้งคะ เปอร์เซ็นต์การเกิดอุบัติเหตุไม่ได้มากขนาดนั้นนะ'
                    r 'แล้ว ถ้า เกิด เหตุ ขึ้น มา ล่ะ'
                    r 'เธอรู้มั้ยว่าพ่อแม่เธอจะเสียใจขนาดไหน'
                    r 'พวกท่านจะต้องโทษตัวท่านเองแน่ๆ ว่าทำไมถึงได้ปล่อยให้ลูกสุดที่รักเดินทางเอง ทำไมไม่ดูแลลูกให้ดีกว่านี้'
                    r 'เธออยากจะทำให้พวกท่านเสียใจหรอ'
                    j 'ไม่ ฉันไม่ได้คิดจะให้เป็นแบบนั้น'
                    j 'ตะ แต่ว่า'
                    r 'ไม่! มี! แต่!'
                    r 'ข้อเสียนี่ยังไม่หมดนะ เพื่อนที่รักเธอ และเพื่อนที่เธอรักอีกล่ะ ไหนจะความใฝ่ฝันของเธอที่ตั้งเป้าไว้ว่าจะทำให้สำเร็จ'
                    r 'แล้วถ้าเธอตัดสินใจเลือกวินมอไซค์ แล้วเกิดอะไรขึ้นมา สิ่งที่ตั้งเป้าจะทำให้สำเร็จ เธออาจจะทำให้สำเร็จไม่ได้อีกเลยนะ'
                    # damage joseph
                    # show joseph's little sad
                    jump finish2
    label finish2:
        j 'แล้วฉันควรจะทำยังไง'
        r 'เดิน'
        j 'คะ'
        r 'เดินไปโรงเรียน'
        j 'แต่ว่านี่จะทำให้ไม่ทันเอานะ'
        r 'เชื่อฉันแล้วเธอจะปลอดภัยจากอันตราย แล้วก็ใช้วิธีเดินเร็วๆนะ อย่าวิ่งละ ถ้าหกล้มขึ้นมาจะเป็นเรื่องอีก'
        # show joseph walk
        j 'ฮือ ทำไมฉันต้องมากลัวเรื่องพวกนี้ด้วย'
        # This ends the game.
label start3:
    #school
    j 'ฟู่ว มาทันเวลาด้วยล่ะค่ะ'
    r 'เก่งมากสาวน้อย เข้าห้องเรียนกันเถอะ'
    #classroom
    ch 'นักเรียนจ๊ะ คะแนนสอบย่อยครั้งที่แล้วออกแล้วนะจ๊ะ'
    j 'เอ๊ะ!'
    ch 'พอครูเรียกชื่อแล้วก็ออกมารับนะจ๊ะ เด็กชายสมชาย...เด็กหญิงโฟกัส'
    j 'เอาล่ะๆ เกรดออกแล้ว ลุ้นจังเลยค่ะ'
    r 'โอ๊ยๆๆๆ เมื่อไหร่จะถึง'
    ch 'เด็กหญิงแม่น้ำไนล์...เด็กหญิงออมเงิน...เด็กชายแจ็คฟรุ๊ต'
    j 'ฉันเคยคิดว่าที่บ้านเขาต้องชอบกินขนุนมากแน่เลยถึงตั้งชื่อว่าแจ๊คฟรุ๊ต'
    ch 'เด็กหญิงโจเซฟ'
    j 'ตาฉันแล้วค่ะ'
    # little girl stand upppp
    #โจเซฟไม่ได้ดูคะแนนของเธอทันที เธอกลับไปนั่งที่โต๊ะเพื่อลุ้นคะแนนที่เธอจะได้
    j 'ฟู่ว ใจเต้นแรงไปหมดเลยค่ะ'
    r 'รีบๆดูเร็วๆๆๆ'
    j 'โอเค นับ 3...2'
    r 'ฮึ่ยยย'
    j '1....!!! ทำไมมัน!...ออกมาเป็นแบบนี้ล่ะคะ'
    r 'โอ้วตายแล้ว งานนี้แย่แน่ๆ'
    j 'มะ ไม่ขนาดนั้นหรอกค่ะ..'
    r 'ไม่ มันขนาดนั้นแหละ คิดดูสิมันจะเกิดอะไรขึ้นถ้าทุกคนรู้ว่าเธอได้เกรดเท่านี้'
    j 'เกรดมันก็แค่..ไม่ๆ ทุกคนไม่ใจร้ายขนาดนั้นหรอกค่ะ'
    r 'ทุกคนอย่างนั้นหรอ พอทุกคนรู้เกรดของเธอแล้วจะไม่มีอะไรเปลี่ยนแปลงเลยอย่างนั้นหรอ'
    menu:
        'อาจารย์':
            r 'รู้อะไรมั๊ย คนแรกที่รู้เกรดของเธอคืออาจารย์'
            j 'แน่นอนอยู่แล้วค่ะ เพราะเขาเป็นคนให้เกรดหนิคะ'
            r 'และเขาก็จะรู้ว่า เด็กสาวคนนี้มันไม่เอาไหน'
            j 'คนเป็นอาจารย์เขาจะคิดแบบนั้นได้ยังไงล่ะคะ'
            r 'เธออ่านใจเขาได้หรอ จะบอกอะไรให้นะ คนเป็นอาจารย์น่ะ เขาชอบและใส่ใจกับเด็กที่เรียนเก่งเกรดดี'
            r 'หลังจากนี้เธอคงได้รับสายตาดูแคลนการเขาแล้วล่ะ ระวังตอนเช็คชื่อให้ดีนะหรือเขาจะทำเป็นไม่เห็นชือเธอกันนะ'#ดูแคลนการเขา
            j 'ฉันเชื่อว่าอาจารย์ไม่ใจร้ายขนาดนั้นหรอกค่ะ เขาบทบาทที่จะทำให้พวกเราเป็นคนที่ดีขึ้น เราต้องให้ใจกับเขาด้วย'#เขาบทบาท
            r 'ตามใจเธอก็แล้วกัน'
            $ score += 0
        'เพื่อน':
            r '"ไม่เห็นจะเรียนเก่งเท่าไหร่เลย" เดินๆอยู่ประโยคนี้คงตามหลอกหลอนเธอไปสักพักเลยนะ'
            j 'นั่นมันใจร้ายเกินไปแล้ว ไม่ๆ ทุกคนต้องเข้าใจแน่นอนค่ะ'
            r 'นั่งกินข้าวคนเดียวก็คงจะเหงาแย่เลยนะ'
            r 'วันไหนลืมเอากระเป๋ามา ระวังไม่มีที่นั่งล่ะ'
            r 'ตอนขึ้นไปเรียนก็คงไม่มีที่นั่งดีๆสำหรับเธอแล้ว'
            j 'ไม่มีใครตัดสินคนจากความผิดพลาดเพียงครั้งเดียวหรอกค่ะ...'
            r 'และงานกลุ่มก็จะไม่มีใครเอาเธอมาอยู่ด้วย!!'
            r 'และไม่มีที่ไหนรับคนคะแนนน้อยเข้าทำงานแน่นอนนนนนน'
            j 'ฮือ นี่มันทำฉันรู้สึกแย่จนปวดท้องไปหมดแล้ว'
            r 'สาวน้อยคนนี้จะเป็นที่จดจำในงานเลี้ยงรุ่น'
            $ score += 1
        'ครอบครัว':
            r '"พ่อคะแม่คะ วันนี้เกรดออกแล้ว แต่มันไม่ค่อยดีเลยค่ะ"'
            r '"ไม่เป็นไรหรอกลูก ครั้งหน้าเอาใหม่ได้นะ"'
            r 'ถ้าพ่อกับแม่ตอบเธอมาแบบนี้ ลองหยิกตัวเองดูนะ เผื่อเธอกำลังฝันอยู่'
            j 'ฉันไม่อยากให้พวกท่านเสียใจเลยค่ะ ฉันไม่อยากบอก แต่ยังไงพวกท่านก็ต้องรู้'
            r 'ไม่อยากบอกก็ไม่ต้องบอกสิ ไม่ใช่เรื่องที่ต้องกังวลเลย'
            j 'ทำยังไงดีล่ะคะ'
            r 'ทำลายมันสิ เผามัน ปั้นกลมๆแล้วโยนลงน้ำ'
            j 'ฉันจะ....ไม่ ฉันจะไม่ทำอย่างนั้นค่ะ คุณพ่อคุณแม่คือคนที่เข้าใจฉันที่สุด'
            r 'แต่ไม่ใช่กับป้าข้างบ้าน'
            j 'ป้าข้างบ้านไม่เกี่ยวนะคะ'
            r 'โถ่ๆ มีะไรที่ป้าข้างบ้านไม่รู้บ้าง และเคยได้ยินประโยคนี้มั๊ย "ป้าข้างบ้านรู้ คนทั้งโลกรู้"'
            r 'วันนึงอาจจะมีคุณป้าที่ไหนไม่รู้มาทักทายเธอ แล้วคิดว่าป้ารู้จักเธอได้ยังไงล่ะ'
            j 'ป้าเป็นเพื่อนของคุณพ่อคุณแม่'
            r 'มั่วแล้ว ก็เธอคือยัยหนูที่เกรดแย่ไงงงงง'
            r 'พ่อกับแม่คงเหนื่อยกับยัยหนูนั่นแย่เลยสินะเนี่ย ฮี่ๆๆๆๆ'
            menu :
                'บอกครอบครัว':
                    j 'ขอแค่คุณพ่อกับคุณแม่เข้าใจฉันก็พอแล้วค่ะ บางทีเราไม่จำเป็นต้องใส่ใจว่าคนอื่นจะมองยังไง'
                    r 'ที่ฉันพูดไปเธอได้ฟังรึเปล่า รู้มั๊ยว่าเด็กเกือบ 90 เปอร์เซ็นต์ ของทั้งโลกจะเป็นโรคซึมเศร้าเพราะป้าข้างบ้าน'
                    j 'ฉันจะเป็นอีก 10 เปอร์เซ็นต์ที่เหลือเองค่ะ'
                    r 'เธอท้าทายอำนาจมืดแล้วล่ะ'
                    j 'แต่จริงๆแล้วไม่ใช่ว่าคุณป้าทุกคนจะใจร้ายเสมอไปนะคะ'
                    $ score += 0
                'ครอบครัวคงไม่เข้าใจ':
                    j 'พวกท่านต้องไม่เข้าใจแน่ค่ะ'
                    r 'เราแค่ป้องกันกรณีที่ร้ายแรงที่สุด คือพวกเขาจะห้ามไม่ให้เธอทำงานอดิเรกอีกเลย'
                    r 'ไม่มีนิยายให้เธออ่าน ทุกอย่างถูกกีดกัน เพื่อให้เธอมีเวลาโฟกัสกับเรื่องการเรียนให้มากที่สุด'
                    j 'นั่นมันแย่มาก ฉันจะไม่บอกพวกเขาเด็ดขาดเลย'
                    $ score += 1
        'คนที่แอบชอบ':
            j 'เขาเป็นคนดีนะคะ ฉันเคยเห็นเขาช่วยติวให้เพื่อนๆด้วย'
            r 'แสดงว่าเขาต้องเป็นคนที่เก่งมากๆ เธอหมดโอกาสแล้วล่ะ'
            menu:
                'พลิกวิกฤตให้เป็นโอกาส':
                    j 'ไม่หรอกค่ะ ไม่แน่ฉันอาจจะขอเข้าร่วมการติวในครั้งหน้าด้วย'
                    r 'เพ้อฝันจริงๆเลยยัยเด็กคนนี้'
                    $ score += 0
                'ตัดใจ':
                    r 'ดูท่าทีเหงาหงอยนั่นสิ ไม่เป็นไรนะฉันจะอยู่กับเธอเอง'
                    $ score += 1
    if score > 1:
        menu:
            'Toxic Level Up':
                r 'ฉันฟันธงเลยว่าเธอคงอยากจะลาออกแน่นอน เป็นสาวน้อยที่แย่จังเลยน้าาา'
                # show smile but angry rabbit
                r 'เงินค่าเทอมตรงนั้นสามารถเอาไปใช้ประโยชน์ได้หลายอย่างแต่เธอดันทำให้มันเสียเปล่าซะได้ ตัดสินใจผิดพลาดจริงๆ'
                # damage joseph
                r 'ไม่ใช่เงินที่หาเธอมาด้วยตัวเองอีก ได้ยินมั๊ยว่าเงินน่ะ! เป็นของมีค่าที่ถูกเธอผลาญไปอย่างเปล่าประโยชน์'
                r 'อนาคตคงเธอมืดบอด ไร้จุดหมายและมีปลายทางที่เตียงนอนกับหมอนเน่า ฟังดูดีหรอ ไม่เลย เธอจะกลายเป็นตัวไร้ประโยชน์ในบ้าน'
                # spirit out
                r 'อยู่ในห้องตลอดไป!!!!'
                # damage joseph and show rabbit win
                jump finish3
    else:
        #show rabbit lose
        jump start4
label finish3:
    j 'ฉันไม่ควรบอกวามจริงกับทุกคน'
    r 'ใช่แล้วสาวน้อย ทุกคนจะปฏิบัติกับเธอแบบเดิม'
    j 'ฉันจะบอกกับทุกคนว่าฉันจะเก็บกลับไปดูกับพ่อแม่'
    r 'นั่นดีมาก และพอกลับบ้านก็ผลัดวันไปเรื่อยๆ แน่นอนว่าจะไม่มีใครได้เห็นใบกระดาษใบนั้นอีก happy ending!!'
    j 'ฉันไม่ชอบแบบนี้เลยค่ะ'
    # This ends the game

label start4:
    # bedroom
    r 'ได้เวลานอนกันแล้ว มีความฝันที่อยากได้มั๊ยสาวน้อย'
    j 'ฉันอยากฝันว่าได้เล่นกับกระต่าย'
    # show happy rabbit face
    j 'บางทีถ้ากระต่ายตัวนั้นกัดฉัน ฉันจะขโมยแครอทเขา'
    # show rabbit scaried face
    j 'แต่ฉันหวังว่ากระต่ายจะดีกับฉันนะคะ ดังนั้นเราจะมีความสุขอยู่ด้วยกัน'
    r 'ฉันก็หวังแบบนั้น'
    j 'โอ๊ะ เกือบลืมเลย ตั้งปลุกกี่โมงดีนะ'
    menu:
        '4.00':
            r 'เดี๋ยวก่อนนะ แล้วเวลาอีก 120 นาทีสำหรับการนอนอันมีค่าล่ะ'
            j 'บางทีฉันก็อยากเปลี่ยนไลฟ์สไตล์ชีวิตดูบ้าง'
            r 'ไหนบอกฉันหน่อยสิว่าเธอตั้งใจจะทำอะไร'
            menu:
                'ออกกำลังกายตอนเช้า':
                    j 'เพื่อนๆฉันบอกว่า การออกกำลังนอกจากจะส่งผลดีต่ออสุขภาพ ยังทำให้สมองเราทำงานได้ดีขึ้นอีกด้วยนะคะ'
                    r 'อย่างนั้นหรอ เธอมั่นใจได้ยังไงว่าไม่ใช่แผนให้เธอไปหลับในห้องเรียนน่ะ'
                    j 'เพื่อนคนนี้เขาเรียนเก่งมากๆเลยนะคะ'
                    r 'แล้วเธอรู้ได้ยังไงว่าเพื่อนคนนั้นเรียนเก่งเพราะออกกำลังกาย'
                    j 'ฉันเห็นเขาลงรูปในโซเชียลค่ะ'
                    r 'อะไรนะ!!'
                    r 'ในตายเถอะสาวน้อย เธอกำลังบอกว่าเธอเชื่อสิ่งที่อยู่ในโซเชียลอย่างนั้นหรอ'
                    r 'เธอไม่เคยเห็นพวกคนที่แต่งชุดออกกำลังกายตามแฟชั่นบ้างหรอ แท้จริงแล้วหุ่นดีๆพวกนั้นก็มาจากยาลดความอ้วนทั้งนั้นแหละ'
                    r 'สาวน้อยอ่อนต่อโลกอย่างเธอตามเรื่องพวกนี้ไม่ทันหรอก อยากเรียนเก่งก็แค่อ่านหนังสือก็พอแล้ว เอา 120 นาทีที่เหลือไปนอนพักสมองดีกว่า'
                    j 'ออกให้ไม่เหนื่อยมากก็ได้หนิคะ'
                    r 'งั้นบอกมาสิว่าเธอจะออกกำลังกายยังไง'
                    menu:
                        'วิ่ง':
                            r 'วิ่งงั้นหรอ!!!! เธอไม่กลัวสะดุดล้มรึไง สะดุดล้ม เข่าถลอก แผลติดเชื้อ บาดทะยัก ตัดขา!!!'
                            j 'ไม่ได้วิ่งเร็วขนาดนั้นนะคะ'
                            r 'การวิ่งของเธออาจจะไปยั่วโมโหหมาเจ้าถิ่นจนพวกมันพาพวกมาวิ่งไล่กวดเธอ!!!'
                            r 'หรือไม่เธออาจจะเจอเจ้าแมวน่ารักๆ ซึ่งนั่นดึงดูดให้เธอเข้าไปเล่นด้วย แต่เจ้าแมวตัวนี้กลัวเธอและตวัดเล็บใส่'
                            r 'ที่น่ากลัวกว่านั้น ถ้าเธอโดนแมวกัดล่ะก็ รู้มั๊ยว่านั่นร้ายแรงกว่าโดนหมากัดอีกนะ เชื้อโรคในปากแมวมันน่ากลัวมาก เธอรู้บ้างรึเปล่า!!!'
                            j 'ฉะ ฉันไม่เล่นกับพวกน้องแมวก็ได้ค่ะ'
                            r 'เธออดใจไหวหรอ!! เจ้าสัตว์หน้าขนปุกปุย อุ้งเท้านุ่มนิ่ม เสียงร้องน่าเอ็นดู แต่ในร่างกายไหลเวียนด้วยเลือดนักสู้ไทยพวกนั้นน่ะ มีใครอดใจไม่สัมผัสได้บ้าง!!!'
                            j 'ฮืออออ ฉันจะไม่เข้าใกล้สัตว์น่ารักแล้ว'
                            r 'ยังไม่หยุดแค่นี้นะ ถ้าวิ่งๆอยู่ฝนเกิดตกขึ้นมาล่ะ และก็ตกหนักๆๆๆขึ้นเรื่อยๆ ทีนี้แหละเธอจะไม่มีทางเลือก นอกจากรีบวิ่งกลับบ้าน สุดท้ายก็มีโอกาสสะดุดล้มอยู่ดีแถมเปอร์เซ็นต์มากกว่าเดิมอีก!!'
                            r 'ฝนที่อยู่ๆก็ตกจะพาฝุ่นละอองที่อยู่บนฟ้ามากระทบตัวเธอซึ่งนั่นอันตรายมาก ถ้าเธออาบน้ำไม่ทันเธอมีโอกาสเสี่ยงเป็นหวัดสูงมากๆๆๆๆๆ'
                            r 'สุดท้ายนี้เธอก็ต้องหยุดเรียนเป็นสัปดาห์!!!'
                            r 'period!'
                            j 'อะไรคือ period ล่ะคะนั่น'
                            r 'ฉันคงบอกเธอไว้แค่'#ไว้เเค่
                            jump finish4
                        'เต้น':
                            j 'ฉันมีคลิปนึงที่อยากเต้นตามอยู่'
                            r 'ข้อมือเธอจะเหวี่ยงไปฟาดอะไรสักอย่างจนกระดูกหักได้นะ'
                            j 'ท่าเต้นไม่ค่อยมีเหวี่ยงแขนขนาดนั้นหรอกค่ะ'
                            r 'หรืออาจจะลื่นล้มหัวฟาดพื้น!!!'
                            r 'เสียงล้มของเธอจะทำให้พ่อแม่ตื่นและรีบวิ่งมาดู และพอรู้ว่าเกิดอะไรขึ้น พวกเขาจะแบนการเต้น'
                            r '"มันเป็นอันตรายต่อลูก ต่อไปนี้เราจะยึดมือถือไม่ให้ลูกดูอะไรพวกนี้อีก และเราจะคอยจับตาดูลูกด้วย"'
                            r 'สุดท้ายนี้เธอจะเกลียดการเต้น และคิดว่าถ้าย้อนเวลากลับไปได้ ฉันจะไม่ทำแบบนั้น!!!'
                            r 'ฉะนั้นแล้ว วิธีคงอิสรภาพไว้คือตั้งปลุกแบบเดิมซะ'
                            jump finish4
                        'โยคะ':
                            j 'โยคะดูทำง่ายดีนะคะ ใช้พื้นที่ไม่เยอะด้วย'
                            r 'ฟังดูดีนะ ไหนฉันขอคำนวณความเสี่ยงให้เธอหน่อย'
                            r 'เธอเสี่ยงเป็นอัมพาตจากโยคะผิดท่า'
                            r 'โอ้ว ไหนจะตะคริวตัวร้าย'
                            r 'หรือเธออาจจะทำไม่ถูกวิธี ซึ่งนั่นทำให้การออกกำลังกายตอนเช้ามันสูญเปล่า'
                            r 'เธออาจจะตายได้เพราะไม่รู้วิธีจัดการตนเองเมื่อร่างกายเหนื่อยเกินไป'
                            r 'สุดท้ายนี้มันจะทำให้เธอไม่สามารถไปโรงเรียนได้ และผลการเรียนเธอก็ตกลงอีกครั้ง'
                            r 'ตั้งปลุกแบบเดิมซะ'
                            jump finish4

                'กินข้าวเช้าที่โรงเรียน':
                    r 'ฉันรู้สึกว่านี่เป็นเรื่องที่บ้ามาก ข้าวที่บ้านไม่อร่อยหรอ'
                    j 'อร่อยที่สุดอยู่แล้วค่ะ'
                    r 'ทั้งอร่อยและไม่ต้องเสียเงิน แล้วเธอจะตื่นเช้าไปกินทำไมกัน'
                    j 'ฉันยังพอมีเงินเก็บอยู่นะคะ ลองสักครั้งคงไม่เป็นอะไร'
                    r 'ฉันไม่อยากจะพูดแบบนี้หรอกนะ แต่การใช้เวลาอยู่กับครอบครัวเป็นสิ่งที่เราไม่สามารถย้อนกลับมาเรียกคืนได้หรอกนะ'
                    r 'แม่ของเธอจะตรอมใจเพราะคิดว่าฝีมือทำอาหารของตัวเองแย่มาก จนลูกสาวต้องรีบตื่นเช้าไปกินข้าวที่โรงเรียนแทน'
                    r 'แม่ของเธออาจจะแอบไปร้องไห้ซึ่งนั่นทำให้คุณพ่อทุกข์ใจที่ตนเองไม่สามารถทำอาหารได้อยู่แล้ว'
                    r 'เกิดความร้าวฉานในครอบครัวเพราะ! เธอ! ไม่! ยอม! กิน! อาหาร! ฝี! มือ! แม่ !!!!!'
                    # น้อนร้องห้ายยยยยยยย
                    j 'ฉันรักมัมมี๊ รักแด๊ดดี๊ด้วย'
                    r 'ไว้บอกอีกทีบนโต๊ะอาหาร'
                    jump finish4

                'แค่อยากตื่นเช้า':
                    r 'นั่นมันบ้ามาก เธอจะตื่นมารอสังเคราะห์แสงแรกของวันหรอ เสียเวลาชีวิตเกินไปแล้ว'
                    j 'บางทีฉันอาจจะลองทำข้าวเช้า'
                    r 'เมนูอะไร ทอด ต้ม นึ่งหรือย่างล่ะ'
                    menu:
                        'ขนมปังปิ้งกับไข่ดาว':
                            j 'แค่ขนมปังปิ้งกับไข่ดาวธรรมดาก็พอแล้วค่ะ'
                            r 'นี่มีปิ้งด้วยหรอ โอ้วให้ตายเถอะ ไข่ดาวนั่นเธอรู้รึเปล่ามีอัตราการบาดเจ็บจากการทำอาหารเป็นจำนวนเท่าไหร่ โดยเฉพาะเมนูที่ใช้น้ำมัน!!!'
                            r 'น้ำมันที่กระเด็นด้วยความร้อนสูงแบบนั้นสามารถละลายผิวหนังเธอจนเป็นแผลเป็นได้เลยนะ'
                            r 'ระหว่างนั้นมันจะเจ็บปวดแค่ไหน หรือบางทีอาจจะไม่ใช้น้ำมันที่กระเด็นมาโดนแต่มีอะไรบางอย่างไปเกี่ยวกระทะจนน้ำมันหกราดใส่ตัวเธอ น้ำมันร้อนๆ!! กับค่ารักษาที่ตามมา!!!'
                            r 'เอาเป็นว่าเราจะไม่พูดถึงเรื่องนี้อีก แบบนี้ปลอดภัยกับเธอแล้ว'
                            jump finish4
                            # show joseph sad face
                        'ไข่ต้มยามเช้า':
                            j 'ไข่ต้มก็ดีนะคะ ดีต่อสุขภาพด้วย'
                            r 'เธอกะเวลาต้มได้อย่างนั้นหรอ ถ้าโชคร้ายมากจับได้ไข่ที่ไม่ปกติขึ้นมา และโชคร้ายอีกที่เธอต้มมันนานเกินไปจนมันระเบิดออกมา!!'
                            r 'ให้ตายสิ ฉันจินตาการกลิ่นออกเลย นี่มันสมรภูมิชัดๆ'
                            j 'ไข่เน่ามาได้ยังไงคะนั่น'
                            r 'ใครจะรู้ หรือเธอสามารถมองทะลุผ่านเปลือกไข่ได้อย่างนั้นหรอ'
                            r 'เอ๊ะๆๆๆๆ หรือว่า'
                            r 'เธออาจจะต้มมันออกมาได้ดีมาก แต่มันรู้ตัวอีกทีตอนเธอปลอกมันแล้วมันระเบิดใส่หน้าเธอ!!!'
                            r 'โอ้วว ยกเลิกแผนนี้เถอะ มันเสี่ยงเกินไป เธอแค่ตั้งเวลาตามปกติแล้วนอนอย่างสบายใจก็พอแล้ว'
                            j 'ฮื่ออออ'
                            # show joseph sad face
                            jump finish4
                        'มาม่า':
                            j 'ฉันไม่ได้ใช้โควตาทานมาม่ามานานแล้ว บางทีทำมาม่าทรงเครื่องตอนเช้าก็ดีนะคะ'
                            r 'เอาล่ะ ฉันคงพูดได้ว่า ผู้คนมากมายป่วยเป็นโรคไตเพราะการทานมาม่า'
                            j 'นั่นเพราะพวกเขาทานแบบแห้งไม่ใช่หรอคะ ฉันตั้งใจจะต้มนะ'
                            r 'ใครบอกเธอแบบนั้นน่ะ'
                            j 'ผู้คนแชร์เรื่องนี้กันในโซเชียล'
                            r 'เธอ! หยุด! เชื่อ! ทุก! อย่าง! ใน! โซเชียลเดี๋ยวนี้!!!!!'
                            r 'ผู้คนเป็นโรคไตเพราะโซเดียมในมาม่า เธอบอกว่าเธอเอาไปต้มแล้วคิดว่าโซเดียมจะหายไปอย่างนั้นหรอ'
                            r 'ยังไงเธอก็ต้องใส่เครื่องปรุงและซดน้ำทุกหยดอยู่ดีนั่นแหละ'
                            r 'และโรคไตน่ะ มันทรมาณแค่ไหนรู้มั๊ย เธอจะอ่อนเพลียไม่มีแรง ปวดหลังปวดเอวหัว ปวดไปหมด!!!'
                            r 'และเธอจะต้องขาดเรียนไปรักษาตัวด้วย'
                            j 'แต่ฉันไม่ได้กินมันบ่อยๆนะคะ'
                            r 'เธออาจจะติดใจจนเป็นอันกินอะไรไม่ได้ถ้าไม่ใช่เมนูนี้ โอ้ พระเจ้า ฉันไม่อยากคิดถึงตอนที่เธอตัวบวมเพราะแค่มาม่ามื้อเช้านั่น'
                            r 'เอาล่ะสาวน้อยคิดถึงพ่อกับแม่ไว้สิ ตื่นเวลาเดิมและรอทานมื้อเช้าแสนอร่อยทรงคุณค่าของแม่ก็พอแล้ว ไม่เสียเวลานอน ไม่เสียสุขภาพ'
                            j 'โถ่ มาม่าฉัน..'
                            r 'ตั้งเวลาเดิม แล้วนอนซะ'
                            j 'ฮื่ออออ'
                            jump finish4
        '5.55':
            j 'จะเป็นยังไงนะถ้าตื่นก่อนเวลาสัก 5 นาที'
            r 'มีเวลาอีกแค่ 5 จะตื่นขึ้นมาทำไม!!! นอนต่อไปเถอะ!!!'#แค่ 5
            j 'ฮื่ออออ'
            # show joseph sad face
            jump finish4
        '6.00':
            j 'ฉันว่าตื่นเวลาเดิมน่ะดีแล้ว'
            jump finish4
label finish4:
    r 'Good night little girl'
    j 'บางทีฉันอาจจะเปลี่ยนเป็นดึงหางเจ้ากระต่ายในฝันแทน'
    # fade scene
    # show the sun
    # show joseph wake up(บิดขี้เกียจด้วย)
    j 'เยี่ยมเลยค่ะ วันนี้รู้สึกเต็มอิ่มมากๆ'
    r 'ไม่นอนต่อหรอ นาฬิกายังไม่ปลุกเลยนะ'
    j 'ไม่แล้วค่ะ ตอนนี้กำลังดีมากเลย'
    j 'ว่าแต่วันนี้พระอาทิตย์วันนี้ขึ้นเร็วจังเลยนะคะ'
    # joshep take her phone to check time
    # the phone has not reponse
    j '(เดี๋ยวก่อนนะ แบบนี้มันแปลกๆแล้ว)'
    #..ก๊อก ก๊อก..
    # someone knock the door
    m 'ลูกรัก อีก 15 นาทีจะ 7 โมงแล้วนะ ยังไม่ลงมาทานข้าวอีกหรอจ๊ะ'
    j 'อะไรนะคะ!!! อีก 15 นาทีจะ 7 โมง มะ มะ ม๊าย!!!!!!!'
    r 'ฮี่ฮี่ โทษทีนะ พึ่งนึกได้ว่าเมื่อคืนเธอลืมเสียบหัวชาร์จ'
    #The End

    return

    # This ends the game.

