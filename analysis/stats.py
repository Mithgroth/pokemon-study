import constants
import seaborn
import matplotlib.pyplot as plot
from . import AnalysisBase

class StatsAnalysis(AnalysisBase):
    def correlation_of_stats(self):
        # Calculate the correlation matrix
        correlation_matrix = constants.data_frame[
            ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Total"]
        ].corr()

        # Plotting
        figure = plot.figure(figsize=(6, 6))
        seaborn.heatmap(correlation_matrix, annot=True, cmap="coolwarm", center=0)

        plot.title("Correlation Heatmap of Pokémon Stats")
        plot.xticks(rotation=45)

        # Define the output path
        output_path = self.output_directory / "stats" / "correlation_heatmap.png"

        # Return the plot with its path in a list of tuples
        self.plots.append((output_path, figure))

        return self

    def cdfs_of_stats_for_top_pokemon(self):
        thresholds = [10, 50]

        # Sort the data frame by 'Total' in descending order
        sorted_data_frame = self.data_frame.sort_values(by="Total", ascending=False)

        for threshold in thresholds:
            subset = sorted_data_frame.head(threshold)
            title = f"CDFs of Stats for Top {threshold} Pokémon"
            filename = f"cdfs_top_{threshold}.png"
            output_path = self.output_directory / "stats" / filename

            # Plotting
            plot.figure(figsize=(14, 10))
            for i, stat in enumerate(
                ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"], 1
            ):
                plot.subplot(2, 3, i)
                seaborn.histplot(
                    subset[stat], kde=False, stat="density", cumulative=True
                )
                plot.title(f"CDF of {stat}")
                plot.xlabel(stat)
                plot.ylabel("Cumulative Probability")
                plot.grid(True)
            plot.suptitle(title, fontsize=16)
            plot.tight_layout(rect=[0, 0.03, 1, 0.95])

            figure = plot.gcf()  # Get the current figure, sigh bloody abbrevations...
            self.plots.append((output_path, figure))

        return self
