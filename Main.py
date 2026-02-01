from geo_service import get_coordinates
from weather_service import get_weather_data

def ana_program():
    print("--- Hava Durumu Analizörüne Hoş Geldiniz ---")
    sehir = input("Hava durumunu öğrenmek istediğiniz şehri yazın: ").strip()

    konum = get_coordinates(sehir)

    if konum:
        print(f"\n{konum['name']} ({konum['country']}) bulundu...")

        hava = get_weather_data(konum['lat'], konum['lon'])

        if hava:
            sicaklik = hava['temperature']
            ruzgar = hava['windspeed']
            print(f"Sıcaklık: {sicaklik}°C")
            print(f"Rüzgar Hızı: {ruzgar} km/sa")
            
  
            if sicaklik < 10:
                print("Tavsiye: Hava oldukça soğuk, sıkı giyinin!")
            elif sicaklik > 25:
                print("Tavsiye: Hava sıcak, bol su içmeyi unutmayın.")
        else:
            print("Hava durumu bilgisi alınamadı.")
    else:
        print("Şehir bulunamadı. Lütfen ismi doğru yazdığınızdan emin olun.")

if __name__ == "__main__":
    ana_program()