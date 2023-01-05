import random
from emails import sendEmails

def main():
    # enter your personalized data here formatted as [("name", "address@email.com"), ... ]
    nameEmailPairs = []
    giftPairs = determineOrder(nameEmailPairs)
    sendEmails(giftPairs)
    outputToFile(giftPairs)

# Purpose:  Create a closed loop of pairs [(a, b), (b, c), ... , (z, a)] in a random order 
# In:       NameEmailPairs, array of all names and email addresses of the participants [(name, email), ... ]
# Out:      GiftPairs, array of tuples representing who each participant is giving a gift to  
# Note:     The first part each (a, b) tuple is the name and email of the gift giver, the second is the name only of the recipient ((name, email), name)
def determineOrder(nameEmailPairs):
    if(nameEmailPairs == []): return []
    giftPairs = []

    prev = 0
    first = nameEmailPairs[0][0]
    for i in range(len(nameEmailPairs) - 1):
        rand = random.choice([j for j in range(len(nameEmailPairs)) if j != prev])
        giftPairs.append((nameEmailPairs[prev], nameEmailPairs[rand][0]))

        del nameEmailPairs[prev]
        if prev > rand: prev = rand
        else:           prev = rand - 1

    giftPairs.append((nameEmailPairs[prev], first))
    return giftPairs

# Purpose:  Print the results of the program to output.txt
# In:       Array of tuples with information on the giver and reviever [((giverName, giverEmail), recieverName), ... ]
def outputToFile(giftPairs):
    f = open('output.txt', 'w')
    for giver, reciever in giftPairs:
        print(f'{giver[0]} has {reciever}')
        f.write(f'{giver[0]} has {reciever}\n')
    f.close()

    
if __name__ == "__main__":
    main()