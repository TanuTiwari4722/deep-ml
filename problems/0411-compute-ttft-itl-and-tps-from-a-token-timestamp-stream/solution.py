def compute_inference_metrics(timestamps: list[float]) -> dict:
	"""
	Compute LLM inference performance metrics from token timestamps.
	
	Args:
		timestamps: List of floats where timestamps[0] is the request start time
		            and timestamps[1:] are the times when each output token was generated.
	
	Returns:
		Dictionary with keys 'ttft', 'tps', 'itl' containing the metric values.
	"""
	if len(timestamps) < 2:
		raise ValueError("Timestamps should be more than two")
	start_time = timestamps[0]
	token_times = timestamps[1:]

	#ttft
	ttft = token_times[0] - start_time

	#tps
	total_tokens = len(token_times)
	total_time = token_times[-1] - start_time
	tps = total_tokens/total_time if total_time > 0 else 0.0

	#itl
	if total_tokens <=1:
		itl = 0.0
	else:
		gaps = []
		for i in range(1, total_tokens):
			gap = token_times[i] - token_times[i-1]
			gaps.append(gap)
		itl = sum(gaps)/len(gaps)

	return {
        'ttft': round(float(ttft), 4),
        'tps': round(float(tps), 4),
        'itl': round(float(itl), 4)
    }

