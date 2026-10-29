import speedtest


def check_internet_speed():
    #The function measures download speed, upload speed 
    #and ping (latency), then prints the results
    
    speed_test = speedtest.Speedtest()
    
    print("Testing speed...")