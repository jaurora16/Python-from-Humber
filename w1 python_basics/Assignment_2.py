# First Name: Jessica
# Last Name: Aurora
def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))
input_list = ['Johannes', 'Jamal', 'Jamal', 'Johannes', 'Galina']
print(*remove_duplicates(input_list))
