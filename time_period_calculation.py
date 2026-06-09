def time_period_length(time_period):
    # TODO: implement the function
    result = []
    single_time = [(part) for part in time_period.split("-")]
    start_time = single_time[0]
    end_time = single_time[1]
    sh, sm, ss = [int(x) for x in start_time.split(":")]
    eh, em, es = [int(x) for x in end_time.split(":")]

    start_seconds = sh * 3600 + sm * 60 + ss
    end_seconds = eh * 3600 + em * 60 + es

    return (end_seconds // 60) - (start_seconds // 60)