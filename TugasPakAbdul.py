# Input nama
nama = input("Nama : ")

while not nama.isalpha():
    print("Masukkan nama yang valid!")
    nama = input("Nama : ")

while True:
    # Input jam kerja
    jamKerja = float(input("Jam masuk kerja (jam.menit)[contoh 6.30 untuk 06:30]: "))

    # Gaji perhari
    gajiPerhari = 175000

    # Mengecek apakah jam kerja valid (antara 0 hingga 24)
    if jamKerja < 0.00 or jamKerja > 24.00:
        print("Jam masuk kerja tidak valid!")
    else:
        # Ucapan selamat pagi, siang, sore, malam berdasarkan waktu
        if jamKerja >= 6.00 and jamKerja <= 12.00:
            print(f"\nSelamat pagi {nama}\n")
        elif jamKerja >= 12.00 and jamKerja <= 15.00:
            print(f"\nSelamat siang {nama}\n")
        elif jamKerja >= 15.00 and jamKerja <= 18.00:
            print(f"\nSelamat sore {nama}\n")
        elif jamKerja >= 18.00 and jamKerja <= 24.00:
            print(f"\nSelamat malam {nama}\n")
        else:
            print("Jam masuk kerja tidak valid!")

        # Input jam keluar kerja
        jamKeluarKerja = float(input("Jam keluar kerja (jam.menit)[contoh 18.30 untuk 18:30]: "))

        # Mengecek apakah jam keluar kerja valid (antara 0 hingga 24)
        if jamKeluarKerja < 0.00 or jamKeluarKerja > 24.00:
            print("Jam keluar kerja tidak valid!")
        else:
            # Ucapan selamat pagi, siang, sore, malam berdasarkan waktu
            if jamKeluarKerja >= 6.00 and jamKeluarKerja <= 12.00:
                print(f"\nSelamat pagi\n")
            elif jamKeluarKerja >= 12.00 and jamKeluarKerja <= 15.00:
                print(f"\nSelamat siang\n")
            elif jamKeluarKerja >= 15.00 and jamKeluarKerja <= 18.00:
                print(f"\nSelamat sore\n")
            elif jamKeluarKerja >= 18.00 and jamKeluarKerja <= 24.00:
                print(f"\nSelamat malam\n")
            else:
                print("Jam keluar kerja tidak valid!")

            print(5 * "-", "Rincian gaji", 5 * "-")

            print(f"Nama : {nama}")

            waktuKerja = (jamKeluarKerja - jamKerja)

            print(f"Waktu Kerja = {int(waktuKerja)} jam ({jamKerja:.2f} s.d {jamKeluarKerja:.2f})")

            if waktuKerja <= 8:
                gaji_total = gajiPerhari
            else:
                gaji_tambahan = (int(waktuKerja) - 8) * 15000
                gaji_total = gajiPerhari + gaji_tambahan

            print(f"Gaji perhari : {gajiPerhari}")
            print(f"Lembur : {gaji_tambahan:.2f} ({int(waktuKerja - 8)} jam * Rp.15,000)")
            print(f"Gaji Total: {gaji_total:.2f}")

    break
