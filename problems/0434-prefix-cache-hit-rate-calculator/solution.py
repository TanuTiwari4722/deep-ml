def prefix_cache_hit_rate(prompts: list, cache: list) -> dict:
    """
    Calculate the prefix cache hit rate for a batch of tokenized prompts.

    Args:
        prompts: List of tokenized prompts (list of list of ints).
        cache: List of cached prefixes (list of list of ints).

    Returns:
        Dictionary with 'hit_rate', 'cached_tokens', and 'total_tokens'.
    """
    # Your code here
    total_tokens = 0
    cached_tokens = 0
    for prompt in prompts:
        total_tokens = total_tokens + len(prompt)

        max_match_len = 0
        for prefix in cache:
            if len(prefix) <= len(prompt) and prompt[:len(prefix)]== prefix:
                max_match_len = max(max_match_len, len(prefix))
        cached_tokens = cached_tokens + max_match_len
    if total_tokens == 0:
        hit_rate = 0.0
    else:
        hit_rate = cached_tokens/total_tokens
    return {
        'hit_rate': round(float(hit_rate), 4),
        'cached_tokens': cached_tokens,
        'total_tokens': total_tokens
    }


    