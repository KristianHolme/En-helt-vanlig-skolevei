from random import randint
from textwrap import dedent
import time

class Scene(object):
    def __init__(self):
        self.dpoints = 0

    def enter(self):
        print("Scene ikke konfigurert.")

        return True, self.dpoints
class Villa(Scene):
    
    def enter(self):
        print(dedent("""
                    Det er en helt vanlig dag, og du forbereder deg på å dra til skolen
                    fra en av Fjellhamars nordligste villaer. Idet du går over dørterskelen
                    ser du to romvesener stå ved siden av huset. Når de ser deg prøver de å 
                    kommunisere med deg, men du forstår ingenting. Hva gjør du for å forstå dem?
                    """))

        Forstå = input("Skriv \"hint\" hvis du trenger et hint.\n>")

        if "hint" in Forstå:
            print("\n- 20 poeng for udugelighet.\nHint: Hvordan går du vanligvis frem for å forstå et fremmed språk?")
            Forstå = input(">")
            self.dpoints -= 20
        else:
            pass
        if "ordbok" in Forstå:
            print("Ordbok er gammeldags, men det funker.\n+ 50 Poeng.")
            self.dpoints += 50
        elif "google" in Forstå or "oversetter" in Forstå or "translate" in Forstå:
            print("Google oversetter er moderne og effektivt!\n+ 100 poeng!")
            self.dpoints += 100
        elif "babelfish" in Forstå:
            print("En babelfish er det perfekte oversettelsesverktøy!\n+ 1000 poeng!")
            self.dpoints += 1000
        else:
            print("Du er ikke den smarteste kniven i skuffen, eller hva?\n- 100 poeng for udugelighet.")
            self.dpoints -= 100
            return False, self.dpoints
        
        time.sleep(1.5)

        print(dedent("""
                        Etter en lang samtale om livet, universet og allting,
                        finner du ut at romvesenene har kommet til jorda for å grenseløst
                        irritere et menneske i 24 timer. Problemet er at de ikke vet hvem de
                        skal irritere, så de spør deg om du har noen forslag.
                        Hvem skal bli grenseløst irritert de neste 24 timene?                     
                     """))

        offer = input(">")

        if "Kim Jong Un" in offer:
            print("Ajajaj, kanskje ikke så veldig lurt at\n",
                  "en diktator med kjernevåpen blir grenesløst irritert.\n- 40 poeng.")
            self.dpoints -= 40

        elif "Donald Trump" in offer:
            print("Ajajaj, kanskje ikke så lurt at en galning med kjernevåpen\n",
            "blir grenseløst irritert.\n- 40 poeng.")
            self.dpoints -= 40

        elif "Ramsey" in offer:
            print("Ajajaj, dette har ingen effekt på Herr Ramsey,\n", 
                  "han er konstant grenseløst irritert.")

        elif "Kim Kardashian" in offer:
            print("Ojojoj, dette kan bli veldig spennende!\n+ 100 poeng!")
            self.dpoints += 100
        elif "Gunilla" in offer:
            print("OJOJOJ! Nu blir det fart på sakan!\n+ 1000 poeng")
            self.dpoints += 1000
        else:
            print("Jaja, blir sikkert morsomt.\n +20 poeng")
            self.dpoints += 20
        
        time.sleep(1.5)
        
        print(dedent("""
                    Etter ditt møte med romvesenene, drar de av gårde
                    for å irritere grenseløst, og du setter deg på sykkelen og 
                    tar fatt på skoleveien.
                     """))
        

        return True, self.dpoints

class SykkelTur(Scene):
    
    def enter(self):
        print(dedent("""
                        Etter i overkant av fem sekunder på sykkelsetet oppdager
                        du at sykkelstien til skjetten er stengt på grunn av et
                        feilparkert romskip. Derfor må du sykle via strømmen stasjon.
                        Når du kommer til strømmen stasjon ser du at et av NSB's
                        flyvetog har noen tekniske feil. Lokomotivkapteinen har mistet
                        kontrollen, og flyvetoget krasjer og ødelegger nesten alle veier
                        til lillestrøm. Du er nødt til å ta veien om Kasjotten.\n\n
                     """))
        time.sleep(3)
        print(dedent("""
                        På veien opp til kasjotten møter du en gal vitenskapsmann i
                        hvit frakk og med blått piggete hår. Han sier "Watch where you're
                        biking you stupid bitch!" og du svarer med et forsøk på å fornærme
                        intelligensen hans.\n\n
                     """))

        rick_fight = Fight("Spiller", "Den gale vitenskapsmannen")

        resultat = rick_fight.fight()


        return resultat, self.dpoints
