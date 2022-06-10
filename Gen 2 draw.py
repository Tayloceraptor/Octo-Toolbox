def printer():

    alphabet =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# Header / Title
    print("")
    print("       |~~~~~~~~~~~~~~~~|")
    print("      /__________________\\")
    print("      | My Octo Tool Box |")
    print("      | Gen 2 Prototyper |")
    print("      |__________________|")
    print("")
    
# Input Prime Traits - Gen 2 updated
    while True:
        prime = input("Enter your first eight letters: \n").upper() + input("Enter your second eight letters: \n").upper()

        if (len(prime) !=16):
            print("Invalid Entry - Must be 16 characters")
            continue
        if prime.isalpha():
            break
        else:
            print("Invalid Entry - Must be Alpha")
            continue
        break
    
# Select Decorations
    decor_list = ("A","B","C","D")
    print("\n")
    print ("Decorations?")
    print("A. Crossword")
    print("B. Stack")
    print("C. Ring")
    print("D. Diagonal")
    
# Decore input check
    while True:
        decor = input("Enter your selection : ").upper()
        try:
            decor in decor_list
        except:
            print("Invalid Selection, Try again: ")
            continue
        if decor not in decor_list:
            continue
        else:
            break
    
    
    # Empty Board
    a1 = (" ")
    a2 = (" ")
    a3 = (" ")
    a4 = (" ")
    a5 = (" ")
    a6 = (" ")
    a7 = (" ")
    a8 = (" ")
    b1 = (" ")
    b2 = (" ")
    b3 = (" ")
    b4 = (" ")
    b5 = (" ")
    b6 = (" ")
    b7 = (" ")
    b8 = (" ")
    c1 = (" ")
    c2 = (" ")
    c3 = (" ")
    c4 = (" ")
    c5 = (" ")
    c6 = (" ")
    c7 = (" ")
    c8 = (" ")
    d1 = (" ")
    d2 = (" ")
    d3 = (" ")
    d4 = (" ")
    d5 = (" ")
    d6 = (" ")
    d7 = (" ")
    d8 = (" ")
    e1 = (" ")
    e2 = (" ")
    e3 = (" ")
    e4 = (" ")
    e5 = (" ")
    e6 = (" ")
    e7 = (" ")
    e8 = (" ")
    f1 = (" ")
    f2 = (" ")
    f3 = (" ")
    f4 = (" ")
    f5 = (" ")
    f6 = (" ")
    f7 = (" ")
    f8 = (" ")
    g1 = (" ")
    g2 = (" ")
    g3 = (" ")
    g4 = (" ")
    g5 = (" ")
    g6 = (" ")
    g7 = (" ")
    g8 = (" ")
    h1 = (" ")
    h2 = (" ")
    h3 = (" ")
    h4 = (" ")
    h5 = (" ")
    h6 = (" ")
    h7 = (" ")
    h8 = (" ")
    
# Calculate Crossword
    if decor == ("A"):
        print ("\n Please Enter Row and Column \n ")
        while True:
            try:
                row = int(input("Enter Row : "))
            except ValueError:
                print ("Value must be between 1-8")
                continue
            if row < 1 or row > 8:
                continue
            else:
                break
        while True:
            try:
                column = int(input("Enter column : "))
            except ValueError:
                print("Value must be between 1-8")
                continue
            if column < 1 or column > 8:
                print("Invalid Entry. must be between 1-8 : ")
                continue
            else:
                break

# Calculate crossword column

        if column == int("1"):
            a1 = prime[8]
            b1 = prime[9]
            c1 = prime[10]
            d1 = prime[11]
            e1 = prime[12]
            f1 = prime[13]
            g1 = prime[14]
            h1 = prime[15]
        if column == int("2"):
            a2 = prime[8]
            b2 = prime[9]
            c2 = prime[10]
            d2 = prime[11]
            e2 = prime[12]
            f2 = prime[13]
            g2 = prime[14]
            h2 = prime[15]
        if column == int("3"):
            a3 = prime[8]
            b3 = prime[9]
            c3 = prime[10]
            d3 = prime[11]
            e3 = prime[12]
            f3 = prime[13]
            g3 = prime[14]
            h3 = prime[15]
        if column == int("4"):
            a4 = prime[8]
            b4 = prime[9]
            c4 = prime[10]
            d4 = prime[11]
            e4 = prime[12]
            f4 = prime[13]
            g4 = prime[14]
            h4 = prime[15]
        if column == int("5"):
            a5 = prime[8]
            b5 = prime[9]
            c5 = prime[10]
            d5 = prime[11]
            e5 = prime[12]
            f5 = prime[13]
            g5 = prime[14]
            h5 = prime[15]
        if column == int("6"):
            a6 = prime[8]
            b6 = prime[9]
            c6 = prime[10]
            d6 = prime[11]
            e6 = prime[12]
            f6 = prime[13]
            g6 = prime[14]
            h6 = prime[15]
        if column == int("7"):
            a7 = prime[8]
            b7 = prime[9]
            c7 = prime[10]
            d7 = prime[11]
            e7 = prime[12]
            f7 = prime[13]
            g7 = prime[14]
            h7 = prime[15]
        if column == int("8"):
            a8 = prime[8]
            b8 = prime[9]
            c8 = prime[10]
            d8 = prime[11]
            e8 = prime[12]
            f8 = prime[13]
            g8 = prime[14]
            h8 = prime[15]
            
