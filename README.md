
# **Incarceration Rates As A Measure of Governance: The United States vs. Latin America**
# **By Brandon Amarasingam, Elliot Jones, and Lorena Robles**

> ## PROBLEM STATEMENT
> ### What are the similarities between the United States incarceration rates and Latin American countries under civil unrest/authoritarian movements as it relates to  age and gender? 
---
> ## PROJECT OVERVIEW
>
> ####  According to the **Freedom House Project**-America's oldest organization defending democracy in the world- we are living in the midst of a growing global trend of democratic decline and rising authoritarianism. " Fewer than a fifth of the world's population now live in fully free countries [(source)]((https://www.google.com/search?channel=ftr&client=firefox-b-1-d&q=what+is+the+freedom+house+project%3F&dlnr=1&sei=qlwfZYGKNfHm0PEPrOKA2A4))."
>
> #### This data science project seeks to draw parallels in the trends of incarceration, by age and gender, across Brazil, El Salvador, Honduras, Mexico and the United States as they relate to the State of governance.
>
> #### We have chosen these countries for our analysis because of the deep connections they have with United States historic political trends and/or political cultural parallels that have become apparent in recent years. Most notably: 
> #### &ensp;&thinsp;-The attacks on the presidential palace in Brasilia on January 8th, 2023 by supporters of former Brazilian president Jair Bolsonaro, which were directly inspired by the January, 6th 2021 U.S Capitol attacks . Leaders of this movement have effectively sown doubt of the legitimacy of the electoral process [(source)](/elliottjones56/project_5_group_work/blob/main/Research/EPRS_BRI(2023)739354_EN.pdf).     
> #### &ensp;&thinsp;-The deeply rooted and devastating effects of the "War on Drugs," first declared by Richard Nixon in 1973 and which was swiftly adopted by Latin American authorities with the political and economic influence of the U.S. As a results of this conflict organized crime (Drug Cartels) have evolved to become as sophisticated as the most advanced military operations ever designed against them by U.S. Military/Intelligence agencies.  [(source)](/elliottjones56/project_5_group_work/blob/main/Research/AD1160921.pdf)
> #### &ensp;&thinsp;-El Salvador, Honduras & Mexico are home to some of the most violent cities in the world. Drug Cartels in these regions have evolved to mimic sate behaviors controlling territory public/private institutions, imposing taxes, redlining and forcing civic loyalty through terror and intimidation.According to the Latin American Public Opinion Project, approval for national military control was at an all time high as of the end of 2021 [(source)](/elliottjones56/project_5_group_work/blob/main/Research/Tough-On-Crime-Policies-in-El-Salvador-Mexico-Honduras-2020.pdf). Fear of becoming a homicide victim was found to be the number one variable correlated to these approval ratings:    
 >#### &ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;-Mexico, 48%,  &ensp;&thinsp;&ensp;&thinsp;-El Salvador,  52% &ensp;&thinsp;&ensp;&thinsp;-Honduras, 64%              