class Kasjotten(Scene):
    
    def enter(self):
        print(dedent("""
                        Du sykler videre mot kasjotten og blir vitne til et
                        stort fangeopprør. Du oppdager tilfeldigvis også at 
                        alt er i svart-hvitt, og du bruker kraften av sunn fornuft 
                        til å resonnere deg fram til at den gale vitenskapsmannen
                        må ha hatt en tidsportalpistol og sendt deg deg tilbake i tid.

                        Fangene slår ned veggene i kasjotten og kommer stormende mot deg.
                        Du tenker at dette var et svært ubelelig tidspunkt å dø på, men
                        hvorfor utsette det uungåelige?

                        Fangene stopper opp rett foran deg og spør om veien til nærmeste 
                        porselensbutikk. Hva gjør du?
                     """))
        
        pors = input(">").lower()

        if "politiet" in pors:
            print("Fangene tror du er i politiet, og fornærmer intelligensen din.")
            return False , self.dpoints

        politikamp = Fight("spiller", "Politiet")
        resultat = politikamp.fight()
        # True: win, False: loss
        return resultat, self.dpoints
   
class Sagelva(Scene):
    
    def enter(self):
        print("Dette er Sagelva")

        return True, self.dpoints
class NitElvBrua(Scene):
    
    def enter(self):
        print("Dette er NitElvBrua")

        return True, self.dpoints

class Ferdig(Scene):
    
    def enter(self):
        print("Spillet er ferdig.\nSe over for poeng.")
        return "æ", 0

class entity(object):
    def __init__(self, name, weapon = None):
        self.name = name
        self.weapon = weapon

        
class Fight(object):
    
    def __init__(self, hero, enemy):
        self.hero = entity(hero)
        self.enemy = entity(enemy)

    def fight(self):
        print(f"Slåsskamp mellom deg og {self.enemy.name}!")

        weapons = {11:"skje", 10:"Lyssabel", 9:"Railgun", 
        8:"Super-Ultra-Mega-Blaster", 7:"Blaster",
        6: "AK-47", 5:"Revolver", 4: "Dolk", 3: "kjøkkenkniv",
        2:"sprettert", 1:"pinne"}

        print("Du drar frem et våpen fra baklomma di.")
        w1index = randint(1, 11)
        w2index = randint(1, 11)

        self.hero.weapon = weapons.get(w1index)
        self.enemy.weapon = weapons.get(w2index)

        print(f"Du har en {self.hero.weapon}, din motstander har en {self.enemy.weapon}!")
        if w1index - w2index <= 2 and w1index - w2index >= -2:
            print("Dere har ganske like våpen, hva gjør du?")
            print("Alternativer: \"skyt\", \"dukk\", \"be til det almektige",
                  "flyvende spaghettimonsteret\".\nHva gjør du?")
            action = input(">>>")

            if "skyt" in action:
                print("Du bommer og du blir skutt av motstanderen. Du taper.")
                return False
            elif "dukk" in action:
                print("Du dukker, men blir allikevel skutt. Du taper.")
                return False
            elif "be" in action:
                print("Bra valg! Gjennom en serie med svært usansynlige ",
                      "hendelser har du vunnet!")
                return True
        elif w1index > w2index:
            print("Du har et suverent overlegent våpen! Du vinner!")
            return True
        elif w2index > w1index:
            print("Du har et suverent underlegent våpen. Du taper.")
            return False





scene_list = ["Villa", "SykkelTur", "Kasjotten", "Sagelva", "NitElvBrua", "Ferdig"]

scene_dict = {0 : Villa(), 1 : SykkelTur(), 2 : Kasjotten(), 3 : Sagelva(), 4 : NitElvBrua(), 5 : Ferdig()}
