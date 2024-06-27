# Now, visualization!
import constants
import matplotlib.pyplot as plot  # data visualization, creating plots and charts
import seaborn  # built on top of mathplotlib, enhances it, works well with pandas
from . import AnalysisBase

## Self-note:
## Compared to C#, we can use *stateful interface* of libraries Matplotlib and Seaborn
## This means we can just code in fluent-style, without assigning return values
## of every call to an object. Mutations will implicitly be done on the objects,
## and states will carry on.

class PowerLevelsAnalysis(AnalysisBase):
    def average_power_level_analysis(self):        
        # Count the unique generations, we'll create a loop
        unique_generations = self.data_frame["Generation"].nunique()
        
        # Loop through each generation + 1 (0 for all generations)
        for gen in range(unique_generations + 1):
            if gen == 0:
                gen_data = self.data_frame
                title = "All Generations"
                filename = "all.png"
            else:
                gen_data = self.data_frame[self.data_frame["Generation"] == gen]
                title = f"Generation {gen}"
                filename = f"gen{gen}.png"
            
            # Plot setup
            figure, axe = plot.subplots(figsize=(8, 2))
            ## A figureure is the container for a plot (chart).
            ## 8, 2 are width and height of the plot in inches.

            # Calculate the median power level for each type and sort descending
            type_order = gen_data.groupby("Type 1")["Total"].median().sort_values(ascending=False).index
            seaborn.boxplot(
                x="Type 1",
                y="Total",
                hue="Type 1",
                data=gen_data,
                order=type_order,
                palette=constants.type_palette,
                showfliers=False,
                legend=False,
                ax=axe
            )
            axe.set_title(f"Power Level Distribution by Pokemon Type ({title})")
            axe.set_xlabel("Primary Type")
            axe.set_ylabel("Power Level (Total)")
            axe.set_xticks(axe.get_xticks())
            axe.set_xticklabels(axe.get_xticklabels(), rotation=45)
            
            self.plots.append((self.output_directory / "avg_power" / filename, figure))
        
        return self

    def total_power_comparision_per_generation(self):
        total_powers_per_generation = self.data_frame.groupby("Generation")["Total"].sum().reset_index()

        figure = plot.figure(figsize=(10, 2))
        seaborn.lineplot(
            data=total_powers_per_generation,
            x="Generation",
            y="Total",
            marker="o"
        )
    
        plot.title("Total Power Comparison per Generation")
        plot.xlabel("Generation")
        plot.ylabel("Total Power")

        # Define the output path
        output_path = self.output_directory / "total_power" / "per_generation.png"
        
        # Return the plot with its path in a list of tuples
        self.plots = [(output_path, figure)]
        
        return self