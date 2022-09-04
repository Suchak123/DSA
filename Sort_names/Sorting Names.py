import random #for performing random operations
import string #for ascii characters/letters

#all uppercase letters from A-Z => "ABC.....XYZ"
letters = string.ascii_uppercase

letters = list(string.ascii_uppercase) #converts into a list => ["A","B"...."Y","Z"]

random.shuffle(letters) #randomly shuffles the letters in list
print(letters)

names = ["Suchak Niraula","Aastha Shrestha","Alok Khadka","Amshu Man Maharjan","Binisha Naga","Shisant ","Rachana Shrestha","Sayal Karki","Sailesh Achhami","Sarad Kathayat","Samyog Dhital","Manish Karki","Reebhu Adhikari","Prashant Bista","Praveen Shrestha","Milan Gyawali","Amish Chaudhary","Aabhash Basnet","Nayan Shrestha","Kamal Soud","Nulok Rai","Perisa Koirala","Shriya Shrestha","Ivaan Prajapati","Lasta Pudasaini","Smarika Shrestha","Nirdesika Chuhan","Suzana Pyakhurel","Shirish Shrestha","Pranjal Neupane","Salil Shrestha","Raseek Shrestha","Sulav Karki","Rohan Taujale","Saransh Sharma","Saurav Kathayat","Anmol Shrestha","Sisam Ghaju","Rachana Ghaju","Reya Awal","Krima Madhi","Sareena Shrestha","Rubeen Shrestha","Rohan Karanjit","Chirag Ds","Deepika Sainju","Usha Suwal"]

names.sort() #sorts names in ascending order


for letter in letters: #for individual letter
    names_starting_with_current_letter = []
    for name in names: #for individual names
         if name.startswith(letter):   #if name starts with letter in letters
            names_starting_with_current_letter.append(name) 
    if names_starting_with_current_letter:    #if list is non empty
        for name in names_starting_with_current_letter: 
            print(f"{name}")
        
            