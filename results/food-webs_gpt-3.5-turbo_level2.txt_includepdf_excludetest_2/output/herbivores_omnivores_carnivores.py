from formatList import formatList

def find_herbivores(relationships):
    producers = set(relationships.keys()) - set(sum(relationships.values(), []))
    herbivores = [predator for predator in relationships.keys() if predator in producers]
    print("Herbivores:", formatList(herbivores) if herbivores else "(None)")

def find_omnivores(relationships):
    omnivores = [predator for predator, prey in relationships.items() if predator in set(sum(relationships.values(), [])) and predator not in set(relationships.keys())]
    print("Omnivores:", formatList(omnivores) if omnivores else "(None)")

def find_carnivores(relationships):
    predators = set(relationships.keys())
    eaten = set()
    for prey in relationships.values():
        eaten.update(prey)
    carnivores = predators - eaten
    print("Carnivores:", formatList(sorted(carnivores)))

def main():
    relationships = read_file(sys.argv[1])
    find_herbivores(relationships)
    find_omnivores(relationships)
    find_carnivores(relationships)

if __name__ == "__main__":
    main()