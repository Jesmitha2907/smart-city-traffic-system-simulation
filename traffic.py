import time 
 
RED    = "\033[31m" 
GREEN  = "\033[32m" 
YELLOW = "\033[33m" 
RESET  = "\033[0m" 
BRIGHT = "\033[1m" 
TRAFFIC_ICON = "🚦" 
 
def build_signal(lane_idx, active_idx, sec_left): 
    if lane_idx == active_idx: 
        return f"{GREEN}{TRAFFIC_ICON} GREEN  {sec_left:02d}s{RESET}" 
    return f"{RED}{TRAFFIC_ICON} RED    -- s{RESET}" 
 
def run_physics_system(): 
    print("\033[2J\033[H", end="") 
    try: 
        print(f"{BRIGHT}--- GREEN WAVE SIGNAL SYSTEM ---{RESET}") 
        n           = int(input("Number of Junctions: ")) 
        distance_km = float(input("Distance (km)      : ")) 
        speed_kmh   = float(input("Speed (km/h)       : ")) 
    except ValueError: 
        n, distance_km, speed_kmh = 3, 1.0, 40 
 
    travel_lag     = (distance_km / speed_kmh) * 3600 
    green_dur      = 30          
    all_lanes      = ["Lane 1", "Lane 2", "Lane 3", "Lane 4"] 
    cycle_duration = green_dur * len(all_lanes)   
 
    start_time = time.time() 
    try: 
        while True: 
            elapsed = time.time() - start_time 
 
            print("\033[2J\033[H", end="") 
 
            header = f"{'LANE':<8}" 
            for j in range(1, n + 1): 
                header += f" || J-{j:<10}" 
            print(f"{BRIGHT}{header}{RESET}") 
            print("-" * len(header)) 
 
            for l_idx, lane_name in enumerate(all_lanes): 
                row = f"{lane_name:<8}" 
                for j in range(n): 
                    junction_time     = elapsed - (j * travel_lag) 
                    active_time       = junction_time % cycle_duration 
                    active_lane_idx   = int(active_time // green_dur) 
                    seconds_remaining = int(green_dur - (active_time % green_dur)) 
 
                    sig = build_signal(l_idx, active_lane_idx, seconds_remaining) 
                    row += f" || {sig:<15}" 
                print(row) 
 
            time.sleep(1.0 - (time.time() % 1)) 
    except KeyboardInterrupt: 
        print(f"\n{RED}System Shutdown.{RESET}") 
 
if __name__ == "__main__": 
    run_physics_system() 
 
 
