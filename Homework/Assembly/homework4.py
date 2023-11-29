import random

def simulate_seek(maxSeekTime, numSimulations):
    totalSeekTime = 0

    for int in range(num_simulations):
        # Randomly select two tracks on the platter
        track1 = random.uniform(0, 1) # Assuming tracks are represented as a percentage of radial extent
        track2 = random.uniform(0, 1) # , so we can use a unit circle for infinite tracks!

        # Calculate the time for the head to move from the first track to the second
        currentSeekTime = abs(track2 - track1) * max_seek_time

        totalSeekTime += currentSeekTime

    # Calculate the average seek time
    averageSeekTime = totalSeekTime / numSimulations

    return averageSeekTime

# Set parameters
max_seek_time = 12  # Maximum seek time from innermost to outermost track in milliseconds
num_simulations = 6000000  # Number of simulations to perform

# Run the simulation
average_seek_time = simulate_seek(max_seek_time, num_simulations)

# Print the result
print(f"Average Seek Time (Monte Carlo simulation): {average_seek_time:.2f} ms")
