#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# JRoe, 2020-Aug-31, created file
# JRoe, 2020-Sep-04, Added error handling, changed data type to list (of CD objects), added annotation / comments, bolstered docstrings
#------------------------------------------#
 
# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
open(strFileName, 'a').close() #Creates blank file

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    #Constructor
    def __init__(self, pos, titl, artist):
        
    #Attributes
        self.__position = pos
        self.__title = titl
        self.__artist = artist
    
    #Properties
      
    @property
    def position(self):
        return self.__position
     
    @position.setter
    def position(self, value):
        if type(value) == int:
            self.__position = value
        else: 
            raise Exception('Integers Only!')
                
    @property
    def title(self):
        return self.__title
        
    @title.setter
    def title(self, value):
        if type(value) == str:
            self.__title = value
        else:
            raise Exception('String Only!')
        
    @property
    def artist(self):
        return self.__artist
        
    @artist.setter
    def artist(self, value):
        if type(value) == str:
            self.__artist = value
        else:
            raise Exception('String Only!')
    def __str__(self):
        return '{},{},{}'.format(self.__position, self.__title, self.__artist)
    

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_fxn(file_name, lst_Inventory): -> None
        read_file(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def read_file(file_name, table):
        """Function to read list objects (CD objects) from file
        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            lstOfCDObjects.append(line)
        objFile.close()

        
    @staticmethod
    def save_fxn(file_name, table):
        """Function to save entered data to designated file
        Args:
            None.
        Returns:
            None.
        """      

        objFile = open(file_name, 'w')

        for row in table:
            strrow = str(row)
            print(strrow)
            objFile.write(strrow + '\n')
        objFile.close() 

# -- PRESENTATION (Input/Output) -- #
class IO:
    
    """Handling Input / Output
    Properties: None
    Methods:
            print_menu(): prints user menu (header)
            menu_choice(); prints user menu (options)
            user_entry(table): gets user input
            show_inventory(table): Shows list stored in local memory"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        Args:
            None.
        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        Args:
            None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def user_entry(table): 
        """Gets user input for "enter data" section 
        Args:
            None.
        Returns:
            None
        """

        # Ensure only integer inputs
        while True:

            ID = input('Enter the ID Number: ')
            # Ensure only integer inputs
            try:
                intID = int(ID)
                break
            except ValueError:
                print('\nIntegers Only!\n')
                continue          
        Title = input('Enter the Title: ')
        Artist = input('Enter the Artist: ')
        first = CD(intID, Title, Artist)
        table.append(first)    
    
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
        Args:
            table that holds the data during runtime.
        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title\t Artist\n')
        for row in table:
            print(row)
        print('======================================')


# -- Main Body of Script -- #

# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program

# 1. When program starts, read in the currently saved Inventory

FileIO.read_file(strFileName, lstOfCDObjects)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.read_file(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        IO.user_entry(lstOfCDObjects)
        # 3.3.2 Add itiem to the table

        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    
    
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? ALL DATA IN FILE WILL BE LOST! [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_fxn(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')


































