def books():
    booklist = ["Eragon, Chris Paolini", "Metamorphasis, Franz Kafa", "Deltora, Emily Rodda", "Meditations, Marcus Aurelius"]
    slicedlist = booklist[0:3]

    slicedlisttest = ["Eragon, Chris Paolini", "Metamorphasis, Franz Kafa", "Deltora, Emily Rodda"]

    for ele in slicedlisttest:
        assert ele in slicedlist

    print("Finished books")

def students():
    studict = {"Alpha":101,"Beta":202, "Delta":303}

    studicttest = {"Alpha":101,"Beta":202, "Delta":303}

    for ele in studicttest:
        assert ele in studict

    print("Finished students")

books()
students()