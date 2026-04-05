def log_inference_time(time_taken):
    with open("logs/app.log", "a") as f:
        f.write(f"Inference time: {time_taken}\n")