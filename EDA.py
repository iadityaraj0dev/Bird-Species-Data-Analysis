import pandas as pd
df=pd.read_csv("cleaned_bird_data.csv")
#Temporal trend
#Seasonal Trend analysis
# df['Date'] = pd.to_datetime(df['Date'])
# df['Year_extracted'] = df['Date'].dt.year
# df['Month_extracted'] = df['Date'].dt.month
# #Year wise Sighting
# df['Year_extracted'].value_counts().sort_index()
# #Month wise Sighting
# df['Month_extracted'].value_counts().sort_index()

##observation 1
# Bird activity is highest in early monsoon (June)
# Slight decline afterward → could be due to:
# migration completion
# weather changes

#Observation Time
# df['Start_Time']= pd.to_datetime(df['Start_Time'],format="%H:%M:%S")
# df['hour']=df['Start_Time'].dt.hour
# print(df['hour'].value_counts().sort_index())

#Observation 2 
#Bird activity peaks around 7 AM, with slightly lower but still high activity at 6 AM and 8 AM. This indicates that early morning hours (6–8 AM) represent the most active period for bird sightings.

#Spatial Analysis
#Location Insights
#hotspot = df.groupby('Location_Type').size().sort_values(ascending=False)
#print(hotspot)

#observation 3 
#the forest has the highest number of sightings indicates the most active or species-rich habitat.

#Plot level Analysis
# print("Top Plot by Activity")
# plot_activity = df.groupby('Plot_Name').size().sort_values(ascending=False)
# print(plot_activity.head(10))

# print("Top Plot by Species")
# plot_biodiversity = (
#     df.groupby('Plot_Name')['Common_Name']
#       .nunique()
#       .sort_values(ascending=False)
# )
# print(plot_biodiversity.head(10))

# print("Top Species per Plot")
# top_plots = plot_activity.head(5).index

# species_in_top_plots = (
#     df[df['Plot_Name'].isin(top_plots)]
#     .groupby(['Plot_Name', 'Common_Name'])
#     .size()
#     .reset_index(name='count')
#     .sort_values(['Plot_Name', 'count'], ascending=[True, False])
# )

# # # top 3 species per plot
# top3_per_plot = species_in_top_plots.groupby('Plot_Name').head(3)
# print(top3_per_plot)

#observation 4
# plot-level analysis shows that (top plots by activity) record the highest number of observations, indicating frequent bird activity. In contrast, (top plots by biodiversity) host the greatest number of unique species, indicating richer biodiversity. Dominant species in high-activity plots include (top species per plot), suggesting habitat preference and localized ecological patterns.

#Species Analysis 
# Total unique species
# total_species = df['Scientific_Name'].nunique()
# print("Total unique species:", total_species)

# # Species distribution across location types
# species_distribution = (
#     df.groupby('Location_Type')['Scientific_Name']
#     .nunique()
#     .reset_index(name='Unique_Species_Count')
# )

# print(species_distribution)
# Activity=df['ID_Method'].value_counts().sort_values(ascending=False)
# print(Activity)

#observation 
# singing is the most common activity

#Male-to-Female Ratio
# # 1. Keep only valid sex values
# df_filtered = df[df['Sex'].isin(['Male', 'Female'])]

# # 2. Count Male vs Female per species
# species_sex = (
#     df_filtered
#     .groupby(['Common_Name', 'Sex'])
#     .size()
#     .unstack(fill_value=0)
# )

# # 3. Add total count
# species_sex['Total'] = species_sex.sum(axis=1)

# # 4. Add Male-to-Female ratio
# species_sex['Male_to_Female_Ratio'] = (
#     species_sex['Male'] / (species_sex['Female'] + 1)
# )

# # 5. Sort by total observations
# species_sex = species_sex.sort_values(by='Male_to_Female_Ratio', ascending=False)

# # Final result
# print(species_sex.head(10))

#Environmental Conditition
# df['Temp_Bin'] = pd.cut(df['Temperature'], bins=5)
# df['Humidity_Bin'] = pd.cut(df['Humidity'], bins=5)

# df.groupby('Humidity_Bin').size()
# df.groupby('Temp_Bin').size()
# temp_analysis = df.groupby('Temp_Bin').size().reset_index(name='count')
# humidity_analysis = df.groupby('Humidity_Bin').size().reset_index(name='count')

# print(temp_analysis)
# print(humidity_analysis)
# df['Distance'] = pd.to_numeric(df['Distance'], errors='coerce')
# df['Temp_Bin'] = pd.cut(df['Temperature'], bins=5)

# temp_distance = (
#     df.groupby('Temp_Bin')['Distance']
#       .mean()
#       .sort_index()
# )

# print(temp_distance)

# print(df.groupby('Sky').size().sort_index())
# print(df.groupby('Wind').size().sort_index())
#Observation
# Bird activity is highest within the temperature range of 21–26°C, followed by 16–21°C, indicating that moderate temperatures favor bird activity.

