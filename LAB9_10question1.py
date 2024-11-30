import os
import pandas as pd
import matplotlib.pyplot as plt

# Election data
data = [
    ['Madhya Pradesh', 'BJP', 163, 230, 72.1],
    ['Madhya Pradesh', 'INC', 66, 230, 72.1],
    ['Madhya Pradesh', 'BSP', 0, 230, 72.1],
    ['Madhya Pradesh', 'Others', 1, 230, 72.1],
    ['Rajasthan', 'BJP', 115, 200, 74.2],
    ['Rajasthan', 'INC', 69, 200, 74.2],
    ['Rajasthan', 'BSP', 2, 200, 74.2],
    ['Rajasthan', 'Others', 13, 200, 74.2],
]

# Column names
columns = ['State', 'Party', 'Seats_Won', 'Total_Seats', 'Voter_Turnout (%)']

# File name
file_name = 'election_data.csv'

# Check if the file exists and write the data if it doesn't
try:
    if not os.path.exists(file_name):
        # Create the DataFrame and write to CSV
        df = pd.DataFrame(data, columns=columns)
        df.to_csv(file_name, index=False)
        print(f"{file_name} created and data written successfully.")
    else:
        # If the file exists, read it
        df = pd.read_csv(file_name)
        print(f"{file_name} already exists, data loaded successfully.")
except Exception as e:
    print(f"Error with file handling: {e}")

# Read the data into a Pandas DataFrame (if not already done)
try:
    # Calculate the percentage of seats won by each party
    df['Seats_Percentage'] = (df['Seats_Won'] / df['Total_Seats']) * 100

    # Display the updated DataFrame
    print("\nData with Seats Percentage:")
    print(df)

    # Determine the party with the highest number of seats in each state
    highest_seats_party = df.loc[df.groupby('State')['Seats_Won'].idxmax()][['State', 'Party']]
    print("\nParty with the highest number of seats in each state:")
    print(highest_seats_party)

    # Create a bar chart showing the number of seats won by each party in each state
    plt.figure(figsize=(10, 6))
    for state in df['State'].unique():
        state_data = df[df['State'] == state]
        plt.bar(state_data['Party'], state_data['Seats_Won'], label=state)

    plt.title('Number of Seats Won by Each Party in Each State')
    plt.xlabel('Party')
    plt.ylabel('Seats Won')
    plt.legend(title="State", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error with data processing or plotting: {e}")
