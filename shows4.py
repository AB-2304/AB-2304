"""
This version of the program:
1. Loads the data from a JSON file
2. Searches for a TV show in the data
3. Formats the show details
4. Shows all actors in the show and their roles
4. Searches for an actor/character in the cast
5. Shows detailed information about a selected actor/character
"""

import json
from zipfile import ZipFile 
  
def load_json(filename) -> dict:
    """
    Load JSON from a file
    """
    with open(filename, 'r') as file:
        TV_shows = json.load(file)
        return TV_shows

def find_show(query: str, shows: dict) -> str:
    """
    Search for TV shows in the shows dictionary
    Return the name of the first (only one) result based on the query
    If the show is not found, return None
    """
    for show in shows:
        if query.lower() in show.lower():
            show_name = show
            break
        else:
            show_name = None
    return show_name
    
def find_actor(query: str, cast: list[dict]) -> dict:
    """
    Search for an actor in the cast list
    Return the actor's data if found
    If the actor is not found, return None
    """
    for details in cast:
        actor_details = details.get("person")
        actor_name = actor_details.get("name")
        character_name = details.get("character").get("name")
        if query.lower() in character_name.lower() or query.lower() in actor_name.lower():
            actor_dict = actor_details
            break
        else:
            actor_dict = None
    return actor_dict
        
def get_show_data_by_name(show_name: str, shows: dict) -> dict:
    """
    Return the data for a show based on its name
    """
    showname = find_show(show_name, shows)
    if showname != None:
        data = shows.get(showname)
    return data

def format_show_details(show: dict) -> str:
    """
    Format the show details
    """
    show_name = show.get("name")
    genres = show.get("genres")
    genres = ", ".join(genres)
    premiered_year = show.get("premiered")
    ended_year = show.get("ended")
    if premiered_year == None:
        premiered_year = "?"
    else:
        premiered_year = premiered_year[0:4]  # slice to get only year of prmeiered date (eg: 2002-06-11)   
    if ended_year == None:
        ended_year = "?" 
    else:
        ended_year = ended_year[0:4]
    formated_str = f"{show_name} ({premiered_year} - {ended_year}, {genres})"
    return formated_str

def get_cast_by_id(show_id: int) -> list[dict]:
    """
    Get the cast for a show
    """
    file_name = f"cast/{show_id}_cast.json"
    cast_list = load_json(file_name)
    return cast_list

def format_cast(cast: list[dict]) -> str:
    """
    Format the cast
    """
    cast_format = ""
    for details in cast:
        cast_name = details.get("person").get("name")
        character_name = details.get("character").get("name")     
        cast_format += f"{cast_name} as {character_name}\n"   
    return cast_format

def format_actor_info(actor_dict: dict) -> str:
    """
    Format the actor's information
    """
    name = actor_dict.get("name")
    if actor_dict.get("gender") == None:
        gender = "?"  
    else:
        gender = actor_dict.get("gender")
    if actor_dict.get("birthday") == None:
        born = "?"
    else:
        born = actor_dict.get("birthday")
    if actor_dict.get("country") == None:
        country = "?"
    else:
        country = actor_dict.get("country").get("name")
    return f"{name} ({gender}, born {born} in {country})"

def character_played(cast, actor_format):
    """
    create a dictionary with the actors' names and their corresponding characters' names.
    returns the name of the character played by the actor chosen by the user.
    """
    cast_format = {}
    for details in cast:
        cast_name = details.get("person").get("name")
        character_name = details.get("character").get("name")
        cast_format[cast_name] = character_name
    actor_name = actor_format[0:(actor_format.find("(")-1)]  # slice first part of actor_format to get actor_name
    character = cast_format.get(actor_name)
    return character

def main():
    """
    Main function 
    """
    # Unzip the zip archive with JSON files containing the cast data
    with ZipFile("C:\\Users\\abhir\\Downloads\\cast.zip", 'r') as zObject:  
        zObject.extractall()    
    shows = load_json("C:\\Users\\abhir\\Downloads\\tvshows.json")
    query = input("Search for a TV show: ")
    show_name = find_show(query, shows)
    if show_name:
        data = get_show_data_by_name(show_name, shows)
        formated_str = format_show_details(data)
        show_id = data.get("id")
        cast = get_cast_by_id(show_id)
        cast_format = format_cast(cast)
        print(f"Found: {formated_str}\nCast:\n{cast_format}")
        actor_query = input("Search for an actor or character: ")
        actor_dict = find_actor(actor_query, cast)
        if actor_dict:
            actor_format = format_actor_info(actor_dict)
            character = character_played(cast, actor_format)
            print(f"Found: {actor_format} plays {character}")
        else:
            print("Can't find this actor or character in the cast!")
    else:
        print("Can't find this TV show in the Top 100!")
    

if __name__ == '__main__':
    main()