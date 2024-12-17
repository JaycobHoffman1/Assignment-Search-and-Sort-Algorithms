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

# Task 1: Implement the merge sort algorithm in Python to sort videos by their titles.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

print(merge_sort(video_titles))

# Task 2
# Develop another REST API endpoint using Flask that allows users to fetch a list of videos sorting alphabetically 
# by their titles using the merge sort developed in Task 1.

@app.route('/')
def home():
    return "Video Sorting with Merge Sort.\n\
    To start, input \"/videos\" into your browser's address bar to see an alphabetized list of video titles."

@app.route('/videos')
def get_video_titles():
    alph_video_titles = merge_sort(video_titles)
    data = {
        "video titles": alph_video_titles
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

# Task 3
# Test the video sorting functionality using Postman or a similar tool. 
# Send requests to the API endpoint created in Task 2 and verify its correctness and efficiency. 
# Ensure that the API returns the expected results.
# Task complete!!!