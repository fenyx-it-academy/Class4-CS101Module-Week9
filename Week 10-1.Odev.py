import heapq
from heapq import heappush, heappop

def dusuk_maliyet(fiyat):
    heapq.heapify(fiyat)
    maliyet = 0

    while len(fiyat) > 1:
        x = heappop(fiyat)
        y = heappop(fiyat)
        toplam = x + y
        heappush(fiyat, toplam)
        maliyet += toplam
    return maliyet
if __name__ == '__main__':
    fiyat = [5, 4, 2, 8]
    print("En Dusuk Maliyet:", dusuk_maliyet(fiyat))