>
> #### "Imprisonment is fundamentally an exercise of power," it is a measure of class/racial struggles, political trends, policy choices, public sentiment and media interpretation [(source)](/elliottjones56/project_5_group_work/blob/main/Research/Shannon_Uggen_BW_10.pdf)." This is why we believe it to be one the strongest indicators on the State of Governance for any nation; and we have chosen it as the main focus for our analysis.  
>
> #### Global incarceration rates continue to grow, 93% of persons detained are men, but the number of women in prison has been increasing at a faster rate. The American continent has the highest incarceration rate of all other global regions, with an average of 379 persons per 100,000 habitants as of the beginning of 2022 [(source)](/elliottjones56/project_5_group_work/blob/main/Research/DataMatters_prison.pdf). 
>
> ### Incarceration Rates (Per 100,000 People) from 2010 to 2021 as reported by the United Nations Office on Drugs  and Crime:
>![PR]('../../Images/Incarceration_rates_all.png')
>
> #### To test our theory we have chosen to train various machine learning algorithms to predict the Democracy Index of multiple nations based on incarceration rates and compared their performance to a robust model which includes multiple governance and economic indicators. Most notable among these indicators are the Freedom House Project's Political Rights and Civil Liberties scores.      
> ### Political Rights Score(0-40) & Civil Liberties Score(0-60) by Country as calculated by the Freedom House Project: 
>![PR]('../../Images/Political_Rights.png')
>![CL]('../../Images/Civil_Liberties.png')
>
>
> #### Please refer to our [Executive Summary](/elliottjones56/project_5_group_work/blob/main/Executive_Summary.md) for the key insights and recommendations of our project. 
---
> ### DATA
> #### This project models the Democracy Index developed by the Economics Intelligence Unit utilizing incarceration data from the United Nations Office on Drugs and Crime, as well governance and economic indicators from the the Quality of Government Institute and the Freedom House Project.    
>
> ### Data Acquisition, Ingestion and Cleaning   
> #### Data Sources:
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1)[The Economist Intelligence Unit: Democracy Index](/elliottjones56/project_5_group_work/blob/main/Datasets/Original_Data/Economist_Intelligence_Unit_Democracy_Index_2022_0-10.csv)
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2)[The Freedom House Project 2021 Report](/elliottjones56/project_5_group_work/blob/main/Datasets/Original_Data/Freedom_House_Project_Aggregate_Scores_2003-2023.csv)
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3)[United Nations Office on Drugs and Crime Report 2021](/elliottjones56/project_5_group_work/blob/main/Datasets/Original_Data/UN_Office_Drugs_Crime_2021_Full_Dataset.csv)
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4)[Elliot's USA STATE DATA SOURCE...]('../../Datasets/Original_Data/') 
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5)[The Quality of Government Institute: Organization for Economic Cooperation & Development(OECD) Dataset](/elliottjones56/project_5_group_work/blob/main/Datasets/Original_Data/Quality_Of_Govt_Inst_OECD_2023.csv)
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6)[United Nation's Person's Held in Prison](/elliottjones56/project_5_group_work/blob/main/Datasets/Original_Data/data_cts_prisons_and_prisoners.xlsx)
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7)[World Population Review Incarceration Rates by Country](/elliottjones56/project_5_group_work/blob/main/Datasets/Original_Data/incarceration-rates-by-country-2023.csv)
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8)[World Population Review Democracy Countries](/elliottjones56/project_5_group_work/blob/main/Datasets/Original_Data/gov_classification_3.csv)
>
> #### These datasets are open source and easily transformed into a Comma Separated Values document with Unicode Transformation Format-8 encoding (which is often the default for use in Pandas/Python). Indicators such as democracy index, incarceration rate, and civil liberties were merged for the modeling process using the country/state name as well as the year. The Freedom House Project and the UN Office on Drugs & Crime dataset had no missing values. The Quality of Government Institute dataset missing values were imputed using skleanr's [KNNImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html) which required standard scaling all the features. 
>
> ### Data Dictionary
> |Feature|Type|Dataset|Description|
> |---|---|---|---|
> |Democracy Index|Float|The Economist Intelligence Unit: Democracy Index|0-10_From Authoritarian Regime to Full Democracy|
> |Incarceration Rate|Integer|United Nations Office on Drugs and Crime Report 2021|National Average/ 100,000 people|
> |Civil Liberties Indicator|Float|The Freedom House Project 2021 Report|0-60_A compilation of freedoms such a freedom of speech and assembly|
> |Political Rights Indicator|Float|The Freedom House Project 2021 Report|0-40_A compilation of rights such as the right to privacy and to vote |
> |gpi_gpi|Float|The Quality of Government Institute OECD Dataset|1-5_Global Peace Index by the Institute of Economics & Peace|
> |gpi_ss|Float|The Quality of Government Institute OECD Dataset|1-5_Safety & Security Index by the Institute of Economics & Peace|
> |gpi_conf|Float|The Quality of Government Institute OECD Dataset|1-5_Ongoing Conflict Index by the Institute of Economics & Peace|
> |wdi_homicidesf|Float|The Quality of Government Institute OECD Dataset|International Female Homicide Rate/ 100,000 people|
> |gd_ptsa|Float|The Quality of Government Institute OECD Dataset|1-5_Amnesty International's Political Terror Scale|
> |spi_bn|Float|The Quality of Government Institute OECD Dataset|0-100_Basic Human Needs Index by the Social Progress Imperative|
> |spi_fob|Float|The Quality of Government Institute OECD Dataset|0-100_Foundations of Wellbeing by the Social Progress Imperative|
> |spi_opp|Float|The Quality of Government Institute OECD Dataset|0-100_Opportunity Index by the Social Progress Imperative|
> |vdem_gcrrpt|Float|The Quality of Government Institute OECD Dataset|0-4_Legislature Corrupt Activties Index by the Varieties of Democracy Project|
> |vdem_jucorrdc|Float|The Quality of Government Institute OECD Dataset|0-4_Judicial Corruption Decisions Index by the Varieties of Democracy Project|
> |undp_hdi|Float|The Quality of Government Institute OECD Dataset|0-1_Human Development Indes by The UN Development Program|
> |gggi_ggi|Float|The Quality of Government Institute OECD Dataset|0-100_Overall Global Gender Gap Index by the World Economic Forum|

