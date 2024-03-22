import pandas as pd
import plotly.express as px
from .mdrHandler import mdrClient
from .helpers import translate_column


class M5_vis:
    """
    Data Visulations on M5 Metadata
    """

    def __init__(self, m5_data):
        self.m5 = m5_data    

    def bar_chart(self):
        """
        Bar plot to visualise all elements included in M5 dictionary
        data: M5 dict extraction
        path: were to store the resulted bar plot figure
        """
    
        #m5 = self.m5
        ## preprocessing

        # cleaning
        self.m5.loc[self.m5['dataType'] == 'STRING','element'] = 'Genetik'
        self.m5['element'] = self.m5['element'].str.replace('_', ' ')
    
        # preparing
        vis_dat = self.m5.groupby(['element', 'conceptType']).size()
        vis_dat = vis_dat.to_frame(name = 'count').reset_index()
        vis_dat = vis_dat.loc[(vis_dat["count"] > 10)] # exclude elements with small occurrence expressions
        vis_dat = translate_column(vis_dat, 'element')

        # eclude all standard mapping approaches 
        std_map = ["Surgery: OPS", "ICD10GM", "ICDO3"]
        vis_dat = vis_dat[~vis_dat['element'].isin(std_map)]
   

        # visualize
        fig = px.bar(vis_dat,
            y='en_element',
            x='count',
            color='conceptType',
            color_discrete_sequence= px.colors.qualitative.Pastel2,
            text_auto=True
            )

        fig.write_image('C:/Users/jac/ukebox3/UCCH_IT/Publikationen/MDR/Visualisation/bar_plot.png')
        #(f"{path}\bar_plot.png")
    
        return fig.show()
