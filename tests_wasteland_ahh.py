__author__ = 'bradleygoldstein'


#
#
p = Player("brad")
c = Card("hearts", 4)
d = Card("spades", 5)
e = Card("diamonds", 6)
f = Card("hearts", 7)
g = Card("hearts", 8)
c_s = [c,d,e,f,g]
for c in c_s:
    p.add_random_card(p.private, c)
    print
    print p.peek_at_top(p.private)
    print p.peek_at_bottom(p.private)
# p.private = [c,d, e, f,g]
for c in p.private:
    print c
# # p.print_p()
# # f = p.peek_at_top(p.private)
# # print f.rank, f.suit
# # p.print_p()
# # f = p.get_top(p.private)
# # print f.rank, f.suit
# # p.print_p()
# # p.collect_cards(p.private, [c,d])
# # p.print_p()
#
p.print_p()
print rank(p.private)
# p.give_random_card(p.private)
# p.print_p()



# p = Player("brad")
c = Card("hearts", 4)
d = Card("hearts", 5)
e = Card("hearts", 9)
f = Card("hearts", 7)
g = Card("hearts", 8)
c_s = [c,d,e,f,g]

# p.private = [c,d, e, f,g]
# for c in p.private:
#     print c
#
# p.print_p()
print rank(c_s)