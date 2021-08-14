ADA_P = [1.3,1.4,1.7,1.5,1.4,1.6,1.5,1.4,1.6] # ราคา last price
USDT = 50 # จำนวนพอร์ต USDT
ADA = 50 # ADA_balance on $
fix = 50 # fix
min = 6 # min trading
sum_max = fix+min  # 60
sum_min = fix-min  # 40
time = 0
while time <=8 :
    ADA_DAY = ADA_P[time] * ADA
    if ADA_DAY > sum_max:
        amt = ADA_DAY-fix
        ADA = ADA - (amt / ADA_P[time])
        print(f"ขาย ADA ออก {amt} $")
        USDT += amt

    elif ADA_DAY < sum_min:
        amt = fix - ADA_DAY
        ADA = ADA + (amt / ADA_P[time])
        print(f"ซื้อ ADA เข้า {amt} $")
        USDT -= amt
    else:
        print("ทันมือ")
    time+=1

print(ADA)
print(USDT)
