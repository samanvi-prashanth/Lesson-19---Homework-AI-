import requests
def get_fact() :
    url = "https://factfacts.com/api.php"
    response = requests.get(url)
    if response.status_code == 200 :
        fact = response.json()
        return f"\nDid you know ? : {fact['fact']['text']}\n"
    else :
        return "Failed to retrieve fact"
def main()  :
    print('\nWelcome to fun fact generator !\n')
    while True :
        user = input('Press enter to get a joke or q to exit : ').strip().lower()
        if user in ('q', 'exit') :
            print('\nGoodbye!\n')
            break
        fact = get_fact()
        print(fact)
if __name__ == "__main__" :
    main()