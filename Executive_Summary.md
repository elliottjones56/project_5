# **EXECUTIVE SUMMARY**
This project has sought to analyze the similarities between United States Incarceration Rates and those of Latin American countries:
         -Brazil
         -El Salvador
         -Honduras
         -Mexico

In addition this project has compared classification, and regression models which attempt to predict a country's/state's democracy index based on incarceration rates alone; and then compare those results to a model utilizing various political and economic indicators, in addition to incarceration rate, to predict the democracy index. 

## Data Science & Machine Learning Process

###  Data Acquisition an Exploratory Data Analysis
We have chosen to limit our Exploratory data analysis to years starting in 2010, as this reflects the state of the global economy post the 2008 global economic crisis as well as the changes brought upon by the pandemic. 

Also, by not going too far in time, we avoid comparing between time periods which have very different data availability and potentially incomparable terms of civil and human rights. 

Challenges to the data acquisition process: 

By nature, reports of incarceration rates for countries with high corruption levels should be considered rough estimates. 

This is why we chose to utilize data from the United Nations as our main source for incarceration as they have a long history of addressing challenges with untrustworthy data sources[(source)]('../../Research/UNSQAF-2018.pdf')

In addition, when modeling to predict democracy index, we have chosen to include data from independent organizations such as: 

- [The Quality of Government Institute](https://www.gu.se/en/quality-government)

- [The Freedom House Project](https://freedomhouse.org/)

- [The Economist Intelligence Unit](https://www.eiu.com/n/)

### Model Performance

We first approached the problem with a classification approach: 

The best classification model was a Support Vector Model, with a training R2 of
 .317 and a testing R2 of . 345 
 
The baseline classification distribution is as follows: 

-Authoritarian Regime 0.32
-Flawed Democracy 0.32
-Hibrid Regime 0.22
-Full Democracy 0.14

Based on these results our team then decided to test a regression model next. 

A simple decision tree model predicting democracy index using incarceration rates for 158 countries yielded a train accuracy score of 0.72 and a test accuracy score of .70. 

This is the model accuracy we have chosen to compared to a regression model using 30+ political and economic indicators from the following sources: 

- [Social Progress Imperative](https://www.socialprogress.org/)
- [Varieties fo Democracy](https://v-dem.net/)
- [United Nations Development Programme](https://www.undp.org/)
- [World Economic Forum](https://www.weforum.org/about/world-economic-forum)
- [Institute for Economics and Peace](https://www.economicsandpeace.org/)
- [World Bank Group](https://www.worldbank.org/en/home)
- [Amnesty International](https://www.amnestyusa.org/about-us/)

This model was trained with data from 35 countries and has a training accuracy of .99 and a testing accuracy of .96

Based on our results we believe that incarceration rate is a robust indicator of the state of governance. 

## Correlation Insights form Random Forest Model 

### Correlations with Incarceration Rate:

[Institute for Economics & Peace](https://www.visionofhumanity.org/resources/)
         
Global Peace Index (1-5) 0.52 correlation

Safety and Security (1-5) 0.42 correlation

[The World Bank Group Collection of Development Indicators](https://databank.worldbank.org/source/world-development-indicators)

International Female Homicide (rate per 100,000), 0.42 correlation 

[The Freedom House Report](https://freedomhouse.org/sites/default/files/2023-03/FIW_World_2023_DigtalPDF.pdf)
         
Civil Liberties Aggregate (0-40) 0.52 correlation

Political Rights Aggregate (0-60) 0.42 correlation

[Amnesty International](https://www.politicalterrorscale.org/)
         
Political Terror Scale (1-5) 0.39 correlation

[Social Progress Imperative](https://www.socialprogress.org/static/8a62f3f612c8d40b09b3103a70bdacab/2022%20Social%20Progress%20Index%20Executive%20Summary_4.pdf)
         
Basic Human Needs (0-100) 0.039 correlation
         
Foundations of Wellbeing (0-100) -0.41 correlation


### Correlations with Democracy Index:

[Social Progress Imperative](https://www.socialprogress.org/static/8a62f3f612c8d40b09b3103a70bdacab/2022%20Social%20Progress%20Index%20Executive%20Summary_4.pdf)

Opportunity Index (0-100) 0.83 correlation

Foundations of Wellbeing (0-100) 0.77 correlation 

[Varieties of Democracy (V-Dem) Project](https://v-dem.net/en/data/)
         
Legislature Corrupt Activities (0-4) 0.82 correlation

Judicial Corruption Decisions (0-4) 0.76 correlation

[United Nations Development Program](https://hdr.undp.org/system/files/documents/global-report-document/hdr2021-22pdf_1.pdf)

Human Development Index (0-1) 0.78 correlation 

[World Economic Forum](https://www.weforum.org/reports/global-gender-gap-report-2022/)

Overall Global Gender Gap Index (0-100) 0.67 correlation

[Institute for Economics & Peace](https://www.visionofhumanity.org/resources/)

Ongoing Conflict  (1-5) -0.57 correlation

Safety and Security (1-5) -0.70 correlation

---
# **CONCLUSIONS & RECOMMENDATIONS**

Looking at the history of Latin America it is undeniable that authoritarian regimes have taken root there often due to United States cold war foreign policy. These authoritarian regimes have taken notes from the United States own incarceration policy, which has a background rooted in targeting black men escaped from enslavement in the 13th amendment, furthered into attacking those same groups during the civil rights and war on drugs movement to put young black men in prison. Preventing them from voting or shifting policy towards communist and leftist ideals. Latin America’s authoritarian leadership tends to follow America’s authoritarian policies to apply to their own people. Strategies developed by the CIA and American administrations as civil oppression tools have proved excellent tools for foreign dictators. So as America has used incarceration as a tool to attack leftist and democratic ideals like markers listed in the democracy index, we find those same metrics (lack of democracy, young male prison populations, and imprisonment of political enemies) reflected onto latin american authoritarian regimes. While America receives an acceptable democracy index score of 7.85/10 from the international community, the Latin American countries America exported these policies to feel the effects of these policies on their score. El Salvador with its martial law since 2022 lower than 4, Brazil with its failing trust in government with a 6, and Mexico with its drug cartels with a 6.5. If you peel away the overall democracy score of the United States and look only at the reality of who’s in prison the real democracy index of the United States comes to light at a predicted 5.5, with many States even lower than that.


---
# CITATIONS
1) [Support for Tough on Crime Policies in El Salvador, Honduras and Mexico]('../../Research/Tough-On-Crime-Policies-in-El-Salvador-Mexico-Honduras-2020.pdf')

2) [An Overview of Democracy Crisis in El Salvador]('../../Research/TheDemocracyCrisisinElSalvador-AnOverview.pdf')

3) [Edge of Democracy Documentary: The Rise of Authoritarianism in Brazil](https://www.youtube.com/watch?v=80xUTDbj7QM)

4) [The Freedom House Project 2021 Report]('../../Research/FIW2021_World_02252021_FINAL-web-upload.pdf')

5) [Laboratories of Democratic Backsliding]('../../Research/laboratories-of-democratic-backsliding.pdf')

6) [United Nations Office on Drugs and Crime Report 2021]('../../Research/DataMatters_prison.pdf')

7) [The Economist Intelligence Unit: Democracy Index Report 2022](https://www.eiu.com/n/campaigns/democracy-index-2022/)

8) [Authoritarianism & Confinement in the Americas]('../../Research/ASSISTED_FREEDOM_CARCERAL_TRANSMUTATION.pdf')

9) [The U.S. War on Drugs in Latin America: What is the Method to the Maddness?]('../../Research/The%20U.S.%20War%20on%20Drugs%20in%20Latin%20America%20What%20is%20the%20Method%20to%20the.pdf')

10) [Artistas del diseño: Mexican Drug Cartels? (A report by the School of Advanced Military Studies: U.S. Army Command and General Staff College)]('../../Research/AD1160921.pdf')

11) [Incarceration as a Political Institution]('../../Research/Shannon_Uggen_BW_10.pdf')

12) [The Quality of Government Institute OECD Codebook]('../../Research/codebook_oecd_jan23.pdf')

13) [Brazilian Democracy in the Aftermath of January 8th]('../../Research/EPRS_BRI(2023)739354_EN.pdf')

14) [Castigos irracionales: Leyes de drogas y encarcelamiento en América Latina ("Irrational Punishments: Laws on Drugs and Incarceration in Latin America")]('../../Research/folleto_cide_castigos_irracionales_v15_full.pdf')
