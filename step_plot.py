import pandas as pd
import matplotlib
# Use the Agg backend to prevent hanging in a terminal environment
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Load the data, EXPLICITLY setting the delimiter to ensure correct reading
# If the plots are empty, try changing delimiter=',' to delimiter=';'
try:
    roll_data = pd.read_csv('roll_step_response_roll_0_pitch_0.csv', delimiter=',')
    prbs_data = pd.read_csv('prbs_roll_0_pitch_0.csv', delimiter=',')
except FileNotFoundError as e:
    print(f"Error: {e}. Make sure the CSV files are in the correct directory.")
    exit()

# Optional: Print the columns to verify they were read correctly
# print("Roll Data Columns:", roll_data.columns.tolist()) 

# Plot roll step response (Figure 1)
plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(roll_data['__time'], roll_data['/psm_joint_telemetry/roll/position'])
plt.title('Roll Step Response')
plt.ylabel('Position')

plt.subplot(2, 1, 2)
plt.plot(roll_data['__time'], roll_data['/psm_joint_telemetry/roll/velocity'])
plt.xlabel('Time (s)')
plt.ylabel('Effort')

plt.savefig('roll_step_response_plot.png') 
# ---------------------------------------------------------------------

# Plot pitch PRBS response (Figure 2)
plt.figure(2)
plt.subplot(2, 1, 1)
plt.plot(prbs_data['__time'], prbs_data['/psm_joint_telemetry/pitch/position'])
plt.title('Pitch PRBS Response')
plt.ylabel('Position')

plt.subplot(2, 1, 2)
plt.plot(prbs_data['__time'], prbs_data['/psm_joint_telemetry/pitch/velocity'])
plt.xlabel('Time (s)')
plt.ylabel('Effort')

plt.savefig('pitch_prbs_response_plot.png')

print("Plots saved successfully as roll_step_response_plot.png and pitch_prbs_response_plot.png")
