﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Joseph")
define r = Character('Conception')


# The game starts here.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
label start:

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
            j 'ฉันว่าฉันคงจะไม่โชคร้ายขนาดที่ว่ารอครึ่งโมง ชั่วโมงหรอกมั้งคะ'
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
                    r 'แล้วถ้ารถติดเธอ อาจจะต้องติดอยู่บนรถที่มีกลุ่มประชานกรหนาแน่น'
                    r 'คิดดูสิ ติดอยู่กับกลุ่มประชากรเยอะเย้อะ'
                    r 'ออกซิเจนก็จะน้ออยลง คาร์บอนไดออกไซด์ก็เยอะ ทั้งจากมนุษย์และควันรถ'
                    r 'เธออาจจะขาดอากาศหายใจ เป็นลมล้มพับไปก็ได้'
                    r 'จากการที่เธอจะไปโรงเรียน ได้ไปโรงบาลแทนแน่'
                    $ score += 1
                'เธอจะไม่ผ่านวิชาเพราะไปโรงเรียนสาย':
                    # show clock rabbit
                    r 'ถ้าเธอเอาแต่รอรถเมล์ รอไปเรื่อยๆ ทั้งๆที่ไม่รู้ว่าจะมาเมื่อไร'
                    r 'มันเสียเวลาโดยปล่าวประโยชน์ และจะทำให้เธอสาย'
                    r 'อาจารย์ก็จะหักคะแนนคุณ แล้วถ้าคะแนนเธอไม่ดี เพราะจะติด F หรือไม่ก็ไม่ผ่านวิชา'
                    j 'ถึงแม้จะโดนหักคะแนน แต่ไม่ถึงกับติด F หรือไม่ผ่านวิชาหรอกนะคะ'
                    j 'แล้วฉันไม่เคยไปสายด้วย เพราะงั้นไม่ต้องกลัวค่ะ'
                    j 'ฉันจะขึ้นรถเมล์ อย่าขี้กลัวไปหน่อยเลย'
                    $score += 0
            if score > 0:
                menu:
                    'Toxic Level Up':
                        r 'แล้วถ้ากรณีที่รถไม่ติด บางครั้งคนขับก็จะขับซิ่ง เหมือนอย่างกับแข่งรถอย่างงั้นแหละ'
                        r 'แรงพุ่ง แรงเหวี่ยง แรงเบรก จะทำให้เธอกลิ้งหลุดออกจากหน้าต่างก็ได้นะ ยิ่งตัวเล็กๆอยู่ ไปสวรรค์ได้เลย'
                        r 'ถ้าแล้วถ้าไม่ใช่ภัยจากอุบัติเหตุ เธออาจจะเจอภัยจากมนุษย์ด้วยกันเองก็ได้นะ'
                menu:
                    'มีโรคจิตมาลวนลาม':
                        r 'ความไม่คาดคิดของเธอ อาจจะทำให้เธออยู่ในอันตรายเลยก็ได้'
                        r 'มันมีโอกาศที่ฉันจะเจอไอโรคจิตที่จะลวนลามเธอบนรถเมล์ก็ได้ ไม่ก็พวกแอบถ่ายใต้กระโปรง'
                        # show smile but angry rabbit
                        r 'เธอคงจะไม่อยากให้มีแผลใจที่โดนเจ้าพวกโรคจิตมากระทำต่อเธอใช่มั้ย'
                        # damage joseph
                    'โดนขโมยของ':
                        r 'เธออาจจะโดนโจรมาล้วงกระเป๋าก็ได้นะ'
                        r 'ของในกระเป๋าเธอก็มีของสำคัญมากมาย ไม่ก็ของที่มีมูลค่า'
                        r 'ถ้าเธอขัดขื่น เธออาจจะโดนขู่จี้ก็ได้'
                        # spirit out
                        r 'แล้วถ้าเหตุการณืร้ายแรง เธออาจจะโดนมีดจ้วง ไม่ก็โดนปาดคอ'
                        # damage joseph
                r 'เธออาจจะโดนลูกหลงจากเหตุการณืมีคนตีกันบนรถ'
                r 'ถ้าเธอซวยจริงๆอย่างที่ฉันพูดมา เธออาจจะตายก็ได้เลยน'
                r 'ตายน่ะ ตายยยยยยยยยยยยยยยยยยยยย'
                r 'เสียเวลา อันตราย​ เสียเวลา อันตราย เสียเวลา อันตราย เสียเวลา อันตราย​ เสียเวลา อันตราย เสียเวลา อันตราย เสียเวลา อันตรายยยยย'
                #show rabbit win
                jump finish1
            else:
                #show rabbit lose
                jump start2
        'วินมอไซค์':
            r 'เธอใจกล้าเกินไปรึเปล่า'
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
                    r 'ถ้าเธอนั่งวันนี้เธออาจจะเกิดเหตุการณ์​ไม่คาดฝัน​ก็ได้นะ'
                    j 'คงไม่เกิดขึ้นหรอกมั้งคะ เปอร์เซ็นต์การเกิดเหตุไม่ได้มากขนาดนั้นนะ'
                    r 'แล้ว ถ้า เกิด เหตุ ขึ้น มา ล่ะ'
                    r 'เธอรู้มั้ยว่าพ่อแม่เธอจะเสียใจขนาดไหน'
                    r 'พวกท่านจะต้องโทษตัวท่านเองแน่ๆ ว่าทำไมถึงได้ปล่อยให้ลูกที่รักเดินทางเอง ทำไมไม่ดูแลลูกให้ดีกว่านี้'
                    r 'เธออยากจะทำให้พวกท่านเสียใจหรอ'
                    j 'ไม่ ฉันไม่ได้คิดจะให้เป็นแบบนั้น'
                    j 'ตะ แต่ว่า'
                    r 'ไม่! มี! แต่!'
                    r 'ข้อเสียนี่ยังไม่หมดนะ เพื่อนที่รักเธอ และเพื่อนที่เธอรักอีกละ ไหนจะความใฝ่ฝันของเธอที่ตั้งเป้าไว้ว่าจะทำให้สำเร็จ'
                    r 'แล้วถ้าเธอตัดสินใจเลือกวิน แล้วเกิดอะไรขึ้นมา สิ่งที่ตั้งเป้าจะทำให้สำเร็จ เธออาจจะทำให้สำเร็จไม่ได้อีกเลยนะ'
                    # damage joseph
                    # show joseph's little sad
                    jump finish1
    label finish1:
        j 'แล้วฉันควรจะทำยังไง'
        r 'เดิน'
        j 'คะ'
        r 'เดินไปโรงเรียน'
        j 'แต่ว่านี่จะทำให้ไม่ทันเอานะ'
        r 'เชื่อฉันแล้วเธอจะปลอดภัยจากอันตราย แล้วก็ใช่วิธีเดินเร็วๆนะ อย่าวิ่งละ ถ้าหกล้มขึ้นมาจะเป็นเรื่องอีก'
        # show joseph walk
        j 'ฮือ ทำไมฉันต้องมากลัวเรื่องพวกนี้ด้วย'
        # This ends the game.
label start2:
    r '?'
    return

    # This ends the game.

