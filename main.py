import argparse 
from stopwatch import Stopwatch
from activity_tracker import ActivityTracker
#Implement the ArguementParser object to input arguements 
def parse_arguements():
    parser = argparse.ArgumentParser(description="CLU Stopwatch")

    parser.add_argument("command", choices=["start", "stop", "status"], help="Control the stopwatch")
    parser.add_argument("activity", nargs='?', help="Specify the activity")
    parser.add_argument("--format", choices=["seconds", "minutes", "hours"], default="seconds", help="Specify the time format (seconds or minutes)")

    return parser.parse_args()

def main():
    args = parse_arguements()
    stopwatch = Stopwatch()
    tracker = ActivityTracker()

    stopwatch.load_state()

    if args.command == "start": 
        tracker.start_activity(args.activity)
        stopwatch.start()
        print(f"Started {args.activity}")
    elif args.command == "stop":
        tracker.stop_activity(args.activity)
        stopwatch.stop()
        print((f"Stopped {args.activity}. Total time: {stopwatch.get_elapsed_time(args.format)} {args.format}"))
    elif args.command == "status":
        elapsed_time = stopwatch.get_elapsed_time(args.format)
        unit = "seconds" if args.format == "seconds" else "minutes" if args.format == "minutes" else "hours"
        print(f"Elapsed time for activity: {args.activity}: {elapsed_time} {unit}")
        xp, level = stopwatch.get_xp_and_level()
        print(f"XP:{xp} Current Level{level} in {args.activity}")
    
    stopwatch.save_state()
if __name__ == "__main__":
    main()