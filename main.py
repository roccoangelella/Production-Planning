def linear_regression(x,y):
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")

    n = len(x)
    x_mean = sum(x) / n
    y_mean = sum(y) / n

    # Calculate numerator and denominator for slope (m)
    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean) ** 2 for i in range(n))

    if denominator == 0:
        raise ValueError("Cannot compute slope because variance of x is zero")

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    return intercept, slope

def moving_average(values,p):
    means=[]
    for x in range(len(values)): 
            if x<=(len(values)-p):
                mean=sum(values[x:x+p])/p
                means.append(mean)
    return means

def static_method(Dt,p):
    t=[x+1 for x in range(len(Dt))]
    if p%2==0: #if even p
        means=moving_average(Dt,p)
        print('First moving mean: ',means)
        means=moving_average(means,2)
        print('Second moving mean: ',means)
    else: #if odd p
        means=moving_average(Dt,p)
        print('Moving mean: ',means)
    t_means=[x+1 for x in range(len(means))]
    a,b=linear_regression(t_means,means)
    T=b
    L0=a-(2*b)
    Levels=[L0]
    for x in range(len(Dt)):
        Lt=L0+((x+1)*T)
        Levels.append(Lt)
        
    Seasonalities=[]
    for x in range(len(Dt)):
        St=Dt[x]/Levels[x+1]
        Seasonalities.append(St)
    Homologus_Seasonalities=[]
    for x in range(p):
        curr=x
        curr_seasonalities=[]
        for y in range(len(Seasonalities)//p):
            try:
                curr_seasonalities.append(Seasonalities[curr])
                curr+=(p)
            except:
                continue
        Homologus_Seasonalities.append(curr_seasonalities)

    print(f"\nSeasonalities for Homologus intervals: {Homologus_Seasonalities}\n")

    for x in range(len(Homologus_Seasonalities)):
        Seasonalities.append(sum(Homologus_Seasonalities[x])/len(Homologus_Seasonalities[x]))

    Forecasts=[0 for x in range(len(Dt))]
    for x in range(1,p+1):
        ind=len(Dt)+x
        Ft=(L0+ind*T)*Seasonalities[ind-1]
        Forecasts.append(Ft)
    print('Levels:',Levels,'\n')
    print('Seasonalities: ',Seasonalities,'\n')
    print('Forecasts: ',Forecasts,'\n')
    return Levels,Seasonalities,Forecasts,T

def moving_avg_method(Dt,N,init): #init is the n of periods used for initialization
    Levels=[]
    curr=-1
    for x in range(len(Dt)-init+1):
        avg=sum(Dt[init+curr:(init+curr)-N:-1])/N
        Levels.append(avg)
        curr+=1
    print(f"Levels (and forecasts as well): {Levels}")

def Brown_method(Dt,a,N,init):
    val=(Dt[init-1:init-N-1:-1])
    if len(val)==0:
        val=Dt[0:init]
    first_avg=sum(val)/N
    Levels=[first_avg]
    Forecasts=[0 for x in range(init)]
    Forecasts.append(int(Levels[0]))
    for t in range(len(Dt)-1):
        Lt=(a*Dt[t+init])+(1-a)*Levels[-1]
        Levels.append(Lt)
        print(Lt)
        Forecasts.append(int(Lt))

def Holt_method(data,n,alpha,beta):
    data_1=data[0:5] #set 0:n_initializing data
    model=linear_regression([x for x in range(1,len(data_1)+1)],data_1)
    a=round(model[0],2)
    b=round(model[1],2)
    levels=[a+(x*b) for x in range(n+1)]
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

def Winters_method(data_init,data_forecast,p,alpha,beta,gamma):
    levels,seasonalities,forecasts,T=static_method(data_init,p)
    data=data_init+data_forecast
    trends=[T]
    for x in range(len(data_init),len(data_init)+len(data_forecast)):
        forecast=(levels[-1]+trends[-1])*seasonalities[x]
        forecasts.append(forecast)
        level=(alpha*(data[x]/seasonalities[x]))+(1-alpha)*(levels[-1]+trends[-1])
        trend=(beta*(level-levels[-1]))+(1-beta)*trends[-1]
        seasonality=(gamma*(data[x]/level))+(1-gamma)*seasonalities[x]
        levels.append(level)
        trends.append(trend)
        seasonalities.append(seasonality)
    print("----------------------------------------------\n")
    print("Levels: ",levels)
    print("\nTrends: ",trends)
    print("\nSeasonalities: ",seasonalities)
    print("\nForecasts: ",forecasts)

#test
Dt_brown=[130,104,122,143,107,133,125,139,183,172,168,182]
Dt_holt=[97,118,107,145,141,128,135,216,245,360,400,460]
Dt_static=[4000,6500,11500,17000,5000,9000,11500,19000,6000,6500,16000,20500]
Dt_winters=[4800,7400,10500,16000,3900,7500,11000]

Winters_method(Dt_static,Dt_winters,4,alpha=0.2,beta=0.8,gamma=0.1)
