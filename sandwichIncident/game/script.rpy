image bg company = im.Scale("images/MyQuestion/bgs/bg_company.png", 1920, 1080)
image bg_office = im.Scale("images/MyQuestion/bgs/bg_office.png", 1920, 1080)
image bg_office_desk = im.Scale("images/MyQuestion/bgs/bg_office_desk.png", 1920, 1080)
image bg_office_path = im.Scale("images/MyQuestion/bgs/bg_office_path.png", 1920, 1080)
image bg_conference_room = im.Scale("images/MyQuestion/bgs/bg_conference_room.png", 1920, 1080)
image bg_smoking_area_with_hand = im.Scale("images/MyQuestion/bgs/bg_smoking_area_with_hand.png", 1920, 1080)
image bg_smoking_area_without_hand = im.Scale("images/MyQuestion/bgs/bg_smoking_area_without_hand.png", 1920, 1080)
image bg_cafeteria = im.Scale("images/MyQuestion/bgs/bg_cafeteria.png", 1920, 1080)


define m    = Character("Matthäus")
define c    = Character("Chef")
define r    = Character("Raphael")
define mc   = Character("Dein Name")
define s    = Character("Sabrina")
define e    = Character("Erzähler")
define z    = Character("Zoro")
define sj   = Character("Sanji")
define n    = Character("Nami")
define jw   = Character("Joshua")
define jte  = Character("JTE")

