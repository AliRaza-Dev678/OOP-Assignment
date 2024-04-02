class Buildings():
    def __init__(IUB):
        IUB.campus1=""
        IUB.campus2=""
        IUB.campus3=""
        IUB.campus4=""
        IUB.campus5=""
    def IUB_Buildings(IUB):
        print (IUB.campus1)
        print(IUB.campus2)
        print(IUB.campus3)
        print(IUB.campus4)
        print(IUB.campus5)

a1=Buildings()
a1.campus1="Baghdad ul jadeed campus Bahawalpur"
a1.campus2="Abbasia campus Bahawalpur"
a1.campus3="Railway campus Bahawalpur"
a1.campus4="Bahawalnagar campus"
a1.campus5="Raheem yar campus"
a1.IUB_Buildings()

class Rooms(Buildings):
    def __init__(Uni):
        Uni.Rooms=""
        Uni.SE_Rooms=""
        Uni.SE_Labs=""
    def IUB_Rooms(Uni):
        print(Uni.Rooms)
        print(Uni.SE_Rooms)
        print(Uni.SE_Labs)

a2=Rooms()
a2.Rooms=("There are atleast 1000 rooms in IUB Baghdad UL Jadeed campus")
a2.SE_Rooms=("There are atleast 50 rooms in SE Department")
a2.SE_Labs=("There are atleast 10 Labs in SE Department")
a2.IUB_Rooms()

        
     

   



        




