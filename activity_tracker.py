import time
class ActivityTracker: 
    def __init__(self):
        self.activities = {}

    def start_activity(self, activity):
        if activity not in self.activities:
            self.activities[activity] = []
        self.activities[activity].append({"start":time.time(), "stop": None})

    def stop_activity(self, activity): 
        if activity in self.activities and self.activities[activity][-1]["stop"] is None:
            self.activities[activity][-1]["stop"] = time.time()

    def get_total_time(self, activity):
        if activity not in self.activities:
            return 0 
        total_time = 0 
        for i in self.activities[activity]:
            if i["stop"]:
                total_time += i["stop"] - i["start"]
            return total_time

