import time 
import json

class Stopwatch: 
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.total_xp = 0

    def start(self):
        if self.start_time is None:
            self.start_time = time.time()
        else:
            print("Stopwatch is already running")

    def stop(self):
        if self.start_time is not None:
            self.elapsed_time += time.time() - self.start_time
            self.start_time = None
        else: 
            print("Stopwatch is not Running")

    def get_elapsed_time(self, format='seconds'):
        if self.start_time is not None:
            return self.elapsed_time +(time.time() - self.start_time)
        
        if format == 'minutes':
            return round(self.elapsed_time / 60, 2)
        elif format == 'hours':
            return round(self.elapsed_time / 3600, 2)

        return round(self.elapsed_time)
    
    def reset(self):
        self.start_time = None
        self.elapsed_time = 0

    def save_state(self, filename="stopwatch_state.json"):
        state = {
            'start_time': self.start_time,
            'elapsed_time': self.elapsed_time
        }
        with open(filename, 'w') as f:
            json.dump(state, f)
    
    def load_state(self, filename="stopwatch_state.json"):
        try: 
            with open(filename, 'r') as f:
                state = json.load(f)
                self.start_time = state['start_time']
                self.elapsed_time = state['elapsed_time']
                if self.start_time is not None:
                    self.start_time = float(self.start_time)
        except FileNotFoundError:
            pass

    def calculate_xp_from_elapsed(self, elapsed_seconds):
        xp_per_30_minutes = 50
        return(elapsed_seconds // 1800) * xp_per_30_minutes
    
    def calculate_level(self):
        base_xp = 50 
        level = 0
        xp = self.total_xp
        while xp >= base_xp:
            level += 1
            xp -= base_xp
            base_xp += 50
        return level
    
    def get_xp_and_level(self):
        level = self.calculate_level()
        return self.total_xp, level