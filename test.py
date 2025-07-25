dicta = [
{"Goose2" :"ห่านเกรด Economic","Price" :"50 บาท","time":"12"},
{"Goose1" :"ห่านเกรด Premium", "Price":"100 บาท" ,"time":"14"}
]
m =12

def timeloop1():
    for i in range(8,13,1) :
        print ( i ,".00")
def timeloop2():
    for i in range(8,17,1) :
        print ( i ,".00")
customer = "0"
print ("ยินดีต้อนรับสู่ห่านย่าง The KMUTT ")

print ("ราคาถูกที่สุดในประเทศไทย ปลอดภัย ")

print("-----------------")
print("โปรดเลือกห่านเกรดที่ท่านต้องการ:")
print( dicta )

customer = input("1.ห่าน Premium  เเละ 2.ห่าน Economic:  ")

i=0
if (customer == "1"):
    print("ราคา 100 บาทนะคะ")
    print("-----------------")
    op1 = input("โปรดพิมพ์ Yes:   ")
    op1 == "Yes" 
    print("สังดเกต รปภ อ้างอิงเวลา")
    timeloop1()
    print (" you get Goose1 ")
    print (" ตั้งร้านค้าขายห่าน")
    for x in range (3) :
        print("กำลังเตรียม")
    print("---------------")
    for x in range (9) :
        print("ปรุง")
    print("---------------")
    print(" your order is completed")
elif (customer == "2" ):
    print("ราคา 50 บาท นะคะ")
    print("-----------------")
    op1 = input("โปรดพิมพ์ Yes:   ")
    op1 == "Yes" 
    print("สังดเกต รปภ อ้างอิงเวลา")
    timeloop2()
    print (" you get Goose1 ")
    print (" ตั้งร้านค้าขายห่าน")
    for x in range (3) :
         print("กำลังเตรียม")
    print("---------------")
    for x in range (9) :
            print("ปรุง")
    print("---------------")
    print(" your order is completed")





   

# timeloop()