# Similarly, activity peaks at humidity levels between 62–80.5%, with slightly lower activity at 80.5–98.8%, suggesting that moderate to high humidity supports bird presence.

# Bird sightings are more frequent under clear or partly cloudy (few clouds) sky conditions, indicating better visibility and favorable environmental conditions.

# In terms of wind, activity is highest at light air movement (1–3 mph smoke drift), followed by calm conditions, suggesting that slight wind may support bird movement while strong winds are unfavorable. 
#Disturbance effect on Bird sight 
# disturbance_activity = (
#     df.groupby('Disturbance')
#       .size()
#       .sort_values(ascending=False)
# )

# print(disturbance_activity)
#observation 
#Bird sightings are highest under no disturbance conditions, followed by slight disturbance, while moderate and serious disturbances significantly reduce observations.

#How many species at each distance
# observer_distance = (
#     df.groupby('Distance')['Common_Name']
#       .nunique()
# )
# print(observer_distance)
#observation 
# most species observed from 50-100 meter distance followed by <=50 meter.

#Flyover Frequency
# print(df.groupby('Flyover_Observed').size().sort_values(ascending=False))
#Observer Bias 
# Observer_bias= df.groupby('Observer').size().sort_values()
# print(Observer_bias)
#Elizabeth Oswald is the observer who reported highest followed by Kimberly serno and Brian Swimela
# observer_species = (
#     df.groupby('Observer')['Common_Name']
#       .unique()
# )

# print(observer_species)
# Visit patterns
# Species diversity per visit + cumulative growth

# visit_analysis = (
#     df.groupby('Visit')['Common_Name']
#       .nunique()
#       .reset_index(name='Species_Count')
#       .sort_values('Visit')
# )

# # observation count per visit
# visit_analysis['Observation_Count'] = df.groupby('Visit').size().values

# # cumulative unique species (overall diversity growth)
# visit_analysis['Cumulative_Species'] = (
#     df.sort_values('Visit')['Common_Name']
#       .drop_duplicates()
#       .groupby(df['Visit'])
#       .count()
#       .cumsum()
#       .values
# )

# print(visit_analysis)
# observation
# The first visit recorded the highest number of species (118), capturing the majority of biodiversity. In subsequent visits, the number of newly observed species decreases (99 in visit 2 and 74 in visit 3), indicating diminishing returns. Although cumulative species count increases slightly (from 118 to 126), the rate of new species discovery is significantly reduced after the first visit.

#Conservational Insights 
# pif_status = df['PIF_Watchlist_Status'].value_counts()
# regional_status = df['Regional_Stewardship_Status'].value_counts()

# print("PIF:\n", pif_status)
# print("\nRegional:\n", regional_status)
# at_risk_species = (
#     df[df['PIF_Watchlist_Status'] == True]
#     .groupby('Common_Name')
#     .size()
#     .sort_values(ascending=False)
# )
# print('At Risk Species')
# print(at_risk_species.head(10))
# combined_priority = (
#     df.groupby(['PIF_Watchlist_Status', 'Regional_Stewardship_Status'])
#       .size()
# )

# print(combined_priority)
# #A subset of species falls under conservation priority, as indicated by True values in PIF Watchlist and Regional Stewardship Status. Species marked True in both categories represent the highest conservation concern and should be prioritized for monitoring and protection.
# #Key insight
# # False, False → low concern
# # True, False → globally important
# # False, True → regionally important
# # True, True → highest priority
# 1. Count observations per AOU_Code
# aou_counts = (
#     df.groupby('AOU_Code')
#       .size()
#       .sort_values(ascending=False)
# )

# # 2. AOU_Code vs conservation priority
# aou_priority = (
#     df.groupby('AOU_Code')[['PIF_Watchlist_Status', 'Regional_Stewardship_Status']]
#       .max()
# )

# # 3. High-priority species (both True)
# high_priority_aou = aou_priority[
#     (aou_priority['PIF_Watchlist_Status'] == True) &
#     (aou_priority['Regional_Stewardship_Status'] == True)
# ]

# # 4. Combine with observation count
# final_analysis = aou_priority.copy()
# final_analysis['Observation_Count'] = aou_counts

# # 5. Output
# print("Top AOU Codes by Observations:")
# print(final_analysis.sort_values(by='Observation_Count', ascending=False).head(10))

# print("\nHigh Priority Species (Both True):")
# print(high_priority_aou)
#Observation
# Analysis using AOU codes shows that the most frequently observed species are not necessarily conservation priorities, as they are largely not flagged under PIF Watchlist or Regional Stewardship Status. In contrast, a smaller group of species (e.g., KEWA, PRAW, WEWA, WOTH) are identified as high-priority conservation targets, despite not being among the most frequently observed. This indicates that conservation concern is not directly linked to observation frequency, and less frequently observed species may require greater attention and protection.
#Therefore, conservation efforts should prioritize species flagged under both PIF Watchlist and Regional Stewardship Status, even if their observation counts are relatively low.