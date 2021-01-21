class Storage:

    def __init__(self, Cars_File, Users_File, Options_File):
        self.Cars_File, self.Users_File, self.Options_File = Cars_File, Users_File, Options_File
        self.Car_Name_List = self.Clear(self.Cars_File, int(3))
        self.User_Name_List = self.Clear(self.Users_File, int(1))
        self.Options_Name_List = self.Clear(self.Options_File, int(1))
        self.Car_Dic, self.User_Dic, self.Option_Dic, self.Ownership_Dic = self.Create_Dic(self.Car_Name_List,
                                                                                           self.User_Name_List,
                                                                                           self.Options_Name_List)

    def Clear(self, File, n):  # Makes the data we got from reading the .txt files more understandable

        File_Name_List = []

        for i in File.readlines():
            File_Name_List.append(i)

        for i in range(len(File_Name_List)):
            File_Name_List[i] = File_Name_List[i].split(',')
            File_Name_List[i][n] = File_Name_List[i][n].rstrip("\n")

        for i in range(len(File_Name_List)):
            File_Name_List[i][n] = int(File_Name_List[i][n])

        return File_Name_List


    def Create_Dic(self, Car_Name_List, User_Name_List, Options_Name_List):

        User_Dic, Car_Dic, Option_Dic, Ownership_Dic = {}, {}, {}, {}

        if len(User_Name_List) > 0:
            for j in range(len(User_Name_List)):
                User_Dic[User_Name_List[j][0]] = User_Name_List[j][1]


        if len(Car_Name_List) > 0:  # Creates the dictionary which will check if a car has a owner
            for i in range(len(Car_Name_List)):
                Car_Dic[str(Car_Name_List[i])] = False


        if len(Options_Name_List) > 0:
            for i in range(len(Options_Name_List)):
                Option_Dic[Options_Name_List[i][0]] = Options_Name_List[i][1]


        for i in range(len(User_Name_List)):
            Ownership_Dic[str(User_Name_List[i][0])] = [0]

        return Car_Dic, User_Dic, Option_Dic, Ownership_Dic


Cars_File = open("cars.txt", "r")
Users_File = open("users.txt", "r")
Options_File = open("options.txt", "r")

Storage = Storage(Cars_File, Users_File, Options_File)

Cars_File.close()
Users_File.close()
Options_File.close()

if __name__ == '__main__':  # If this module is run from this module, execute these
    print("CAR NAME LIST: ", Storage.Car_Name_List, "\n")
    print("USER NAME LIST: ", Storage.User_Name_List, "\n")
    print("OPTIONS LIST: ", Storage.Options_Name_List, "\n")
    print("THIS IS USER/ACCOUNT DICTIONARY: ", Storage.User_Dic, "\n")
    print("THIS IS CAR DICTIONARY: ", Storage.Car_Dic, "\n")
    print("THIS IS OPTIONS DICTIONARY: ", Storage.Option_Dic, "\n")
    print("OWNER DIC: ", Storage.Ownership_Dic)