# Calculate crossword Row

        if row == int("1"):
            a1 = prime[0]
            a2 = prime[1]
            a3 = prime[2]
            a4 = prime[3]
            a5 = prime[4]
            a6 = prime[5]
            a7 = prime[6]
            a8 = prime[7]
        if row == int("2"):
            b1 = prime[0]
            b2 = prime[1]
            b3 = prime[2]
            b4 = prime[3]
            b5 = prime[4]
            b6 = prime[5]
            b7 = prime[6]
            b8 = prime[7]
        if row == int("3"):
            c1 = prime[0]
            c2 = prime[1]
            c3 = prime[2]
            c4 = prime[3]
            c5 = prime[4]
            c6 = prime[5]
            c7 = prime[6]
            c8 = prime[7]
        if row == int("4"):
            d1 = prime[0]
            d2 = prime[1]
            d3 = prime[2]
            d4 = prime[3]
            d5 = prime[4]
            d6 = prime[5]
            d7 = prime[6]
            d8 = prime[7]
        if row == int("5"):
            e1 = prime[0]
            e2 = prime[1]
            e3 = prime[2]
            e4 = prime[3]
            e5 = prime[4]
            e6 = prime[5]
            e7 = prime[6]
            e8 = prime[7]
        if row == int("6"):
            f1 = prime[0]
            f2 = prime[1]
            f3 = prime[2]
            f4 = prime[3]
            f5 = prime[4]
            f6 = prime[5]
            f7 = prime[6]
            f8 = prime[7]
        if row == int("7"):
            g1 = prime[0]
            g2 = prime[1]
            g3 = prime[2]
            g4 = prime[3]
            g5 = prime[4]
            g6 = prime[5]
            g7 = prime[6]
            g8 = prime[7]
        if row == int("8"):
            h1 = prime[0]
            h2 = prime[1]
            h3 = prime[2]
            h4 = prime[3]
            h5 = prime[4]
            h6 = prime[5]
            h7 = prime[6]
            h8 = prime[7]

# Calculate Box Pattern

    if decor == ("B"):
        c3 = prime[0]
        c4 = prime[1]
        c5 = prime[2]
        c6 = prime[3]
        d3 = prime[4]
        d4 = prime[5]
        d5 = prime[6]
        d6 = prime[7]
        e3 = prime[8]
        e4 = prime[9]
        e5 = prime[10]
        e6 = prime[11]
        f3 = prime[12]
        f4 = prime[13]
        f5 = prime[14]
        f6 = prime[15]
    
# Calculate Ring Pattern

    if decor == ("C"):
        b3 = prime[0]
        b4 = prime[1]
        b5 = prime[2]
        b6 = prime[3]
        c7 = prime[4]
        d7 = prime[5]
        e7 = prime[6]
        f7 = prime[7]
        g6 = prime[8]
        g5 = prime[9]
        g4 = prime[10]
        g3 = prime[11]
        f2 = prime[12]
        e2 = prime[13]
        d2 = prime[14]
        c2 = prime[15]
    
# Calculate Diagonal Pattern
    
    if decor == ("D"):
        a1 = prime[0]
        b2 = prime[1]
        c3 = prime[2]
        d4 = prime[3]
        e5 = prime[4]
        f6 = prime[5]
        g7 = prime[6]
        h8 = prime[7]
        a8 = prime[8]
        b7 = prime[9]
        c6 = prime[10]
        d5 = prime[11]
        e4 = prime[12]
        f3 = prime[13]
        g2 = prime[14]
        h1 = prime[15]
    
    
# Print Visual Prime
    print("")
    
    print("     _______________________ ")
    print("    |  ___________________  |")
    print("    | |                   | |")
    print("    | |  "   + a1 + " " + a2 + " " + a3 + " " + a4 + " " + a5 + " " + a6 + " " + a7 + " " + a8 + "  | |")
    print("    | |  "   + b1 + " " + b2 + " " + b3 + " " + b4 + " " + b5 + " " + b6 + " " + b7 + " " + b8 + "  | |")
    print("    | |  "   + c1 + " " + c2 + " " + c3 + " " + c4 + " " + c5 + " " + c6 + " " + c7 + " " + c8 + "  | |")
    print("    | |  "   + d1 + " " + d2 + " " + d3 + " " + d4 + " " + d5 + " " + d6 + " " + d7 + " " + d8 + "  | |")
    print("    | |  "   + e1 + " " + e2 + " " + e3 + " " + e4 + " " + e5 + " " + e6 + " " + e7 + " " + e8 + "  | |")
    print("    | |  "   + f1 + " " + f2 + " " + f3 + " " + f4 + " " + f5 + " " + f6 + " " + f7 + " " + f8 + "  | |")
    print("    | |  "   + g1 + " " + g2 + " " + g3 + " " + g4 + " " + g5 + " " + g6 + " " + g7 + " " + g8 + "  | |")
    print("    | |  "   + h1 + " " + h2 + " " + h3 + " " + h4 + " " + h5 + " " + h6 + " " + h7 + " " + h8 + "  | |")
    print("    | |___________________| |")
    print("    |_______________________|")
    print("        " + prime + "   ")
    
    print("")
    
    
    
while True:
    printer()
    
    
    