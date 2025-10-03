import time

def pomodoro_timer(work=25, short_break=5, cycles=4):
    for i in range(cycles):
        print(f"Pomodoro {i+1}: Work for {work} minutes")
        time.sleep(work * 60)
        print("Break time!")
        time.sleep(short_break * 60)
    print("Pomodoro session complete!")


