from flask import Flask, jsonify

app = Flask(__name__)
video_titles = [
    "The Art of Coding", 
    "Exploring the Cosmos", 
    "Cooking Masterclass: Italian Cuisine", 
    "History Uncovered: Ancient Civilizations", 
    "Fitness Fundamentals: Strength Training", 
    "Digital Photography Essentials", 
    "Financial Planning for Beginners", 
    "Nature's Wonders: National Geographic", 
    "Artificial Intelligence Revolution", 
    "Travel Diaries: Discovering Europe"
]

# Task 1 - Implement the binary search algorithm for searching videos by title.

def binary_search(arr, target):
    sorted_arr = sorted(arr) # I will sort the "video_titles" array above
    low = 0
    high = len(sorted_arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            low = mid + 1
        else: 
            high = mid - 1
    return -1

target_index = binary_search(video_titles, "Exploring the Cosmos")

print(f'"Exploring the Cosmos" is located at index {target_index}.')

# Task 2
# Develop a REST API endpoint using Flask that allows users to search for videos by their titles using the binary search developed in Task 1. 
# This API should accept a search query as input and return the matching videos, if any.

@app.route('/')
def home():
    return "Video Search Application with Binary Search.\n\
    To start, input \"/videos/\" into your browser's address bar, followed by the title of the video you wish to search for."

@app.route('/videos/<string:video_title>')
def get_video_title_index(video_title):
    video_title_index = binary_search(video_titles, video_title)
    data = {
        "index": video_title_index
    }
    return jsonify(data)

# Task 3
# Test the video search functionality using Postman or a similar tool. 
# Send requests to the API endpoint created in Task 2 with different search queries to verify its correctness and efficiency. 
# Ensure that the API returns the expected results for both existing and non-existing videos.
# Task complete!!!

if __name__ == "__main__":
    app.run(debug=True)