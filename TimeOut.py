# coding: utf-8
import json
from jsoncomment import JsonComment

users = 'users.json'
venues = 'venues.json'


def load_json(filename):
    '''A simple function to load json files.'''
    
    with open(filename,'r') as f:
        parser = JsonComment(json)  #Remove trailing commas
        return parser.load(f)
    
load_users = load_json(users)
load_venues = load_json(venues)

places_to_avoid = {}  #Venues with nothing to eat/drink
all_venues = []  #All available venues
for venue in load_venues:
        #All available drinks in a venue (lowercase) 
        venue_drinks = [drink.lower() for drink in venue['drinks']]
        #All available food in a venue (lowercase) 
        venue_food = [food.lower() for food in venue['food']]
        all_venues.append(venue['name'])
        for user in load_users:
            #A user's list of drinks
            user_drinks = [drink.lower() for drink in user['drinks']]
            #A user's list of won't eat food
            user_food = [food.lower() for food in user['wont_eat']]
            #Check if user has something to drink
            drink_exists = list(set(venue_drinks) & set(user_drinks))
            #Check if user has something to eat
            food_exists = list(set(venue_food) - set(user_food))
            if  not food_exists:
                #If nothing to eat, add to places to avoid
                if not places_to_avoid.get(venue['name']):
                    places_to_avoid[venue['name']] = []
                places_to_avoid[venue['name']].append("{} has nothing to eat. ".format(user['name']))
            if  not drink_exists:       
                #If nothing to drink, add to places to avoid
                if not places_to_avoid.get(venue['name']):
                    places_to_avoid[venue['name']] = []
                places_to_avoid[venue['name']].append("{} has nothing to drink. ".format(user['name']))
                

print("Places to avoid:\n")
for key,value in places_to_avoid.items():
    print ("{}: ".format(key))
    for item in value:
        print("\t{}".format(item))
    print("\n")

places_to_go = set(all_venues)-set(places_to_avoid.keys())
print("Places to go:")
for place in places_to_go:
    print("\t{}".format(place))