---
> ## REQUIREMENTS FOR RUNNING THE CODE
> #### &ensp;&thinsp;- [Python 3.9 or above](https://www.python.org/downloads/)
> #### &ensp;&thinsp;- The following libraries:
> #### &ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;- [NumPY](https://numpy.org/install/go)   - [Pandas](https://pandas.pydata.org/docs/getting_started/install.htmlgo)   - [Matplotlib.pyplot](https://matplotlib.org/stable/users/installing/index.html)
> #### &ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;- [Seaborn](https://seaborn.pydata.org/installing.html)   - [Plotly](https://plotly.com/python/getting-started/g)   - [Streamlit](https://docs.streamlit.io/library/get-started/installation)   - [ScikitLearn](https://scikit-learn.org/stable/install.html)   - [ImbalancedLearn](https://imbalanced-learn.org/stable/index.html)
> #### &ensp;&thinsp;- [Link for running Streamlit App]()
>
---
> ## TABLE OF CONTENTS
> ### &nbsp;&nbsp;A) [Executive Summary](/elliottjones56/project_5_group_work/blob/main/Executive_Summary.md)
> ### &nbsp;&nbsp;B) [Coding_Notebooks](/elliottjones56/project_5_group_work/tree/main/Coding_Notebooks)
>   
> ### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1)[Exploratory_Data_Analysis](/elliottjones56/project_5_group_work/tree/main/Coding_Notebooks/Exploratory_Data_Analysis)   
> ### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2)[Modeling_Process](/elliottjones56/project_5_group_work/tree/main/Coding_Notebooks/Modeling_Process)
> ### &nbsp;&nbsp;C) [Datasets](/elliottjones56/project_5_group_work/tree/main/Datasets)
>    
> ### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1) [Original_Data](/elliottjones56/project_5_group_work/tree/main/Datasets/Original_Data)
> ### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2) [Processed_Data](/elliottjones56/project_5_group_work/tree/main/Datasets/Processed_Data)
> ### &nbsp;&nbsp;D) [Images](/elliottjones56/project_5_group_work/tree/main/Images)
> ### &nbsp;&nbsp;E) [Research](/elliottjones56/project_5_group_work/tree/main/Research)
> ### &nbsp;&nbsp;F) [Presentation](/elliottjones56/project_5_group_work/tree/main/Presentation)
---
> ### CONTACT INFORMATION
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*[Brandon Amarasingam](https://www.linkedin.com/in/brandonamarasingam/)
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*[Elliot Jones](https://www.linkedin.com/in/elliott-jones-w/)
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*[Lorena Robles](https://www.linkedin.com/in/lroblesm/)
