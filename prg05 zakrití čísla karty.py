def card_hide(card_num):
    hidden_card = ""
    for i in range(len(card_num)):
        if i < 12:
            hidden_card += "*"
        else:
            hidden_card += card_num[i]
    return hidden_card
print(card_hide("5858462284778568"))
