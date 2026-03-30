image bg company = im.Scale("images/MyQuestion/bgs/bg_company.png", 1920, 1080)
image bg_office = im.Scale("images/MyQuestion/bgs/bg_office.png", 1920, 1080)
image bg_office_desk = im.Scale("images/MyQuestion/bgs/bg_office_desk.png", 1920, 1080)
image bg_office_path = im.Scale("images/MyQuestion/bgs/bg_office_path.png", 1920, 1080)
image bg_conference_room = im.Scale("images/MyQuestion/bgs/bg_conference_room.png", 1920, 1080)
image zoro_sanji_angry = im.Scale("images/MyQuestion/characters/zoro_sanji_angry.png", 1920, 1080)
image nami_sanji_zoro_knock_out = im.Scale("images/MyQuestion/characters/nami_sanji_zoro_knock_out.png", 1920, 1080)

define m    = Character("Matthäus")
define c    = Character("Chef")
define r    = Character("Ralph")
define mc   = Character("Dein Name")
define s    = Character("Sabrina")
define e    = Character("Erzähler")
define z    = Character("Zoro")
define sj   = Character("Sanji")
define n    = Character("Nami")

label start:

    e "Bevor wir uns in die Abgründe der Fokusteams stürzen...\n Wer bist du überhaupt?"
    
    $ player_name = renpy.input("Dein Name:")
    $ player_name = player_name.strip()

    if not player_name:
        $ player_name = "Agent X"

    $ mc = Character(player_name)

    e "Alles klar, [player_name]. Schnall dich an. \nEs ist ein Dienstagmorgen wie jeder andere, aber für dich wird er unvergesslich..."

    scene bg company
    with fade 
    scene bg company
    e "Ein strahlender Morgen bei Albis. Die Vögel singen von Reiners Schatz und Multithreading..."
    e "Doch im Schatten der Kaffeemaschine braut sich eine Katastrophe zusammen. Ein Mann. Ein Ziel. Ein unbändiger Hunger."

    scene bg_office
    show matthäus_normal

    m "Hörst du das, [mc]? Das ist das Flüstern des Schicksals...\nEs riecht verdächtig nach frisch gebackenem Himbeerkuchen und belegten Brötchen im Innovationsforum."

    show matthäus_happy

    mc "Matthäus, wenn wir da ohne Einladung aufkreuzen, dann verlieren wir unsere Jobs!"

    show matthäus_normal

    m "Unsere Jobs? Es ist wohl eher ein strategische Akquise von Backwaren. Wer nicht wagt, der hungert. Bist du bereit für den Überfall auf die Brötchen?"
    
    show matthäus_happy

    scene bg_office_path
    e "Mit einem großen Hunger schleichen sich beide ins Innovationsforum. Mit jedem weiterem Schritt wird der Hunger von Matthäus größer und größer."

    scene bg_conference_room
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

            show ralph_angry

            r "HALT! KEINE BEWEGUNG!"
            r "Matthäus?! Das ist ein Dienstjubiläum und keine Selbstbedienungstheke! Du hast die feierliche Stille mit deinem Hunger ruiniert!"

            show matthäus_normal
            m "Ralf, ich kann das erklären... es ist für das Gemeinwohl!"

            hide matthäus_normal
            show ralph_angry

            r "RAUS HIER! Bevor der Chef dich bemerkt und uns alle bloßgestellt!"

            hide ralph_angry
            show matthäus_normal

            m "[mc], SCHNELL! Rette die Beute! Stopf dir die Taschen voll! Das hier ist jetzt eine Rettungsmission für die gesamte Albis-Belegschaft!"

            hide matthäus_normal

            hide chef_normal
            scene bg_office_path with fade

            e "Matthäus und [mc] rennen, als ginge es um unser Leben. Der Geschmack von Sieg und belgeten Brötchen liegt auf deren Zunge."

            scene bg_office with fade
            show matthäus_happy

            m "Puh... das war knapp. Aber hast du gesehen, wie Ralf geguckt hat? Als wäre ich ins Louvre Museum eingebrochen."

            mc "Wir sind offiziell auf der schwarzen Liste, Matthäus."

            mc "Glaubst du der Chef hat uns bemerkt?"

            show bg_conference_room with fade
            hide matthäus_happy

            show chef_normal
            c "Albis...Warum ist es immer Albis?"
            hide chef_normal

            show zoro_happy at  left with moveinleft

            z "Wo bin ich? "

            z "Wo ist Kaido? "

            #hide zoro_happy

            show sanji_happy at right with moveinright

            sj "Du Spinatschädel hast dich schon wieder verlaufen! Man kann dich nicht alleine lassen."

            show zoro_happy at left with moveinleft
            show sanji_happy at right with moveinright

            z "Ich will zur See, ein wenig Fischen."
            
            sj "Nein, kannst du nicht, Grünkopf!"

            z "Warum kann ich nicht? Warum sollte ich dir überhaupt zuhören?"

            sj "Glaubst du, ich renne hier mit dir herum, weil ich das möchte?"
            sj "Du machst nur noch mehr Ärger, wenn du übers Campus spazierst. Du streunender Mooskopf!"
            sj "Die anderen kommen bald, also geh einfach mit zum Schiff."

            z "Wie kann die Nummer Sieben nur so mit der Nummer Eins reden?"

            sj "Warum ordnest du uns in der Reihenfolge, in der wir angekommen sind? Du bist hier nur aus Zufall als Erster angekommen! Lass dir das nicht zu Kopf steigen!"

            z "Okay, tut mir leid..."
            z "Nummer Sieben."

            hide zorro_happy
            hide sanji_happy

            show zoro_sanji_angry

            sj "Okay, ich mach dich fertig!"
            sj "Ich habe meine Beine zwei Jahre lang wie verrückt traniert!"

            z "Dann zeigs mir! Ich zerteile dich in zwei Teile!"

            menu:
                "Willst du dazwischen gehen?"

                "Nein, interessiert mich nicht. Ich habe meine Brötchen.":
                    hide zoro_sanji_angry

                    show bg_office_desk with fade 
                    e "Du entscheidest dich für die Sicherheit deines Schreibtisches und somit endet leider dein Abenteuer mit Matthäus..."
                    return
    
                "Ja, die sollten sich nicht streiten.":

                    hide zoro_sanji_angry
                    hide zoro_happy
        
                    show nami_happy

                    n "Da lass ich euch einmal aus dem Auge!"

                    hide nami_happy

                    show nami_sanji_zoro_knock_out

                    n "Ihr kommt jetzt mit!"

                    mc "Nami greift den beiden am Kragen und zieht sie hinterher."

                    hide nami_sanji_zoro_knock_out with fade 
                    
                    mc "Schauen wir mal kurz rüber zu Matthäus."

            show bg_office_desk with fade
            show matthäus_happy

            m "Egal. Felix! Komm schnell her, du glaubst nicht, welche Opfer wir für diesen Snack bringen mussten..."

            return