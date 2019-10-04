#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:41:55 2019

@author: gather3
"""

from Scrapper.NFL import NFLScrapper
import pandas as pd
import plotly.express as px


class DataPreprocessor():
    
    def __init__(self, data):
        self.data = data
        

# =============================================================================
# # Clean the data
# =============================================================================
    def dataClean(self):
        for df in self.data:
            df.drop(columns = [df.columns[0], 'Year'], axis = 1, inplace = True)
    #print(df)

# =============================================================================
# # Create plotly functions to generate the graphs
# =============================================================================

# General plot
    def plot_all(self, function, x_label,y_label, color,  *args, **kwargs ):
        try:
            for df in self.data:
                self.__plot(df,function, x_label,y_label, color,  *args, **kwargs)
        except ValueError as e:
            print(e)
            print(f'Showing only the ones that mathces the requirement')
            pass
    
    def __plot(self, df, function, x_label,y_label, color = 'Team',  *args, **kwargs):
        fig = function(df, x= x_label, y = y_label, color = color, 
                       hover_data = list(args),labels = kwargs)
        fig.show()
        
    def plotByIndex(self, index, function, x_label,y_label, color,  *args, **kwargs):
        self.__plot(self.data[index], function, x_label,y_label, color,  *args, **kwargs)
# =============================================================================
# # Create a database
# =============================================================================

if(__name__ == "__main__"):
    
    passing =  NFLScrapper(initial_year = 2019, final_year = 2019, attribute = 'Passing')
    rushing =  NFLScrapper(initial_year = 2019, final_year = 2019, attribute = 'Rushing')
    receiving =  NFLScrapper(initial_year = 2019, final_year = 2019, attribute = 'Receiving')

    dataframes = [passing.getNFLData() , rushing.getNFLData() ,receiving.getNFLData()]
    
    dpp = DataPreprocessor(dataframes)
    dpp.dataClean()
    dpp.plot_all(px.bar, 'Player', 'Yds', 'Avg', 'Pos', 'TD', Player_name = "Player", Yards = "Yds")
    dpp.plotByIndex(0,px.bar, 'Player', 'Yds', 'Avg', 'Pos', 'TD', Player_name = "Player", Yards = "Yds")
#    plot(data, px.bar, 'Player', 'Yds', 'Int', 'Att', 'Pct', 'Rate',
#         Player_name = "Player", Yards = "Yds")
    
