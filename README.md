# Fire_Prediction

The Fire Prediction Project utilizes data from two main sources: [Oregon Open Data Portal](https://data.oregon.gov/Natural-Resources/ODF-Fire-Occurrence-Data-2000-2022/fbwv-q84y/about_data), [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api). The fire data consists of thousands of records between 2000 and 2022, where the most recent 2000 are utilized for model building. These 2000 records are joined with associated weather data, and an additional 2000 records are retrieved from the weather API for non-fire records. 

The focus of the project is predicting whether certain environmental and weather conditions are probable to lead to a fire ignition. With the focus of the model being probability of ignition, the severity classifications for each fire (A - G) are converted to a singular numeric indicator (class 1). In the final section of the project, weather variables are declared and the model is tested against general domain knowledge for which conditions lead to fires.

## Weather Features

The weather features utilized for the model are as follows: 

| Feature |       Rate        | Units  |     Definition    |
|:-------:|:-----------------:|:------:|:-----------------:|
| Soil Moisture | Hourly | m³/m³ |The average soil water content as volumetric mixing ratio at 0-7 cm. |
| Surface Pressure | Hourly | hPa | Atmospheric air pressure, which usually decreases with increasing elevation|
| Dew Point | Hourly | °F | Dew point temperature (temperature at which air becomes saturated with water vapor) at 2 meters above ground | 
| Apparent Temperature | Hourly | °F | Apparent temperature is the perceived feels-like temperature combining wind chill factor, relative humidity and solar radiation |
| Precipitation | Hourly | in | Total precipitation (rain, showers, snow) sum of the preceding hour. Data is stored with a 0.1 mm precision |
| Wind Speed Max | Daily | mph | Maximum wind speed on a day |
| Reference Evapotranspiration | Daily | mm | Daily sum of ET₀ Reference Evapotranspiration (the process by which water is transferred from the land to the atmosphere by evaporation) of a well watered grass field |
| Temperature Max | Daily | °F | Maximum daily air temperature at 2 meters above ground |
| Temperature Min | Daily | °F | Minimum daily air temperature at 2 meters above ground |


## Step by Step Overview:

More details are provided within the .ipynb script - the flow of the project is generalized below:

1. Imports and installs

2. Data Extraction

    The fire data is in a csv format previously exported from the Oregon Open Data Portal. The weather API data is called iteratively through a loop. There are multiple variables at the hourly and daily level. The fire data was right-sized to be joined with the associated weather data. 
    
    An additional loop was used to call more weather data that is not associated with fires. 

3. Aggregations, Conversions, Cleanup

    In order to create a singular dataframe that can be used for training and testing, several data type conversions, dataframe adjustments, and aggregations are performed. 

4. Feature Visualization

    A correlation heatmap provides easy and quick insights into which features have impacts on fire ignition. 

5. Modeling, Training, Testing

    A RandomForestClassifier is instantiated and the hyperparameters tuned with a GridSearch. The models f1 score is evaluated and associated precision/recall displayed. 

6. Prediction

    Weather variables are declared and the model is used to predict the probability of fire ignition.

## Usage

The bulk of the project is within an .ipynb file to provide insight into model results and visualizations. ***Directory: Fire_Prediction/fire/Fire_Prediction.ipynb***

To get started, first clone the repository. This will download a copy of the repository in your current working directory. 

```python
$ git clone https://github.com/cgp9900/Fire_Prediction.git
```
