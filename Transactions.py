import Storage


class Transactions:

    def __init__(self, x, y, z, i):
        self.x, self.y, self.z, self.i = x, y, z, i

        if self.i == 1:
            self.Purchase(self.x, self.y)
        elif self.i == 11:
            self.Purchase_From(self.x, self.y, self.z)
        elif self.i == 2:
            self.Purchase_Ops(self.x, self.y, self.z)
        elif self.i == 3:
            self.Owned_Cars()
        elif self.i == 4:
            self.Unowned_Cars()

    def Purchase(self, x, y):

        if Storage.Storage.User_Dic[x] >= Storage.Storage.Car_Name_List[y][3]:
            Storage.Storage.User_Dic.update({x: int(Storage.Storage.User_Dic[x] - Storage.Storage.Car_Name_List[y][3])})
            Storage.Storage.Car_Dic.update({str(Storage.Storage.Car_Name_List[y]): True})
            if Storage.Storage.Ownership_Dic[x] == [0]:
                Storage.Storage.Ownership_Dic.update({x: [Storage.Storage.Car_Name_List[y]]})
                del Storage.Storage.Car_Name_List[y]
            else:
                Storage.Storage.Ownership_Dic[x].append(Storage.Storage.Car_Name_List[y])
                del Storage.Storage.Car_Name_List[y]
        else:
            print(x, "can not afford this car\n")

    def Purchase_Ops(self, x, y, z):

        if Storage.Storage.User_Dic[x] >= Storage.Storage.Option_Dic[z]:
            Storage.Storage.User_Dic[x] -= Storage.Storage.Option_Dic[z]
            del Storage.Storage.Car_Dic[str(Storage.Storage.Car_Name_List[y])]
            Storage.Storage.Ownership_Dic[x][y][3] += Storage.Storage.Option_Dic[z]
            Storage.Storage.Car_Dic.update({str(Storage.Storage.Car_Name_List[y]): True})
        else:
            print(x, "can not afford this option\n")

    def Purchase_From(self, x, y, z):

        if Storage.Storage.User_Dic[x] >= Storage.Storage.Ownership_Dic[y][0][3]:
            Storage.Storage.User_Dic[x] -= Storage.Storage.Ownership_Dic[y][0][3]
            Storage.Storage.User_Dic[y] += Storage.Storage.Ownership_Dic[y][0][3]  # Depending on the fuel they use,
            if Storage.Storage.Ownership_Dic[y][z][2] == "Benzin":                 # the price goes down after a second hand transaction
                Storage.Storage.Ownership_Dic[y][z][3] -= int(Storage.Storage.Ownership_Dic[y][z][3] * (10 / 100))
            elif Storage.Storage.Ownership_Dic[y][z][2] == "Dizel":
                Storage.Storage.Ownership_Dic[y][z][3] -= int(Storage.Storage.Ownership_Dic[y][z][3] * (15 / 100))
            elif Storage.Storage.Ownership_Dic[y][z][2] == "Elektrik":
                Storage.Storage.Ownership_Dic[y][z][3] -= int(Storage.Storage.Ownership_Dic[y][z][3] * (20 / 100))
            if Storage.Storage.Ownership_Dic[x] == [0]:
                Storage.Storage.Ownership_Dic.update({x: [Storage.Storage.Ownership_Dic[y][z]]})
                del Storage.Storage.Ownership_Dic[y][z]
            else:
                Storage.Storage.Ownership_Dic[x].append(Storage.Storage.Ownership_Dic[y][z])
                del Storage.Storage.Ownership_Dic[y][z]
        else:
            print(x, "can not afford", y, "'s car")


    def Owned_Cars(self):
        for i in Storage.Storage.Ownership_Dic:
            if Storage.Storage.Ownership_Dic[i] != [0] and Storage.Storage.Ownership_Dic[i] != []:
                print(i, Storage.Storage.Ownership_Dic[i])


    def Unowned_Cars(self):
        for i in Storage.Storage.Car_Dic:
            if Storage.Storage.Car_Dic[i] is False:
                print(i)