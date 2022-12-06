class FishModel:
    def __init__(self, init):
        self.day = 0
        self.fishes = init
    
    def progress_day(self):
        self.day += 1
        print(f"DAY {self.day}: pop={len(self.fishes)}")
        aged_population = []
        new_fish_count = 0
        for fish in self.fishes:
            if fish == 0: 
                aged_population.append(6)
                new_fish_count += 1
            else: aged_population.append(fish-1)
        self.fishes = aged_population + ([8]*new_fish_count)
    
    def get_population(self):
        return len(self.fishes)


if __name__ == '__main__':
    ## INPUT STUFF
    f = open(__file__.replace(".py", ".txt"), "r")
    text = f.read()
    lines = list(map(int,text.split(",")))


    fm = FishModel(lines)
    for _ in range(256):
        fm.progress_day()
    print(fm.get_population())

    