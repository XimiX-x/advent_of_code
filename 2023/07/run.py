class Card :
    def __init__(self, value) :
        match value :
            case "2" :
                self.value = 0
            case "3" :
                self.value = 1
            case "4" :
                self.value = 2
            case "5" :
                self.value = 3
            case "6" :
                self.value = 4
            case "7" :
                self.value = 5
            case "8" :
                self.value = 6
            case "9" :
                self.value = 7
            case "T" :
                self.value = 8
            case "J" :
                self.value = -1
            case "Q" :
                self.value = 10
            case "K" :
                self.value = 11
            case "A" :
                self.value = 12

    def isUpper(self, c) :
        return self.value > c.value

    def isEqual(self, c) :
        return self.value == c.value

class Hand :
    def __init__(self, text, bid) :
        self.bid = bid
        self.cards = [Card(text[i]) for i in range(5)]
        self.value = 0
        dico = {}
        for elem in text :
            if elem in dico :
                dico[elem] += 1
            else :
                dico[elem] = 1
        match len(dico) :
            case 1 :
                self.value = 6
            case 2 :
                for x in dico.values() :
                    if x == 4 :
                        self.value = 5
                        break
                    if x == 3 :
                        self.value = 4
                        break
                if "J" in dico :
                    self.value = 6
            case 3 :
                for x in dico.values() :
                    if x == 2 :
                        self.value = 2
                        if 'J' in dico :
                            self.value = dico["J"] + 1 + self.value
                        break
                    if x == 3 :
                        self.value = 3
                        if 'J' in dico :
                            self.value = 5
                        break
            case 4 :
                self.value = 1
                if "J" in dico :
                    self.value = 3
            case 5 :
                if "J" in dico :
                    self.value = 1

    def isUpper(self, hand) :
        if self.value > hand.value :
            return True
        if self.value < hand.value :
            return False
        for i in range(5) :
            if self.cards[i].isUpper(hand.cards[i]) :
                return True
            if hand.cards[i].isUpper(self.cards[i]) :
                return False
        return False

    def __str__(self) :
        return f"{self.value}, {self.bid}"

def fusion(l1, l2) :
    l = [None for _ in range(len(l1) + len(l2))]
    pos = pos1 = pos2 = 0
    while pos1 < len(l1) and pos2 < len(l2) :
        if l1[pos1].isUpper(l2[pos2]) :
            l[pos] = l2[pos2]
            pos += 1
            pos2 += 1
        else :
            l[pos] = l1[pos1]
            pos += 1
            pos1 += 1
    if pos1 < len(l1) :
        while pos1 < len(l1) :
            l[pos] = l1[pos1]
            pos += 1
            pos1 += 1
    else :
        while pos2 < len(l2) :
            l[pos] = l2[pos2]
            pos += 1
            pos2 += 1
    return l

def tri_fusion(l) :
    if len(l) < 2 :
        return l
    return fusion(tri_fusion(l[:len(l)//2]), tri_fusion(l[len(l)//2:]))

def main() :
    hands = []
    with open("input", encoding = "utf-8") as file :
        for line in file :
            l = line.split()
            hands.append(Hand(l[0], int(l[1])))
    hands = tri_fusion(hands)
    win = 0
    for pos, hand in enumerate(hands, start = 1) :
        win += pos*hand.bid
    print(win)

main()