label start:

    e "Bevor wir uns in die Abgründe der Fokusteams stürzen...\n Wer bist du überhaupt?"
    
    $ player_name = renpy.input("Dein Name:")
    $ player_name = player_name.strip()

    if not player_name:
        $ player_name = "Agent X"

    $ mc = Character(player_name)

    e "Alles klar, [player_name]. Schnall dich an. \nEs ist ein Dienstagmorgen wie jeder andere, aber für dich wird er unvergesslich..."

    play music "singing_birds.wav"

    scene bg company
    with fade 
    scene bg company
    e "Ein strahlender Morgen bei Albis. Die Vögel singen von Reiners Schatz und Multithreading..."
    e "Doch im Schatten der Kaffeemaschine braut sich eine Katastrophe zusammen. Ein Mann. Ein Ziel. Ein unbändiger Hunger."

    stop music fadeout 1.0

    play music "background.wav"
    scene bg_office
    show matthäus_normal

    m "Hörst du das, [mc]? Das ist das Flüstern des Schicksals...\nEs riecht verdächtig nach frisch gebackenem Himbeerkuchen und belegten Brötchen im Innovationsforum."

    show matthäus_happy

    mc "Matthäus, wenn wir da ohne Einladung aufkreuzen, dann verlieren wir unsere Jobs!"

    show matthäus_normal

    m "Unsere Jobs? Es ist wohl eher ein strategische Akquise von Backwaren. Wer nicht wagt, der hungert. Bist du bereit für den Überfall auf die Brötchen?"
    
    show matthäus_happy

    stop music fadeout 1.0

    play music "running.wav" volume 1.0
    scene bg_office_path
    e "Mit einem großen Hunger rennen beide ins Innovationsforum. Mit jedem weiterem Schritt wird der Hunger von Matthäus größer und größer."
    
    stop music fadeout 1.0

    scene bg_conference_room
    play music "crowded_room.wav" volume 0.30
    show matthäus_happy

    m "Da ist es. Das gelobte Land von Backwaren. Sieh dir diese Brötchen an...\nSie glänzen im Licht der Deckenstrahler wie Diamanten."

    menu:
        "Willst du wirklich zu einem Brötchen-Banditen werden?"

        "Nein, ich will nicht!":
            show bg_office_desk with fade 
            e "Du entscheidest dich für die Sicherheit deines Schreibtisches und somit endet leider dein Abenteuer mit Matthäus..."
            return

        "Ja, ich will zu einem Brötchen-Banditen werden":
            m "(flüstert Sabrina zu)\nWie ist die Lage an der Front? Wurden die Brötchen bereits gesichtet?"

            hide matthäus_happy
            show sabine_normal

            s "Die Zielobjekte sind noch unbewacht. Aber beeilt euch, der Chef poliert schon sein Mikrofon für die große Rede. Wenn er loslegt, gibt es kein Entkommen mehr."

            hide sabine_normal
            show matthäus_happy

            m "Ein kalkulierbares Risiko. [mc], deck mir den Rücken, ich gehe rein!"

            hide matthäus_happy
            show sabine_normal

            s "Nur zu. Im schlimmsten Fall leugne ich, euch jemals gesehen zu haben."

            hide sabine_normal
           
            with fade

            show raphael_angry

            r "HALT! KEINE BEWEGUNG!"
            r "Matthäus?! Das ist ein Dienstjubiläum und keine Selbstbedienungstheke! Du hast die feierliche Stille mit deinem Hunger ruiniert!"

            show matthäus_normal
            m "Raphael, ich kann das erklären... es ist für das Gemeinwohl!"

            hide matthäus_normal
            show raphael_angry

            r "RAUS HIER! Bevor der Chef dich bemerkt und uns alle bloßgestellt!"

            hide ralphael_angry
            show matthäus_normal

            m "[mc], SCHNELL! Rette die Beute! Stopf dir die Taschen voll! Das hier ist jetzt eine Rettungsmission für die gesamte Albis-Belegschaft!"

            hide matthäus_normal

            hide chef_normal
            stop music fadeout 0.50
            scene bg_office_path with fade

            e "Matthäus und [mc] rennen, als ginge es um unser Leben. Der Geschmack von Sieg und belgeten Brötchen liegt auf deren Zunge."

            scene bg_office with fade
            show matthäus_happy

            m "Puh... das war knapp. Aber hast du gesehen, wie Rapahel geguckt hat? Als wäre ich ins Louvre Museum eingebrochen."

            mc "Wir sind offiziell auf der schwarzen Liste, Matthäus."

            mc "Glaubst du der Chef hat uns bemerkt?"

            show bg_conference_room with fade
            hide matthäus_happy

            show chef_normal
            c "Albis...Warum ist es immer Albis?"
            hide chef_normal

            hide bg_conference_room

            show bg_office with fade
            show matthäus_happy

            m "Egal. JTE! Komm schnell her, du glaubst nicht, welche Opfer wir für diesen Snack bringen mussten..."

            hide matthäus_happy
            show jte_happy 

            jte "(stürmt rein wie ein FBI-Agent) MATTHÄUS! Vergiss die Brötchen, wir haben ein ethisches Dilemma."

            jte "Also... rein hypothetisch..."

            jte "Würdest du jemanden daten, der Herpes hat? Aber so richtig fies?"

            hide jte_happy
            show matthäus_normal

            m "(starrt ihn fassungslos an) JTE... ich habe gerade mein Leben für ein Brötchen riskiert und das ist deine erste Frage?"
            m "Eher nicht so, nein."

            hide matthäus_normal
            show jte_happy

            jte "Auch wenn die Wahrscheinlichkeit einer Übertragung bei unter 3 Prozent liegt?"

            hide jte_happy
            show matthäus_normal

            m "Nein, JTE. Ich würde niemanden daten, der Herpes hat."

            hide matthäus_normal
            show joshua_normal

            jw "(schaut aus der Ferne, als würde er versuchen, C++ im Kopf zu kompilieren)"

            jw "Salamander Aluminium..."

            jw "Kann mir mal jemand erklären, warum wir hier über Herpes diskutieren, während mein Magen nach weißem Monster und Zigaretten knurrt?"

            hide joshua_normal
            show jte_happy

            jte "Die Sache ist... Sie ist eine absolute 10 von 10! Ein echte Baddie! Ich wollte mit ihr eigentlich nur ein bisschen Pair-Programming betreiben..."

            hide jte_happy
            show joshua_normal

            jw " Pair-Programming... ist das jetzt der neue Code für 'Date'?"

            hide joshua_normal
            show jte_happy

            jte "Eh, ja genau ein Date..."

            jte "Anyways. Es ist 11:30 Uhr, Zeit für die heilige Pilgerfahrt zum Bistro. Ich brauche eine Nussecke und genug Proteine."

            hide jte_happy
            show joshua_normal

            jw "Guter Plan, aber davor brauchen wir eine strategische Nikotinpause."

            menu:
                "Willst du mit JTE und Joshua eine durchziehen?"

                "Ja, mein Gehirn braucht den Neustart...": 
                    
                    hide joshua_normal
                    scene bg_smoking_area_with_hand

                    mc "Du ziehst an der Kippe und spürst, wie der Stress des Brötchen-Raubs langsam verfliegt..."

                    show bg_smoking_area_without_hand with fade
                    show joshua_happy at right
                    show jte_happy at left

                    jte "Leute, Planänderung für das Wochenende. Wir organisieren einen Rave mit 180 BPM und ohne Genehmigung."

                    mc "Klingt wild, aber wer zahlt das Equipment? Wir haben nicht mal Budget für neue Ladekabel."

                    jte "Kein Stress! Ich hab da diesen Typen bei AliExpress... mein AliExpress-Chinese des Vertrauens. Der schickt mir 10.000 Watt LEDs für den Preis von einer Kiste Spezi. Super Angebote!"
                    
                    jte "(zeigt stolz verschwommene Screenshots von blinkenden Lichtern auf seinem Handy)"

                    jw "Mein Lieferant aus Shenzhen schreibt mir mittlerweile 'Guten Morgen'. Ich glaube, ich bin sein bester Kunde."

                    jw "Aber jetzt mal im Ernst...Mein Monster wartet auf mich."

                    jw "Ich brauche endlich mein flüssiges Gold. Meinen Monster Energy."

                    hide joshua_happy 
                    hide jte_happy 
                    scene bg_office_path with fade

                    e "Joshua, JTE und [mc] machen sich auf den Weg ins Bistro, bereit, um den ganzen Vorrat enhalieren."

                    scene bg_cafeteria

                    show jte_normal
                    jte "Diggah, guck dir diesen Glanz an... heute gibt es wieder Currywurst und Pommes."

                    hide jte_normal

                    show joshua_normal
                    jw "Ich sicher uns einen Tisch und hole mir noch mein Monster."
                    hide joshua_normal

                    e "Joshua und JTE stürzen sich auf ihr Essen, als hätten sie seit dem letzten Firmenjubiläum nichts mehr bekommen."

                    show joshua_normal
                    jw "(mit vollem Mund) Habt ihr eigentlich die E-Mail gelesen?"

                    mc "Welche Email? Mein Postfach quillt nur über vor Jira-Tickets."

                    jw "Heute Abend. Gourmet Tempel. Das Team. All-you-can-eat. Wir werden diesen Laden ruinieren."

                    hide joshua_normal

                "Nein, ich bleib sauber!": # Antwort 2
                    m "Wir gehen dann schon mal vor."

                    scene bg_cafeteria with fade

                    mc "Mal sehen... Was serviert die Sterneküche heute?"
                    mc "Oh, die klassische Currywurst-Pommes-Schranke. Ein Klassiker."
                    mc "Matthäus, beeil dich, die Schlange wird länger als die Warteschleife beim IT-Support!"

                    e "Matthäus und [mc] sichern sich ihre Rationen und genießen den Sieg über den Hunger an einem Tisch."

            e "20 Minuten später. Die Bäuche sind voll, die Welt ist wieder in Ordnung. Von Liebeskummer bis hin zur legendären Berlin-Fahrt wird über jedes Thema gesprochen."

            scene bg_office_path with fade
            e "Die Mittagspause neigt sich dem Ende zu. Die Gruppe schlendert träge zurück in Richtung Büro... zumindest theoretisch."

            show joshua_happy

            jw "JTE... [mc]... meine Freunde..."

            e "Joshua hebt seine Hand, in der wie durch Zauberei schon wieder eine Zigarette klemmt."

            jw "Die erste war nur zum Aufwärmen. Noch eine?"

            hide joshua_happy    
            menu:
                "Bist du bereit für Runde zwei in der Räucherkammer?"

                "Ich liebe den Geruch von Tabak am Mittag...": 

                    scene bg_smoking_area_with_hand with fade
                   
                    e "Ihr genießt die Ruhe vor dem nächsten Meeting-Sturm, bis plötzlich etwas die Idylle stört."

                    scene bg_smoking_area_without_hand with fade

                    show jte_normal at right

                    jte "(starrt konzentriert ins Gebüsch) Diggah... siehst du das? Unsere 5 Gramm Gratis-Proteine sind gelandet."

                    menu:
                        "Willst du wirklich wissen, was JTE mit 'Proteinen' meint?"

                        "Interessiert mich nicht, ich will nur rauchen.":    

                            show joshua_normal at left #with fade
                            e "[mc] entscheidet sich für die Ignoranz. Manche Dinge will man einfach nicht wissen, während man raucht."

                            #show joshua_normal
                            mc "Wir müssen noch die Wasserkisten schleppen. Freust du dich schon auf das Workout?"

                            jw "Können das nicht die anderes es nicht machen? Die haben doch noch Träume und Energie."

                            mc "Vergiss es. Die verstecken sich im Home-Office."
                            return    

                        "Ich muss es wissen.":
                            show jte_happy
                            mc "JTE, was zur Hölle meinst du mit 5 Gramm Proteinen? Wir kommen gerade vom Essen!"

                            mc "Sag mir bitte nicht, dass das was mit dem Tier da vorne zu tun hat..."

                            e "JTE deutet mit einem undefinierbaren Funkeln in den Augen auf den Hund, der gerade freudig über den Rasen rennt."

                            mc "JTE, nein! Erstens ist das illegal und zweitens hast du nicht mal eine Küche!"

                            hide jte_happy
                "Ich will nicht rauchen.":

                            return