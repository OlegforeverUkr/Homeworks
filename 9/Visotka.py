def entrance_floor_flat(number, etazhey, kv_etazh):
    kv_podiezd = etazhey * kv_etazh
    podiezd = (number - 1) // kv_podiezd + 1
    etazh = ((number - 1) % kv_podiezd) // kv_etazh + 1
    return f'Подьезд - {podiezd}, Этаж - {etazh}'


r = entrance_floor_flat(5, 5, 4)
print(r)
