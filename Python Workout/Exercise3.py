def run_timing():
    run_count = 0
    total_time = 0
    while True:
        user_input = input("Enter the time for the run in minutes or press Enter to finish: ")
        if not user_input:
            break
        try:
            run_time = float(user_input)
        except ValueError:
            print("Invalid input, please try a valid number.")
            continue
        total_time += run_time
        run_count += 1
    if run_count > 0:
        return f"The average time the distance was traveled in is {total_time / run_count} minutes!"
    else:
        return "Nothing was found"


print(run_timing())
