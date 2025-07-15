def generate_unique_email(prefix='test'):
    """Генерирует уникальный email"""
    import random
    suffix = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(5))
    return f"{prefix}_{suffix}@example.com"