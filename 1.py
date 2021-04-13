def read_from_database():
    try:
        Prdcts=[]
        F=open("Store/database.csv","r")
        BText=F.read()

        Prdct_List=BText.split('\n')
        
        for i in range(len(Prdct_List)):
            Prdct_Info=Prdct_List[i].split(',')
            Prdcts.append({'Id':Prdct_Info[0],'Name':Prdct_Info[1],'Price':Prdct_Info[2],'Count':Prdct_Info[3] })
    except Exception as e:
        print(e)
        Prdcts=[]

    return Prdcts

def Add():
    Id=input('Enter id : ')
    Name=input('Enter Name : ')
    Price=input('Enter Price : ')
    Count=input('Enter Count : ')
    Prdcts.append({'Id: ':Id,'Name: ':Name,'Price: ':Price,'Count: ':Count })


def Search():
    U_Input = input('Enter a Text to Search ==>')

    for Item in Prdcts:
        if Item['Id']==U_Input or Item['Name']==U_Input:
            print(Item)
            break
    else:
            print('Not found !!')

def Edit():
    
    Edit_N = input('Select The Product You Want To Edit')
    for Item in range(len(Prdcts)):
        if Edit_N == Prdcts[Item]['Name']:
            Prdcts[Item]['Name'] = input('Ente a New Name : ')
            Prdcts[Item]['Price'] = input('Ente a New Price: ')
            Prdcts[Item]['Count'] = input('Ente a New Count: ')
            break
    else:
        print('There is no Product With This Name in Stock,Please Try Again ...')

    ShowMenu()


def Remove():
    
    Remove_O= input('Select The Knockout Option ')
    for Item in Prdcts:
        if Item['Id']==Remove_O or Item['Name']==Remove_O:
            Prdcts.remove(Item)
            break
    else:
        print('not found!')

    ShowMenu()


def Buy():
    pass
#vaqean Ino bald nbodm :((

def ShowAll():
    for Item in Prdcts:
        print(Item)    
def Exit():
    AExit = input('Are you sure you want to log out?')
    if AExit == "Yes":
        File = open("database.csv", "a")
        for Item in Prdcts:
            File.write(str(F"\n{Item}"))
            exit()
    else:
        exit()

def ShowMenu():
    print('Welcme To My Store :) ')
    print('1-  Add ')
    print('2-  Search ')
    print('3-  Edit ')
    print('4-  Remove ')
    print('5-  Buy ')
    print('6-  Show All ')
    print('7-  Exit ')


Prdcts=read_from_database()
while True:
    ShowMenu()

    Choice=input('Enter Your Choice: ')
#bayad user entekhab kone 
    if Choice=='1':
        Add()
    elif Choice=='2':
        Search()
    elif Choice=='3':
        Edit()
    elif Choice=='4':
        Remove()
    elif Choice=='5':
        Buy()
    elif Choice=='6':
        ShowAll()
    elif Choice=='7':
        Exit()

