import scenes

import linecache
import time
from os import system


def Engine(curr_scene, Curr_oppliv, curr_points):
    scene_index = scenes.scene_list.index(curr_scene)

    #Runs Scenes
    while True:
        
        scene = scenes.scene_dict[scene_index]

        system('cls')
        print(f"Scene: {scenes.scene_list[scene_index]} | Sprøyter: {Curr_oppliv} | Poeng: {curr_points}")

        dpoints = 0
        bestått, dpoints = scene.enter()

        curr_points += dpoints

        Save(scenes.scene_list[scene_index], Curr_oppliv, curr_points)

        if bestått is True:
            scene_index += 1
        elif bestått is False:
            print("Du faila hardt, og p.g.a din usikkerhet på deg selv dør du.")

            if Curr_oppliv > 0:
                print("Din usynlige hjelper er dessverre ikke tom for\ngjenopplivningssprøyter",
                      "så den vekker deg til live og\ndu får prøve på nytt :(")
                Curr_oppliv -= 1
            else:
                print("Din usynlige hjelper har heldigvis ikke flere\ngjennopplivningssprøyter, ",
                      "så du fortsetter å være død.\nGratulerer!")
                break
        else:
            break
        input("\n\nTrykk enter for å fortsette...")

def Delete():
    # Resetter de lagrede dataene

    with open("Status.txt", "w") as File:
        File.seek(0)
        File.truncate()

def Save(scene, sprøyter, points):
    with open("Status.txt", "w") as File:
        File.write(scene + "\n")
        File.write(str(sprøyter) + "\n")
        File.write(str(points))

def Reset():
    curr_scene = "Villa"
    Curr_oppliv = 4
    curr_points = 0

    return curr_scene, Curr_oppliv, curr_points

def PrAll():
    print("Scene: ", curr_scene)
    print("Sprøyter: ", Curr_oppliv)
    print("Poeng: ", curr_points)

print("Velkommen til spillet \"En helt vanlig skolevei\"!")

curr_scene = linecache.getline("Status.txt", 1)
Curr_oppliv = linecache.getline("Status.txt", 2)
curr_points = linecache.getline("Status.txt", 3)

curr_scene = curr_scene.strip("\n")
Curr_oppliv = Curr_oppliv.strip("\n")

if not curr_scene or not Curr_oppliv or not curr_points or curr_scene == "Ferdig":
    print("Ingen eller ufullstendige lagringsdata funnet, du Starter på nytt.")

    Delete()
    curr_scene, Curr_oppliv, curr_points = Reset()


else:
    print("Lagringsdata funnet. Vil du fortsette eller starte på nytt?")
    print("Hvis du velger å starte på nytt, vil lagringsdataene bli slettet ",
          "og din nye framgang lagret.")
    svar = input(">")

    if "fort" in svar:
        print("Du valgte å fortsette.\nIgangsetter spillet...")
        Curr_oppliv = int(Curr_oppliv)
        curr_points = int(curr_points)
    else:
        print("Du valgte å starte på nytt.\nIgangsetter spillet...")
        Delete()
        curr_scene, Curr_oppliv, curr_points = Reset()


time.sleep(2)
Engine(curr_scene, Curr_oppliv, curr_points)
