import scenes

import linecache

class Fight(object):
    
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def fight():
        pass


def Engine(curr_scene, Curr_oppliv):
    scene_index = scenes.scene_list.index(curr_scene)
    print(">>> scene index: ", scene_index)

def Reset():
    # Resetter de lagrede dataene

    with open("Status.txt", "w") as File:
        File.seek(0)
        File.truncate()
    


print("Velkommen til dette spillet!")

curr_scene = linecache.getline("Status.txt", 1)
Curr_oppliv = linecache.getline("Status.txt", 2)



if not curr_scene or not Curr_oppliv:
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

Engine(curr_scene, Curr_oppliv)
