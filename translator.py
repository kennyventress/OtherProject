import requests
import json
#import sqlite3 which was downloaded already
import sqlite3

def main():
    #connection Object to represent database
    conn = sqlite3.connect('translatedDictionary.db')

    #creates the myData.db file even if it doesn't exist
    #create cursor to make some SQL commands
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS Translation_Table (
                col1 TEXT,
                col2 TEXT,
                )""")

    valid = True
    while valid == True:
        word = input("What do you want to translate? (Enter 'q' to quit) ")
        if word == 'q':
            break


        # Make an API request
        url = f"https://restcountries.com/v3.1/translation/{word}"
        response = requests.get(url)

        #checks response status
        if response.status_code == 200:
            translation_data = response.json()

            # Extract the translation from the response data
            translated_word = translation_data["translation"]

            # Insert the word and its translation into the database
            c.execute("INSERT INTO Countries (col1, col2) VALUES (?, ?)", (word, translated_word))
            conn.commit()

            print(f"The translation of '{word}' is '{translated_word}'.")

        else:
            print("Translation not found. Please try again.")
            valid = False
        
    # Retrieve all records from the database
    c.execute("SELECT * FROM TranslationTable")
    records = c.fetchall()

    # Print the records
    for record in records:
        print(record)


    # Close the database connection
    conn.close()



if __name__ == "__main__":
    main()


