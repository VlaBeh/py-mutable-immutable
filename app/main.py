lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}

apr = one_is_a_prime_number
bfl = my_favourite_films
col = collection_of_coins
sorted_variables = {
    "mutable": [],
    "immutable": []
}
for i in [lucky_number, pi, apr, name, bfl, profile_info, marks, col]:
    if isinstance(i, (list, dict, set)):
        sorted_variables["mutable"].append(i)
    else:
        sorted_variables["immutable"].append(i)
print((sorted_variables))
