#rumus keuntungan (Π)=Q**3 +15*Q**2 + 13*Q – 30.000
print("rumus keuntungan:(Q)**3 +15*(Q**2) + 13*Q-30000")
Q=input("Q=");
Q=int(Q)
rumus = (Q)**3 +15*(Q**2) + 13*Q-30000;
print (rumus)
if (rumus>700000):
    print("keuntungan besar")
elif (rumus>0) & (rumus<=700000):
     print("keuntungan kecil")
elif rumus <=0:
     print("rugi")
