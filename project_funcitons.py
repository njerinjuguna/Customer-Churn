import seaborn as sns
import matplotlib.pyplot as plt

class UnivariateAnalysis:

  def __init__(self, df):
    self.df = df

  def plot_distribution(self, variable_name, column_name):
   
    g = sns.FacetGrid(self.df, col="churn")
    g.map(plt.hist, column_name)
    plt.xlabel(column_name)
    plt.ylabel("Count")
    plt.show()

