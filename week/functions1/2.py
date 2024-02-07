#f to c:
def far_to_cen(f):
    return (5.0/9.0)*(f-32)
f=20
c=far_to_cen(f)
print("F{0} is C{1}".format(f, c))