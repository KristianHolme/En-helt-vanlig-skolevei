import scenes

import linecache
import time


def Engine(curr_scene, Curr_oppliv):
    scene_index = scenes.scene_list.index(curr_scene)

    #Runs Scenes
    while True:
        time.sleep(1)
        scene = scenes.scene_dict[scene_index]
        bestått = scene.enter()

        Save(scenes.scene_list[scene_index], Curr_oppliv)

        if bestått is True:
            scene_index += 1
        elif bestått is False:
            print("Du failer hardt, og p.g.a din usikkerhet på deg selv dør du.")

            if Curr_oppliv > 0:
                print("Din usynlige hjelper er dessverre ikke tom for gjenopplivningssprøyter", 
                        " så den vekker deg til live og du får prøve på nytt :(")
                Curr_oppliv -= 1
            else:
                print("Din usynlige hjelper har heldigvis ikke flere gjennopplivningssprøyter, ", 
                        "så du fortsetter å være død, Gratulerer!")
        else:
            break


def Reset():
    # Resetter de lagrede dataene

    with open("Status.txt", "w") as File:
        File.seek(0)
        File.truncate()
    
def Save(scene, sprøyter):
    with open("Status.txt", "w") as File:
        File.write(scene + "\n")
        File.write(str(sprøyter))


print("Velkommen til dette spillet!")

curr_scene = linecache.getline("Status.txt", 1)
Curr_oppliv = linecache.getline("Status.txt", 2)

curr_scene = curr_scene.strip("\n")

if not curr_scene or not Curr_oppliv or curr_scene == "Ferdig":
    print("Ingen eller ufullstendige lagringsdata funnet, du Starter på nytt.")

    Reset()
    curr_scene = "DørTerskel"
    Curr_oppliv = 2

else:
    print("Lagringsdata funnet. Vil du fortsette eller starte på nytt?")
    print("Hvis du velger å starte på nytt, vil lagringsdataene bli slettet og din nye framgang lagret.")
    svar = input(">")

    if "fort" in svar:
        print("Du valgte å fortsette.\nIgangsetter spillet...")
        Curr_oppliv = int(Curr_oppliv)
    else:
        print("Du valgte å starte på nytt.\nIgangsetter spillet...")
        Reset()
        curr_scene = "DørTerskel"
        Curr_oppliv = 2

time.sleep(2)
Engine(curr_scene, Curr_oppliv)