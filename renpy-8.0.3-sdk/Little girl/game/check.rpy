# for project
label start3:
    #school
        j 'ฟู่ว มาทันเวลาด้วยล่ะค่ะ'
        r 'เก่งมากสาวน้อย เข้าห้องเรียนกันเถอะ'
        #classroom
        Teacher 'ฉันเรียนจ๊ะ คะแนนสอบย่อยครั้งที่แล้วออกแล้วนะจ๊ะ'
        j 'เอ๊ะ!'
        Teacher 'พอครูเรียกชื่อแล้วก็ออกมารับนะจ๊ะ เด็กชายสมชาย...เด็กหญิงโฟกัส'
        j 'เอาล่ะๆ เกรดออกแล้ว ลุ้นจังเลยค่ะ'
        r 'โอ๊ยๆๆๆ เมื่อไหร่จะถึง'
        Teacher 'เด็กหญิงแม่น้ำไนล์...เด็กหญิงออมเงิน...เด็กชายแจ็คฟรุ๊ต'
        j 'ฉันเคยคิดว่าที่บ้านเขาต้องชอบกินขนุนมากแน่เลยถึงตั้งชื่อว่าแจ๊คฟรุ๊ต'
        Teacher 'เด็กหญิงโจเซฟ'
        j 'ตาฉันแล้วค่ะ'
        # little girl stand upppp
        #โจเซฟไม่ได้ดูคะแนนของเธอทันที เธอกลับไปนั่งที่โต๊ะเพื่อลุ้นคะแนนที่เธฮจะได้
        j 'ฟู่ว ใจเต้นแรงไปหมดเลยค่ะ'
        r 'รีบๆดูเร็วๆๆๆ'
        j 'โอเค นับ 3...2'
        r 'ฮึ่ยยย'
        j '1....!!! ทำไมมัน!...ออกมาเป็นแบบนี้ล่ะคะ'
        r 'โอ้วตายแล้ว งานนี้แย่แน่ๆ'
        j 'มะ ไม่ขนาดหรอกค่ะ..'
        r 'ไม่ มันขนาดนั้นแหละ คิดดูสิมันจะเกิดอะไรขึ้นถ้าทุกคนรู้ว่าเธอได้เกรดเท่านี้'
        j 'เกรดมันก็แค่..ไม่ๆ ทุกคนไม่ใจร้ายขนาดนั้นหรอกค่ะ'
        r 'ทุกคนอย่างนั้นหรอ พอทุกคนรู้เกรดของเธอแล้วจะไม่มีอะไรเปลี่ยนแปลงเลยอย่างนั้นหรอ'
        menu :
            'อาจารย์'
                r 'รู้อะไรมั๊ย คนแรกที่รู้เกรดของเธอคืออาจารย์'
                j 'แน่นอนอยู่แล้วค่ะ เพราะเขาเป็นคนให้เกรดหนิคะ'
                r 'และเขาก็จะรู้ว่า เด็กสาวคนนี้มันไม่เอาไหน'
                j 'คนเป็นอาจารย์เขาจะคิดแบบนั้นได้ยังไงล่ะคะ'
                r 'เธออ่านใจเขาได้หรอ จะบอกอะไรให้นะ คนเป็นอาจารย์น่ะ เขาชอบและใส่ใจกับเด็กที่เรียนเก่งเกรดดี'
                r 'หลังจากนี้เธอคงได้รับสายตาดูแคลนการเขาแล้วล่ะ ระวังตอนเช็คชื่อให้ดีนะหรือเขาจะทำเป็นไม่เห็นชือเธอกันนะ'
                j 'ฉันเชื่อว่าอาจารย์ไม่ใจร้ายขนาดนั้นหรอกค่ะ เขาบทบาทที่จะทำให้พวกเราเป็นคนที่ดีขึ้น เราต้องให้ใจกับเขาด้วย'
                r 'ตามใจเธอก็แล้วกัน'
                $ score += 0
            'เพื่อน'
                r '"ไม่เห็นจะเรียนเก่งเท่าไหร่เลย" เดินๆอยู๋ประโยคนี้คงตามหลอกหลอนเธอไปสักพักเลยนะ'
                j 'นั่นมันใจร้ายเกินไปแล้ว ไม่ๆ ทุกคนต้องเข้าใจแน่นอนค่ะ'
                r 'นั่งกินข้าวคนเดียวก็คงจะเหงาแย่เลยนะ'
                r 'วันไหนลืมเอากระเป๋ามา ระวังไม่มีที่นั่งล่ะ'
                r 'ตอนขึ้นไปเรียนก็คงไม่มีที่นั่งดีๆสำหรับเธอแล้ว'
                j 'ไม่มีใครตัดสินคนจากความผิดพลาดเพียงครั้งเดียวหรอกค่ะ...'
                r 'และงานกลุ่มก็จะไม่มีใครเอาเธอมาอยู่ด้วย!!'
                r 'และไม่มีที่ไหนรับคนเกรดน้อยเข้าทำงานแน่นอนนนนนน'
                j 'ฮือ นี่มันทำฉันรู้สึกแย่จนปวดท้องไปหมดแล้ว'
                r 'สาวน้อยคนนี้จะเป็นที่จดจำในงานเลี้ยงรุ่น'
                $ score += 1
            'ครอบครัว'
                r '"พ่อคะแม่คะ วันนี้เกรดออกแล้ว แต่มันไม่ค่อยดีเลยค่ะ"'
                r '"ไม่เป็นไรหรอกลูก ครั้งหน้าเอาใหม่ได้นะ"'
                r 'ถ้าพ่อกับแม่ตอบเธอมาแบบนี้ ลองหยิกตัวเองดูนะ เผือเธอกำลังฝันอยู่'
                j 'ฉันไม่อยากใหพวกท่านเสียใจเลยค่ะ ฉันไม่อยากบอก แต่ยังไงพวกท่านก็ต้องรู้'
                r 'ไม่อยากบอกก็ไม่ต้องบอกสิ ไม่ใช้เรื่องที่้ต้องกังวลเลย'
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
                    'บอกครอบครัว'
                        j 'ขอแค่คุณพ่อกับคุณแม่เข้าใจฉันก็พอแล้วค่ะ บางทีเราไม่จำเป็นต้องใส่ใจว่าคนอื่นจะมองยังไง'
                        r 'ที่ฉันพูดไปเธอได้ฟังรึเปล่า รู้มั๊ยว่าเด็กเกือบ 90% ของทั้งโลกจะเป็นโรคซึมเศร้าเพราะป้าข้างบ้าน'
                        j 'ฉันจะเป็นอีก 10% ที่เหลือเองค่ะ'
                        r 'เธอท้าทายอำนาจมืดแล้วล่ะ'
                        j 'แต่จริงๆแล้วไม่ใช่ว่าคุณป้าทุกคนจะใจร้ายเสมอไปนะคะ'
                    $ score += 0
                    'ครอบครัวคงไม่เข้าใจ'
                        j 'พวกท่านต้องไม่เข้าใจแน่ค่ะ'
                        r 'เราแค่ป้องกันกรณีที่ร้ายแรงที่สุด คือพวกเขาจะห้ามไม่ให้เธอทำงานอดิเรกอีกเลย'
                        r 'ไม่มีนิยายให้เธออ่าน ทุกอย่างถูกกีดกัน เพื่อให้เธอมีเวลาโฟกัสกับเรื่องการเรียนให้มากที่สุด'
                        j 'นั่นมันแย่มาก ฉันจะไม่บอกพวกเขาเด็ดขาดเลย'
                    $ score += 1
            'คนที่แอบชอบ'
                j 'เขาเป็นคนดีนะคะ ฉันเคยเห็นเขาช่วยติวให้เพื่อนๆด้วย'
                r 'แสดงว่าเขาต้องเป็นคนที่เก่งมากๆ เธอหมดโอกาสแล้วล่ะ'
                    menu:
                        'พลิกวิกฤตให้เป็นโอกาส'
                            j 'ไม่หรอกค่ะ ไม่แน่ฉันอาจจะขอเข้าร่วมการติวในครั้งหน้าด้วย'
                            r 'เพ้อฝันจริงๆเลยยัยเด็กคนนี้'
                            score += 0
                        'ตัดใจ'
                            r 'ดูท่าทีเหงาหงอยนั่นสิ ไม่เป็นไรนะฉันจะอยู่กับเธอเอง'
                            score += 1
        if score > 1:
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
            '4.00'
                r 'เดี๋ยวก่อนนะ แล้วเวลาอีก 120 นาทีสำหรับการนอนอันมีค่าล่ะ'
                j 'บางทีฉันก็อยากเปลี่ยนไลฟ์สไตล์ชีวิตดูบ้าง'
                r 'ไหนบอกฉันหน่อยสิว่าเธอตั้งใจจะทำอะไร'
                menu 
                    'ออกกำลังกายตอนเช้า'
                        j 'เพื่อนๆฉันบอกว่า การออกกำลังนอกจากจะส่งผลดีต่ออสุขภาพ ยังทำให้สมองเราทำงานได้ดีขึ้นอีกด้วยนะคะ'
                        r 'อย่างนั้นหรอ เธอมั่นใจได้ยังไงว่าไม่ใช่แผนให้เธอไปหลับในห้องเรียนน่ะ'
                        J 'เพื่อนคนนี้เขาเรียนเก่งมากๆเลยนะคะ'
                        r 'แล้วเธอรู้ได้ยังไงว่าเพื่อนคนนั้นเรียนเก่งเพราะออกกำลังกาย'
                        j 'ฉันเห็นเขาลงรูปในโซเชียลค่ะ'
                        r 'อะไรนะ!!'
                        r 'ในตายเถอะสาวน้อย เธอกำลังบอกว่าเธอเชื่อสิ่งที่อยู่ในโซเชียลอย่างนั้นหรอ'
                        r 'เธอไม่เคยเห็นพวกคนที่แต่งชุดออกกำลังกายตามแฟชั่นบ้างหรอ แท้จริงแล้วหุ่นดีๆพวกนั้นก็มาจากยาลดความอ้วนทั้งนั้นแหละ'
                        r 'สาวน้อยอ่อนต่อโลกอย่างเธอตามเรื่องพวกนี้ไม่ทันหรอก อยากเรียนเก่งก็แค่อ่านหนังสือก็พอแล้ว เอา 120 นาทีที่เหลือไปนอนพักสมองดีกว่า'
                        j 'ออกให้ไม่เหนื่อยมากก็ได้หนิคะ'
                        r 'งั้นบอกว่าสิว่าเธอจะออกกำลังกายยังไง'
                        menu:
                            'วิ่ง'
                                r 'วิ่งงั้นหรอ!!!! เธอไม่กลัวสะดุดล้มรึไง สะดุดล้ม เข่าถลอก แผลติดเชื้อ บาดทะยัก ตัดขา!!!'
                                j 'ไม่ได้วิ่งเร็วขนาดนั้นนะคะ'
                                r 'การวิ่งของเธออาจจะไปยั่วโมโหหมาเจ้าถิ่นจนพวกมันพาพวกมาวิ่งไล่กวดเธอ!!!'
                                r 'หรือไม่เธออาจจะเจอเจ้าแมวน่ารักๆ ซึ่งนั่นดึงดูดให้เธฮเข้าไปเล่นด้วย แต่เจ้าแมวตัวนี้กลัวเธอและตวัดเล็บใส่'
                                r 'ที่น่ากลัวกว่านั้น ถ้าเธอโดนแมวกัดล่ะก็ รู้มั๊ยว่านั่นร้ายแรงกว่าโดนหมากัดอีกนะ เชื้อโรคในปากแมวมันน่ากลัวมาก เธอรู้บ้างรึเปล่า!!!'
                                j 'ฉะ ฉันไม่เล่นกับพวกน้องแมวก็ได้ค่ะ'
                                r 'เธออดใจไหวหรอ!! เจ้าสัตว์หน้าขนปุกปุย อุ้งเท้านุ่มนิ่ม เสียงร้องน่าเอ็นดู แต่ในร่างกายไหลเวียนด้วยเลือดนักสู้ไทยพวกนั้นน่ะ มีใครอดใจไม่สัมผัสได้บ้าง!!!'
                                j 'ฮืออออ ฉันจะไม่เข้าใกล้สัตว์น่ารักแล้ว'
                                r 'ยังไม่หยุดแค่นี้นะ ถ้าวิ่งๆอยู่ฝนเกิดตกขึ้นมาล่ะ และก็ตกหนักๆๆๆขึ้นเรื่อยๆ ทีนี้แหละเธอจะไม่มีทางเลือก นอกจากรีบวิ่งกลับบ้าน สุดท้ายก็มีโอกาสสะดุดล้มอยู่ดีแถมเปอร์เซ็นต์มากกว่าเดิมอีก!!'
                                r 'ฝนที่อยู่ๆก็ตกจะพาฝุ่นละอองที่อยู่บนฟ้ามากระทบตัวเธอซึ่งนั่นอันตรายมาก ถ้าเธออาบน้ำไม่ทันเธอมีโอกาสเสี่ยงเป็นหวัดสูงมากๆๆๆๆๆ'
                                r 'สุดท้ายนี้เธอก็ต้องหยุดเรียนเป็นสัปดาห์!!!'
                                j 'ฮืออ'
                                jump finish4
                            'เต้น'
                                j 'ฉันมีคลิปนึงที่อยากเต้นตามอยู่'
                                r 'ข้อมือเธอจะเหวี่ยงไปฟาดอะไรสักอย่างจนกระดูกหักได้นะ'
                                j 'ท่าเต้นไม่ค่อยมีเหวี่ยงแขนขนาดนั้นหรอกค่ะ'
                                r 'หรืออาจจะลื่นล้มหัวฟาดพื้น!!!'
                                r 'เสียงล้มของเธอจะทำให้พ่อแม่ตื่นและรีบวิ่งมาดู และพอรู้ว่าเกินอะไรขึ้น พวกเขาจะแบนการเต้น'
                                r '"มันเป็นอันตรายต่อลูก ต่อไปนี้เราจะยึดมือถือไม่ให้ลูกดูอะไรพวกนี้อีก และเราจะคอยจับตาดูลูกด้วย"'
                                r 'สุดท้ายนี้เธอจะเกลียดการเต้น และคิดว่าถ้าย้อนเวลากลับไปได้ ฉันจะไม่ทำแบบนั้น!!!'
                                jump finish4
                            'โยคะ'
                                j 'โยคะดูทำง่ายดีนะคะ ใช้พื้นที่ไม่เยอะด้วย'
                                r 'ฟังดูดีนะ ไหนฉันขอคำนวณความเสี่ยงให้เธอหน่อย'
                                r 'เธอเสี่ยงเป็นอัมพาตจากโยคะผิดท่า'
                                r 'โอ้ว ไหนจะตะคริวตัวร้าย'
                                r 'หรือเธออาจจะทำไม่ถูกวิธี ซึ่งนั่นทำให้การออกกำลังกายตอนเช้ามันสูญเปล่า'
                                r 'เธออาจจะตายได้เพราะไม่รู้วิธีจัดการตนเองเมื่อร่างกายเหนื่อยเกินไป'
                                r 'สุดท้ายนี้มันจะทำให้เธอไม่สามารถไปโรงเรียนได้ และผลการเรียนเธอก็ตกลงอีกครั้ง'
                                jump finish4

                    'กินข้าวเช้าที่โรงเรียน'
                        j 'ฉันรู้สึกว่านี่เป็นเรื่องที่บ้ามาก ข้าวที่บ้านไม่อร่อยหรอ'
                        r 'อร่อยที่สุดอยู่แล้วค่ะ'
                        j 'ทั้งอร่อยและไม่ต้องเสียเงิน แล้วเธอจะตื่นเช้าไปกินทำไมกัน'
                        r 'ฉันยังพอมีเงินเก็บอยู่นะคะ ลองสักครั้งคงไม่เป็นอะไร'
                        j 'ฉันไม่อยากจะพูดแบบนี้หรอกนะ แต่การใช้เวลาอยู่กับครอบครัวเป็นสิ่งที่เราไม่สามรถย้อนกลับมาเรียกคืนได้หรอกนะ'
                        j 'แม่ของเธอจะตรอมใจเพราะคิดว่าฝีมือทำอาหารของตัวเองแย่มากจนลูกสาวรีบตืนเช้าไปกินที่โรงเรียนแทน'
                        j 'แม่ของเธออาจจะแอบไปร้องไห้ซึ่งนั่นทำให้คุณพ่อทุกข์ใจที่ตนเองไม่สามารถทำอาหารได้อย่แล้ว'
                        j 'เกิดความร้าวฉานในครอบครัวเพราะ! เธอ! ไม่! ยอม! กิน! อาหาร! ฝี! มือ! แม่ !!!!!'
                        jump finish4

                    'แค่อยากตื่นเช้า'
                        r 'นั่นมันบ้ามาก เธอจะตื่นมารอสังเคราะห์แสงแรกของวันหรอ เสียเวลาชีวิตเกินไปแล้ว'
                        j 'บางทีฉันอาจจะลองทำข้าวเช้า'
                        r 'เมนูอะไร ทอด ต้ม นึ่งหรือย่างล่ะ'
                        menu:
                            'ขนมปังปิ้งกับไข่ดาว'
                                j 'แค่ขนมปังปิ้งกับไข่ดาวธรรมดาก็พอแล้วค่ะ'
                                r 'นี่มีปิ้งด้วยหรอ โอ้วให้ตายเถอะ ไข่ดาวนั่นเธอรู้รึเปล่ามีอัตราการบาดเจ็บจากการทำอาหารเป็นจำนวนเท่าไหร่ โดยเฉพาะเมนูที่ใช้น้ำมัน!!!'
                                r 'น้ำมันที่กระเด็นด้วยความร้อนสูงแบบนั้นสามารถละลายผิวหนังเธอจนเป็นแผลเป็นได้เลยนะ'
                                r 'ระหว่างนั้นมันจะเจ็บปวดแค่ไหน หรือบางทีอาจจะไม่ใช้น้ำมันที่กระเด็นมาโดนแต่มีอะไรบางอย่างไปเกี่ยวกระทะจนน้ำมันหกราดใส่ตัวเธอ น้ำมันร้อนๆ!! กับค่ารักษาที่ตามมา!!!'
                                r 'เอาเป็นว่าเราจะไม่พูดถึงเรื่องนี้อีก แบบนี้ปลอดภัยกับเธอแล้ว'
                                jump finish4
                                # show joseph sad face
                            'ไข่ต้มยามเช้า'
                                j 'ไข่ต้มก็ดีนะคะ ดีต่อสุขภาพด้วย'
                                r 'เธอกะเวลาต้มได้อย่างนั้นหรอ ถ้าโชคร้ายมากจับได้ไข่ที่ไม่ปกติขึ้นมา และโชคร้ายอีกที่เธอต้มมันนานเกินไปจนมันระเบิดออกมา!!'
                                r 'ให้ตายสิ ฉันจินตาการกลิ่นออกเลย นี่มันสมรภูมิชัดๆ'
                                j 'ไข่เน่ามาได้ยังไงคะนั่น'
                                r 'ใครจะรู้ หรือเธอสามารถมองทะลุผ่านเปลือกไข่ได้อย่างนั้นหรอ'
                                r 'เอ๊ะๆๆๆๆ หรือว่า'
                                r 'เธออาจจะต้มมันออกมาได้ดีมาก แต่มันรู้ตัวอีกทีตอนเธอปลอกมันแล้วมันระเบิดใส่หน้าเธอ!!!'
                                r 'โอ้วว ยกเลิกแผนนี้เถอะ มันเสี่ยงเกินไป
                                # show joseph sad face
                                jump finish4
                            'มาม่า'
                                j 'ฉันไม่ได้ใช้โควตาทานมาม่ามานานแล้ว บางทีทำมาม่าทรงเครื่องตอนเช้าก็ดีนะคะ'
                                r 'เอาล่ะ ฉันคงพูดได้ว่า ผู้คนมากมายป่วยเป็นโรคไตเพราะการทานมาม่า'
                                j 'นั่นเพราะพวกเขาทานแบบแห้งไม่ใช่หรอคะ ฉันตั้งใจจะต้มนะ'
                                r 'ใครบอกเธอแบบนั้นน่ะ'
                                j 'ผู้คนแชร์เรื่องนี้กันในโซเชียล'
                                r 'เธอ! หยุด! เชื่อ! ทุก! อย่าง! ใน! โซเชียลเดี๋ยวนี้!!!!!'
                                r 'ผู้คนเป็นโรคไตเพราะโซเดียมในมาม่า เธอบอกว่าเธอเอาไปต้มแล้วคิดว่าโซเดียมจะหายไปอย่างนั้นหรอ'
                                r 'ยังไงเธอก็ต้องใส่เครื่องปรุงและซดน้ำทุกหยดอยู่ดีนั่นแหละ'
                                r 'และโรคไตน่ะ มันทรมาณแค่ไหนรู้มั๊ย เธอจะอ่อนเพลียไม่มีแรง ปวดหลังปวดเอวหัว ปวดไปหมด!!! 
                                r 'และเธอจะต้องขาดเรียนไปรักษาตัวด้วย'
                                j 'แต่ฉันไม่ได้กินมันบ่อยๆนะคะ'
                                r 'เธออาจจะติดใจจนเป็นอันกินอะไรไม่ได้ถ้าไม่ใช่เมนูนี้ โอ้ พระเจ้า ฉันไม่อยากคิดถึงตอนที่เธอตัวบวมเพราะแค่มาม่ามื้อเช้านั่น'
                                r 'เอาล่ะสาวน้อยคิดถึงพ่อกับแม่ไว้สิ ตื่นเวลาเดิมและรอทานมื้อเช้าแสนอร่อยทรงคุณค่าของแม่ก็พอแล้ว ไม่เสียเวลานอน ไม่เสียสุขภาพ'
                                jump finish4
                '5.55'
                    j 'จะเป็นยังไงนะถ้าตื่นก่อนเวลาสัก ถ นาที'
                    r 'มีเวลาอีกแค่ 5 จะตื่นขึ้นมาทำไม!!! นอนต่อไปเถอะ!!!'
                    # show joseph sad face
                    jump finish4
                '6.00'
                    j 'ฉันว่าตื่นเวลาเดิมน่ะดีแล้ว'
                    jump finish4
    label finish4:
        r 'เอาล่ะ Good night little girl'
        j 'บางทีฉันอาจจะเปลี่ยนเป็นดึงหางเจ้ากระต่ายในฝันแทน'
        # fade scene
        # show the sun
        # show joseph wake up(บิดขี้เกียจด้วย)
        j 'เยี่ยมเลยค่ะ วันนี้รู้สึกเต็มอิ่มมากๆ'
        r 'ไม่นอนต่อหรอ นาฬิกายังไม่ปลุกเลยนะ'
        j 'ไม่แล้วค่ะ ตอนนี้กำลังดีมากเลย'
        j 'ว่าแต่ัวันนี้พระอาทิตย์วันนี้ขึ้นเร็วจังเลยนะคะ'
        # joshep take her phone to check time
        # the phone has not reponse
        j '(เดี๋ยวก่อนนะ แบบนี้มันแปลกๆแล้ว)'
        ..ก๊อก ก๊อก..
        # someone knock the door
        mom 'ลูกรัก อีก 15 นาทีจะ 7 โมงแล้วนะ ยังไม่ลงมาทานข้าวอีกหรอจ๊ะ'
        j 'อะไรนะคะ!!! อีก 15 นาทีจะ 7 โมง มะ มะ ม๊าย!!!!!!!'
        r 'ฮี่ฮี่ โทษทีนะ พึ่งนึกได้ว่าเมื่อคืนเธอลืมเสียบหัวชาร์จ'
#The End