from collections import Counter

def normalize_time(dt):
    return dt.replace(minute=(0 if dt.minute < 30 else 30), second=0, microsecond=0)

def get_user_habit_times(meals, top_n: int = 3):
    times = [normalize_time(meal.created_at) for meal in meals]

    if not times:
        return []

    most_common = Counter(times).most_common(top_n)

    return [t for t, _ in most_common]