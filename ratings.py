"""Restaurant rating lister."""


# read scores file and return a dictionary of {restaurant-name: score}


def process_scores():

    scores_txt = open('scores.txt')

    scores = {}

    for line in scores_txt:
        line = line.rstrip()
        restaurant, score = line.split(":")

        scores[restaurant] = int(score)

        return scores

# add a restaurant and rating


def add_restaurant(scores):
    print('Please add a rating for your favorite restaurant!')
    restaurant = input('Restaurant name> ')
    rating = int(input('Rating> '))

    scores[restaurant] = rating

# print sorted restaurants and ratings


def print_sorted_scores(score):
    for restaurant, rating in sorted(scores.items()):
        print(f'{restaurant} is rated at {rating}.')


# read existing scores in from file
scores = process_scores()

# allow user to add a restaurant/rating pair
add_restaurant(scores)

# print a list of the restaurants and their ratings in alphabetical order
print_sorted_scores(scores)
