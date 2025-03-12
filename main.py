import statsmodels.api as sm
import numpy as np
import pandas as pd
import math

def moving_mean(values,p):
    means=[]
    for x in range(len(values)): 
            if x<=(len(values)-p):
                mean=sum(values[x:x+p])/p
                
                means.append(mean)
    return means

def regression(X,y):
    X=np.array(X)
    X=pd.DataFrame({'Intercept':np.ones(X.shape[0]),'X':X})
    y=np.array(y)

    model=sm.OLS(y,X.values).fit()  
    return model
    
def get_levels(t,a,b):
    l_0=a-(2*b)
    levels=[]
    for x in range(t):
        l_t=l_0+(x*b)
        l_t=f"{l_t:.2f}"
        levels.append(float(l_t))
    return levels
    
def get_seasonality(Dt,Lt):
    Lt=Lt[1:]
    seasonalities=[]
    for x in range(len(Dt)):
        s=Dt[x]/Lt[x]
        s=f"{s:.4f}"
        seasonalities.append(float(s))
    return seasonalities

def get_next_seasonality(S):
    S_next=[[S[0],S[4],S[8]],[S[1],S[5],S[9]],[S[2],S[6],S[10]]] #if needed, add lists of seasonality points to add
    future_seasonalities=[]
    for x in range(len(S_next)):
        f_s=(sum(S_next[x])/len(S_next[x]))
        f_s=f"{f_s:.4f}"
        future_seasonalities.append(float(f_s))
    return future_seasonalities

def get_forecast(t,Lt,Tt,St):
    n=4
    forecasts=[]
    for x in range(n):
        f_t1=(Lt[t+x]+Tt[t+x])*St[t+x+1]
        f_t1=f"{f_t1:.4f}"
        forecasts.append(float(f_t1))
    return forecasts

def static_method(values,p,t):
    means=moving_mean(values,p)
    print(f"Media mobile dei valori: {means}\n")
    if p%2==0: #se p è pari facciamo la media mobile doppia
        double_moving_mean=moving_mean(means,2)
        print(f"Doppia media mobile: {double_moving_mean}\n")
        X=[x for x in range(1,len(double_moving_mean)+1)]
        model=regression(X,double_moving_mean)
        print(f"Intercept: {model.params[0]:.2f}\nSlope: {model.params[1]:.2f}")

    else:      #se p è dispari direttamente la regressione lineare
        X=[x for x in range(1,len(means)+1)]
        model=regression(X,means)
        print(f"Intercept: {model.params[0]:.2f}\nSlope: {model.params[1]:.2f}")
    
    levels=get_levels(t,model.params[0],model.params[1])
    print(f"\nLevels: {levels}")

    seasonalities=get_seasonality(values,levels)
    print(f"\nSeasonalities: {seasonalities}")

    new_seasonalities=get_next_seasonality(seasonalities)
    print(f"Seasonalities from S{len(seasonalities)+1} to S{len(seasonalities)+len(new_seasonalities)}: {new_seasonalities}")
    for x in new_seasonalities:
        seasonalities.append(x)
        print(f"\nNew Seasonalities: {seasonalities}")


def record(data,alpha,last_level,l):
    return (alpha*data[l])+((1-alpha)*last_level)

def Brown_method(data,n): #n is the (given) number of intervals to initialize the method
    levels=[0 for x in range(n-1)]
    forecasts=[0 for x in range(n)]
    last_level=np.average(data[0:n])
    levels.append(last_level)
    alpha=0.3
    for x in range(len(data)-n):
        forecasts.append(round(levels[-1]))
        new_level=record(data,alpha,levels[-1],len(levels))
        levels.append(new_level)
    print(f"Levels: {Brown_method(Data,6)[0]}")
    print(f"\nForecasts: {Brown_method(Data,6)[1]}")
    
def Holt_method(data,n,alpha,beta):
    data_1=data[0:5]
    model=regression([x for x in range(1,len(data_1)+1)],data_1)
    print(model.params[0])
    a=round(model.params[0],2)
    b=round(model.params[1],2)
    levels=[0 for x in range(n+1)]
    levels[0]=a
    last_level=a+(n*b)
    levels.append(last_level)
    trends=[b]
    forecasts=[]
    for x in range(n,len(data)):
        forecast=levels[-1]+trends[-1]
        forecasts.append(forecast)
        new_level=(alpha*data[x])+(1-alpha)*forecast
        levels.append(new_level)
        new_trend=(beta*(levels[-1]-levels[-2])+(1-beta)*trends[-1])
        trends.append(new_trend)
    forecasts.append(levels[-1]+trends[-1])
    print(f"Forecasts: {forecasts}")
    print(f"\nLevels: {levels}")
    print(f"\nTrends: {trends}")

