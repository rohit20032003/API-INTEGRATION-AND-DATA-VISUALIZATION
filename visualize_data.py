import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(temp, feels_like, humidity, city):
    """Create a bar chart to visualize weather parameters."""
    categories = ['Temperature (°C)', 'Feels Like (°C)', 'Humidity (%)']
    values = [temp, feels_like, humidity]

    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.barplot(x=categories, y=values, palette="viridis")
    plt.title(f"Current Weather Data for {city}", fontsize=16)
    plt.xlabel("Parameters", fontsize=12)
    plt.ylabel("Values", fontsize=12)
    plt.tight_layout()
    plt.show()
