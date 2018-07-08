def convertRunHr(runHr):
    hr_list = runHr.split('h')
    hr = int(hr_list[0])

    min_list = hr_list[1].split('m')
    min = int(min_list[0])

    totalHr = hr + min/60
    return totalHr

run_hour = input("Enter run hour of genset (eg. 30h20m): ")

print(convertRunHr(run_hour))
