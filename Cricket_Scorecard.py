import numpy as np

players_name=["Rohit","Bhurtel","Aashif","Malla","Dipendra"]

runs=np.array([
    [45, 0,  88, 12, 120, 33, 67, 0,  95, 50],   
    [72, 55, 0,  99, 44,  88, 11, 76, 33, 60],   
    [10, 88, 44, 0,  77,  55, 90, 22, 66, 33],   
    [0,  33, 77, 55, 88,  0,  44, 99, 11, 66],   
    [55, 22, 33, 44, 11,  77, 88, 0,  99, 44], 
])

balls=np.array([
    [60,  1,  95, 20, 140, 45, 80,  1,  110, 65],   
    [90,  70,  1,  110, 55, 100, 15, 88, 40, 72],  
    [15,  100, 55, 1,  90, 65, 105, 30, 80, 45],  
    [1,   45, 88, 65, 100, 1,  55, 115, 15, 80],   
    [65,  30, 45, 55, 15,  90, 100, 1, 115, 55],  
])

match_numbers=np.arange(1,11)
innings_played=np.count_nonzero(runs,axis=1)
print(innings_played)
print("="*50)
print("          CRICKET SCORECARD ANALYZER")
print("="*50)

print("--- Innings Played (non-duck innnings) ---")
for i,player in enumerate(players_name):
    print(f"{player:14} : {innings_played[i]} innings")
print()

total_runs=np.sum(runs,axis=1)
print("--- Total Runs in 10 matches ---")
for i,player in enumerate(players_name):
    print(f"{player:14}  : {total_runs[i]} runs")
print()    


batting_average= total_runs/innings_played
print("--- Batting Average (runs per innings) ---")
for i,player in enumerate(players_name):
    print(f"{player:14}  : {batting_average[i]:.1f}")
print()

print("--- Strike Rate (runs per 100 balls) ---")
total_balls=np.sum(balls,axis=1)
strike_rate=(total_runs/total_balls)*100
for i,player in enumerate(players_name):
    print(f"{player:14}  : {strike_rate[i]:.2f}")
print()

best_match_idx=np.argmax(runs,axis=1)
print("--- Best Match ---")
for i,player in enumerate(players_name):
    match_num=match_numbers[best_match_idx[i]]
    best_score=runs[i,best_match_idx[i]]
    print(f"{player:14} : Match {match_num} {best_score} runs ")
print()

runs_no_duck= np.where(runs == 0 , 999, runs)

worst_match_idx = np.argmin(runs_no_duck, axis=1)
print("\n--- Worst Match (excluding ducks) ---")
for i,player in enumerate(players_name):
    match_num=match_numbers[worst_match_idx[i]]
    worst_run=runs[i,worst_match_idx[i]]
    print(f"{player:14}  : Match {match_num}  {worst_run} runs")
print()

rank_idx= np.argsort(batting_average)[::-1]
print(rank_idx)
print("--- player Rankings (by Batting Average) ---")
print(f"{'Rank':5} {'player':>14}{'Avg':>8}{'SR':>8}{'Total Runs':>15}")
print("  " + "-" * 50)
for rank,idx in enumerate(rank_idx):
    print(f"{rank+1:5} {players_name[idx]:>14} {batting_average[idx]:>8.2f} {strike_rate[idx]:>8.2f} {total_runs[idx]:>10}")