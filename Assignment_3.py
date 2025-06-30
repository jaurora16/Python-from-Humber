# First Name: Jessica
# Last Name: Aurora
def find_points_for_organizer(organizer, courses, points):
    total_points = 0
    for course, course_organizer in courses.items():
        if course_organizer == organizer:
            total_points += points.get(course, 0)
    return total_points
# Sample data
courses = {"Analytics": "Johannes", "Mega analytics": "Johannes", "Basic analytics": "John"}
points = {"Analytics": 15, "Mega analytics": 10, "Basic analytics": 5}
# Example usage
print(find_points_for_organizer('Johannes', courses, points))
