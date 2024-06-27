import constants
import matplotlib.pyplot as plot
from . import AnalysisBase

class CountsAnalysis(AnalysisBase):
    def count_per_type(self):
        # Count the number of Pokémon for each primary type
        type_counts = self.data_frame["Type 1"].value_counts()

        # Get the colors for each type from the custom palette
        colors = [constants.type_palette[type_] for type_ in type_counts.index]

        # Plotting the pie chart
        figure = plot.figure(figsize=(6, 6))

        ## Two major problems with the default pie chart:
        ## 1) There are a lot of values ~3%, making the chart unreadable.
        ## This is solved with "explode", which seperates slices so they become readable.

        explode = [0.05] * len(type_counts)
        plot.pie(
            type_counts,
            labels=type_counts.index,
            autopct='%1.1f%%',
            colors=colors,
            explode=explode,
            pctdistance=.8,
            labeldistance=1.1,
        )

        ## 2) Title needs a padding. This wasn't an issue with other chart types,
        ## but piechart does need more space than others.
        ## so we add pad=20

        plot.title("Distribution of Pokémon by Primary Type", pad=20)
        plot.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Define the output path
        output_path = self.output_directory / "counts" / "per_type.png"
        
        # Return the plot with its path in a list of tuples
        self.plots.append((output_path, figure))
        
        return self
