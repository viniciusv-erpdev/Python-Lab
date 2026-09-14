# Compare se o número do meio da lista ou a média entre o primeiro e segundo números da lista são iguais a média da lista
hand = [4,5,6,7,8,9,10]

def approx_average_is_average(hand):

    average = sum(hand)/len(hand)

    average_first_last = (hand[0] + hand[-1])/2

    average_by_middle = hand[len(hand) // 2]

    print(f'Normal average: {average}')
    print(f'Avarege by first and last cards: {average_first_last} \n')
    print(f'Avarege by mean: {average_by_middle} \n')

    if average_first_last == average or average_by_middle == average:

        return True

    else:
        return False

print(approx_average_is_average(hand))