nominee1 = "BJP"
nominee2 = "CONGRESS"

nom_1_votes = 0
nom_2_votes = 0

votes_id = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
num_of_voters = (len(votes_id))

while True:
    if votes_id == []:
        print("VOTING SESSION IS OVER")

        if nom_1_votes>nom_2_votes:
            percent = (nom_1_votes/num_of_voters)*100
            print(f"{nominee1} won the election with {percent}% votes.")
            break

        elif nom_2_votes>nom_1_votes:
            percent = (nom_2_votes/num_of_voters)*100
            print(f"{nominee2} won the election with {percent}% votes.")
            break


    voter = int(input("ENTER YOUR VOTER ID NO. : "))
    if voter in votes_id:
        print("You are a authorised voter")
        votes_id.remove(voter)
        vote = int(input('''Choose whom you want to vote 
        1 for BJP
        2 for CONGRESS\n'''))

                
        if vote == 1:
            nom_1_votes += 1
            print(f"Thank you for voting to {nominee1}\n\n")

        elif vote == 2:
            nom_2_votes += 2
            print(f"Thank you for voting to {nominee2}\n\n")

    else:
        print("VOTER ID DOESN'T EXIT OR YOU HAVE ALREADY VOTED.\n")        