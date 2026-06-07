import numpy as np

rainfall= np.array([12,130,67,45,350,400,450,360,320,470,178,360],dtype=np.float64)
months= np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul",
                  "Aug","sep", "Oct","Nov","Dec"])

wettest_pos=np.argmax(rainfall)
driest_pos=np.argmin(rainfall)

wettest_month=months[wettest_pos]
wettest_rainfall=rainfall[wettest_pos]

driest_month=months[driest_pos]
driest_rainfall=rainfall[driest_pos]

clipped_rainfall=np.clip(rainfall,10,400)
cumulative_rain=np.cumsum(rainfall)

sorted_positions=np.argsort(rainfall)[::-1]
sorted_months=months[sorted_positions]
sorted_rainfall=rainfall[sorted_positions]

print("="*50)
print("         RAINFALL ANALYZER - NEPAL")
print("="*50)

print(f"Total yearly rainfall   : {np.sum(rainfall)} mm")
print(f"Average monthly rain    : {np.mean(rainfall):.1f} mm")
print(f"Wettest month           : {wettest_month} ({wettest_rainfall}) mm")
print(f"Driest month            : {driest_month} ({driest_rainfall} mm)")

print("="*45)
print("    MONTHLY RAINFALL WITH CUMULATIVE TOTAL")
print("="*45)

print(f"{'Month':<8} {'Rainfall':>10}{'Clipped':>10}{'Cumulative':>12}")
print('-'*45)
for i in range(len(rainfall)):
    print(f"{months[i]:<8} {rainfall[i]:>8.1f} mm {clipped_rainfall[i]:>8.1f} mm {cumulative_rain[i]:>10.1f}mm")
print()

print("=" * 40)
print("   MONTHS RANKED BY RAINFALL (HIGH→LOW)")
print("=" * 40)

print(f"{'Rank':<6}{'Month':<8}{'Rainfall':>10}")
print('-'*40)

for rank,idx in enumerate(sorted_positions,start=1):
    print(f"{rank:<6}{months[idx]:<8}{rainfall[idx]:>9} mm")
print()

data_to_save=np.column_stack([rainfall,clipped_rainfall,cumulative_rain])
header="Rainfall(mm)\tClipped(mm)\tCumultaive(mm)"

np.savetxt(
    "rainfall_data.txt",
    data_to_save,
    fmt="%.1f",
    delimiter="\t",
    header=header,
    comments=""   
)

print("File saved: rainfall_data.txt")
print("  Columns: Rainfall | Clipped | Cumulative")