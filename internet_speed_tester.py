import speedtest


def check_internet_speed():
    #The function measures download speed, upload speed 
    #and ping (latency), then prints the results
    
    speed_test = speedtest.Speedtest()
    
    print("Testing speed...")

    download = speed_test.download() / 1_000_000
    upload = speed_test.upload() / 1_000_000

    speed_test.get_best_server()
    ping = speed_test.results.ping
    return {
        "download": round(download, 2),
        "upload": round(upload, 2),
        "ping": round(ping, 2)
    }