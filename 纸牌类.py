#实例1-1 一摞有序的纸牌
import collections
Card = collections.namedtuple("Card",["rank","suit"])
class FrenchDeck: #通过类来建立一副扑克牌
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                       for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self,position):
        return self._cards[position]
# beer_card = Card("7","diamonds")
# print(beer_card)
deck = FrenchDeck()
# print(len(deck))
# print(deck[0])
#for i in deck: #迭代整套牌
   # print(i)

#for card in reversed(deck): #反向迭代
    #print(card)
#迭代通常是隐式的，譬如说一个集合类型没有实现__contains__方法，那么in运算符就会按顺序做一次迭代搜索。于是，in运算符可以用在我们FrenchDeck类上，因为它是可迭代的。

#如何排序，按照常规，用点数来判断扑克牌的大小，2最小、A最大；同时还要加上花色的判定，spade最大，heart最小，diamond次之，club最小。

suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
# for card in sorted(deck,key=spades_high):
#     print(card)
print(FrenchDeck.suits)
print(dir(collections))