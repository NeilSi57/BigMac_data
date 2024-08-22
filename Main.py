#Main.py
#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df =pd.read_csv('data/global_inflation_data.csv')


global_inflation_data= original_df[['country_name','indicator_name','2008','2012','2016','2020','2024']] 

global_inflation_data = global_inflation_data.dropna()

row1 = global_inflation_data.iloc[0:30]
row2 = global_inflation_data.iloc[30:60]
row3 = global_inflation_data.iloc[60:90]
row4 = global_inflation_data.iloc[90:120]
row5 = global_inflation_data.iloc[120:150]
row6 = global_inflation_data.iloc[150:187]

#----Define Functions Below----#
def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(global_inflation_data)

def showCharts():
    row1.plot(
            kind='bar',
            x='country_name',
            y='2024',
            color='blue',
            alpha=0.3,
            title='Inflation rate for 2024')
    row2.plot(
            kind='bar',
            x='country_name',
            y='2024',
            color='blue',
            alpha=0.3,
            title='Inflation rate for 2024')

    row3.plot(
            kind='bar',
            x='country_name',
            y='2024',
            color='blue',
            alpha=0.3,
            title='Inflation rate for 2024')

    row4.plot(
            kind='bar',
            x='country_name',
            y='2024',
            color='blue',
            alpha=0.3,
            title='Inflation rate for 2024')

    row5.plot(
            kind='bar',
            x='country_name',
            y='2024',
            color='blue',
            alpha=0.3,
            title='Inflation rate for 2024')

    row6.plot(
            kind='bar',
            x='country_name',
            y='2024',
            color='blue',
            alpha=0.3,
            title='Inflation rate for 2024')
    plt.show()

def showAustralia():
    result_df=global_inflation_data[global_inflation_data['country_name'] == 'Australia']
    print(result_df)

def userOptions():
    global quit

    print("""Welcome to the Global inflation data Extraordinaire!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the global inflation rate
    4 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showCharts()
        elif choice == 4:
            showAustralia()
        elif choice == 5:
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')

   

#----Main program----#
while not quit:
    userOptions()
