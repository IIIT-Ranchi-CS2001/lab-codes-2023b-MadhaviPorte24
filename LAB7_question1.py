import matplotlib.pyplot as plt

def plot_election_results():
    # Data for Madhya Pradesh and Rajasthan
    mp_parties = ['BJP', 'INC', 'BSP', 'Others']
    mp_seats = [163, 66, 0, 1]
    mp_total_seats = sum(mp_seats)
    mp_percentages = [seats / mp_total_seats * 100 for seats in mp_seats]

    rj_parties = ['INC', 'BJP', 'BSP', 'Others']
    rj_seats = [69, 115, 2, 13]
    rj_total_seats = sum(rj_seats)
    rj_percentages = [seats / rj_total_seats * 100 for seats in rj_seats]

    # Colors
    colors = ['blue', 'orange', 'green', 'gray']

    # Find party with highest percentage
    mp_highest_index = mp_percentages.index(max(mp_percentages))
    rj_highest_index = rj_percentages.index(max(rj_percentages))

    # Create the figure and subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # Madhya Pradesh Pie Chart
    axes[0].pie(
        mp_percentages, labels=mp_parties, autopct='%1.1f%%', startangle=90,
        explode=[0.1 if i == mp_highest_index else 0 for i in range(len(mp_parties))],
        colors=colors, shadow=True
    )
    axes[0].set_title("Madhya Pradesh Assembly Results 2023")

    # Rajasthan Pie Chart
    axes[1].pie(
        rj_percentages, labels=rj_parties, autopct='%1.1f%%', startangle=90,
        explode=[0.1 if i == rj_highest_index else 0 for i in range(len(rj_parties))],
        colors=colors, shadow=True
    )
    axes[1].set_title("Rajasthan Assembly Results 2023")

    # Adjust layout for pie charts
    plt.tight_layout()

    # Create a bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_width = 0.35
    index = range(len(mp_parties))

    ax.bar(index, mp_seats, bar_width, label='Madhya Pradesh', color='blue')
    ax.bar(
        [i + bar_width for i in index], rj_seats, bar_width, label='Rajasthan', color='orange'
    )

    # Set labels and titles for bar chart
    ax.set_xlabel('Parties')
    ax.set_ylabel('Seats Won')
    ax.set_title('Assembly Results 2023: Madhya Pradesh & Rajasthan')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(mp_parties)
    ax.legend()

    # Show the plots
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_election_results()
