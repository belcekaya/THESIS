# **MASTER THESIS** - Deep Learning Models to Predict the Traffic Intensity in Madrid City 

## Brief Introduction

As the human population in the world increases and technology develops, the increase in car usage has witnessed a sharp rise from the past to the present. Therefore, nowadays, due to this increase, traffic has become one of the most important problems in urbanized settlements. For more livable city life, it is necessary to control vehicle traffic by determining the current density and taking the necessary measures for future congestion. To reduce the time spent in traffic, various applications have been developed that show people the fastest and most comfortable route from one point to another. Although these applications are suitable for short-term traffic congestion estimation in the traffic flow, the aim of this thesis is to provide a different approach to forecasting the traffic intensity on a regional basis by using sensor data from the sensors placed in URB and M30 road types in 21 districts of Madrid. Sensor data and zone areas of each sensor were obtained from the Madrid open data portal. 

![image](https://github.com/belcekaya/master_thesis/assets/58460284/c2938271-ad69-4beb-867f-3c74702d7894)

In this paper, first, the related works similar to this problem have been studied and the approaches of these studies have been placed in the literature review part.

![image](https://github.com/belcekaya/master_thesis/assets/58460284/9be742a8-82fb-4758-81e0-be47e5ece659)

![image](https://github.com/belcekaya/master_thesis/assets/58460284/d0017210-cb84-4b6b-9098-a7f9e0e8f721)

After broad research, the success of Convolutional neural networks (CNN) and Long-short term Memory (LSTM) which is a special type of recurrent neural network (RNN) has been witnessed in the state of the art. In the proposed model, CNN and LSTM model combinations have been implemented in sequence to sequence modeling approach. 

![image](https://github.com/belcekaya/master_thesis/assets/58460284/3b87512a-eabb-4e5c-ae65-736f75927bd6)


Before training the models, the sensor and zone data have been analyzed in detail and various data manipulations have been made to prepare the data for deep learning models. 

Apart from numeric sensor data, another experiment has been made with the traffic intensity map images. The images have been produced by using the geographical information in the sensor data set. First, the pre-processed numeric data has been trained with 24-minute time steps which correspond to a 6-hour period and the regional traffic intensity has been estimated for the next 4 time steps which equate to a 1-hour period. Then as a second experiment, the regional traffic intensity images have been forecasted with the same defined looking back and forecasting time step periods. This experiment has proved that the deep learning models learning capability showed a good forecasting performance and the models could learn the 15-minute interval traffic intensity flow from the images produced. The final results have shown that even though the experiment of training the model with traffic intensity images could perform more than the baseline model and could learn the traffic intensity flow information, the models’ performance with the numerical data has over-performed.
