# define P and Q truth tables
P = [True, True, False, False]
Q = [True, False, True, False]


# create a function to find P->Q
# if P then Q
def p_then_q(p, q):
    if p == q:
        return True
    elif q:
        return True
    else:
        return False


# test it
P_then_Q = []
for i in range(4):
    P_then_Q.append(p_then_q(P[i], Q[i]))
print(P_then_Q)


# create a function that returns the converse Q->P
# if Q then P
def converse(p, q):
    if q == p:
        return True
    elif p:
        return True
    else:
        return False


# test it
Q_then_P = []
for i in range(4):
    Q_then_P.append(converse(P[i], Q[i]))
print(Q_then_P)


# create a function that returns the inverse !P->!Q
# if not P then not Q
def inverse(p, q):
    if (not p) == (not q):
        return True
    elif not q:
        return True
    else:
        return False


# test it
notP_then_notQ = []
for i in range(4):
    notP_then_notQ.append(inverse(P[i], Q[i]))
print(notP_then_notQ)


# create a function that returns the contrapostive !Q->!P
# if not Q then not P
def contrapositive(p, q):
    if (not q) == (not p):
        return True
    elif not p:
        return True
    else:
        return False


# test it
notQ_then_notP = []
for i in range(4):
    notQ_then_notP.append(contrapositive(P[i], Q[i]))
print(notQ_then_notP)

# now let's try it in a practical sense
# if i cooked food, i can eat
cooked_food = True
can_eat = True
# contrapositive is if i can't eat, i didn't cook food
# check if the conditional matches the contrapositive (they should match)
condit = p_then_q(cooked_food, can_eat)
contra = contrapositive(cooked_food, can_eat)
print(condit, contra)

# let's try another
# if i have glasses, then i don't have 2020 vision
has_glasses = True
has_2020 = False
# contrapositive is if i have 2020 vision, i don't have glasses
# check if the conditional matches the contrapositive (they should match)
condit = p_then_q(has_glasses, has_2020)
contra = contrapositive(has_glasses, has_2020)
print(condit, contra)

# try another
# if i don't study, i fail the class
studied = False
passed = False
# contrapositive is if i passed the class, i must have studied
# check if the conditional matches the contrapositive (they should match)
condit = p_then_q(studied, passed)
contra = contrapositive(studied, passed)
print(condit, contra)
