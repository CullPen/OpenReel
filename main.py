def recommend_videos(user_history, all_videos, num_recommendations=3):
    """
    A super basic video recommendation algorithm based on shared tags.

    Args:
        user_history (list): A list of video IDs the user has interacted with (e.g., watched, liked).
        all_videos (dict): A dictionary where keys are video IDs and values are
                           dictionaries containing video information, including 'tags'.
                           Example:
                           {
                               "video1": {"title": "Funny Cats", "tags": ["cats", "funny", "animals"]},
                               "video2": {"title": "Coding Tutorial", "tags": ["coding", "tutorial", "python"]},
                               "video3": {"title": "More Cats!", "tags": ["cats", "cute", "animals"]}
                           }
        num_recommendations (int): The number of videos to recommend.

    Returns:
        list: A list of recommended video IDs.
    """

    if not user_history:
        # If the user has no history, recommend some popular or random videos.
        # For simplicity, let's just return the first few videos.
        return list(all_videos.keys())[:num_recommendations]

    # 1. Identify user interests based on their history
    user_tags = set()
    for video_id in user_history:
        if video_id in all_videos:
            user_tags.update(all_videos[video_id]['tags'])

    # 2. Score other videos based on shared tags with user interests
    video_scores = {}
    for video_id, video_info in all_videos.items():
        if video_id not in user_history:  # Don't recommend videos the user has already seen
            score = 0
            for tag in video_info['tags']:
                if tag in user_tags:
                    score += 1
            video_scores[video_id] = score

    # 3. Sort videos by score in descending order
    sorted_videos = sorted(video_scores.items(), key=lambda item: item[1], reverse=True)

    # 4. Return the top N recommended videos
    recommended_videos = [video_id for video_id, score in sorted_videos[:num_recommendations]]
    return recommended_videos

# Example Usage:
all_videos_data = {
    "video1": {"title": "Funny Cats", "tags": ["cats", "funny", "animals"]},
    "video2": {"title": "Coding Tutorial", "tags": ["coding", "tutorial", "python"]},
    "video3": {"title": "More Cats!", "tags": ["cats", "cute", "animals"]},
    "video4": {"title": "Python Basics", "tags": ["coding", "python", "beginner"]},
    "video5": {"title": "Dog Tricks", "tags": ["dogs", "training", "animals"]},
    "video6": {"title": "Advanced Python", "tags": ["coding", "python", "advanced"]},
}

user_history_data = ["video1", "video3"]  # User has watched "Funny Cats" and "More Cats!"

recommendations = recommend_videos(user_history_data, all_videos_data)
print(f"Recommended videos for the user: {recommendations}")

user_history_empty = []
recommendations_empty_history = recommend_videos(user_history_empty, all_videos_data)
print(f"Recommended videos for a new user: {recommendations_empty_history}")
