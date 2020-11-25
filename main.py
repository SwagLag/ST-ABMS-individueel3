import numpy as np
import matplotlib.pyplot as plt
from mesa.batchrunner import BatchRunner
from money_model import *

model = MModel(10,10,10)
fixed_params = {"width":10,
                "height":10}
variable_params = {"agent_count": range(10,100,10)}

batch_run = BatchRunner(MModel,
                        variable_params,
                        fixed_params,
                        iterations=10,
                        max_steps=100,
                        model_reporters={"Gini":compute_gini},
                        agent_reporters={"Money":"money",
                                         "Happiness":"happy"})

batch_run.run_all()

agent_counts = np.zeros((model.grid.width,model.grid.height))
for cellinfo in model.grid.coord_iter():
    cell_content, x, y = cellinfo
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count

plt.title("Agent positions")
plt.imshow(agent_counts, interpolation='nearest')
plt.colorbar()
plt.show()

plt.title("Gini plot")
run_data1 = batch_run.get_model_vars_dataframe()
run_data1.head()
plt.scatter(run_data1["agent_count"],run_data1["Gini"])
plt.show()

run_data2 = batch_run.get_agent_vars_dataframe()
plt.title("Frequency agent money values")
plt.hist(run_data2["Money"], bins=range(max(run_data2["Money"])+1))
plt.show()
