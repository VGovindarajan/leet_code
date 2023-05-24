f = [i for i in range(12,0,-1)]
t = []
a = []

def tower_of_hanoi(n, from_tower, to_tower, auxillary_tower):

    if n > 0:

        if len(from_tower) == 1:
            to_tower.append(from_tower.pop())
            print(f"Now to_tower is {to_tower}")
            return

        # Move n-1 discs to the aux tower
        tower_of_hanoi(n=n-1, from_tower=from_tower, to_tower=auxillary_tower, auxillary_tower=to_tower)

        # Move nth disc to the to tower
        to_tower.append(from_tower.pop())

        print(f"from={f},to={t},aux={a} ")

        # Move the n-1 discs from aux to the to tower
        tower_of_hanoi(n=n-1, from_tower=auxillary_tower, to_tower=to_tower, auxillary_tower=from_tower)

        return



def main():

    tower_of_hanoi(len(f), f, t, a)

    print(f)
    print(t)
    print(a)


if __name__ == "__main__":
    main()
