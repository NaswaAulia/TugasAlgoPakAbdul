# while True : karena supaya prosesnya bisa di loop
while True:
    #input nama  
    nama = input("Nama : ")

    #jika nama itu angka maka nama tidak valid
    if nama.isdigit():
        print("Masukkan nama yang valid!")
        #akan mengulangi proses kembali ke input variabel "nama"
        continue

    #ketika nama benar maka proses kalkulasi akan berjalan
    while nama.isalpha():
        
        #input jam masuk kerja memakai string
        jamKerja = (input("Jam masuk kerja [contoh 06:30]: "))

        #jika di string jamKerja tidak ada ":"
        if not ":" in jamKerja:
            print("Jam Tidak Valid!")
            #akan mengulangi proses kembali ke input variabel "jamKerja"
            continue
        
        #konversi variabel "jamKerja" dari string menjadi int

        #kenapa saya konversi?, karena nanti jam masuk kerja akan digunakan dalam perhitungan juga
        jam, menit = map(int, jamKerja.split(":"))

        #nilai jam untuk penghitungan matematika
        masukJamKerja = jam + menit / 60

        # Gaji perhari
        gajiPerhari = 175000

        # Mengecek apakah jam kerja valid (antara 0 hingga 24)
        if masukJamKerja <= 1.00 or masukJamKerja >= 24.00:
                print("Jam masuk kerja tidak valid!")
                #jika jam kerja tidak valid maka program akan kembali ke input jam
                continue
                
        else:
                # Ucapan selamat pagi, siang, sore, malam berdasarkan waktu
                if masukJamKerja >= 6.00 and masukJamKerja <= 12.00:
                    print(f"\nSelamat pagi {nama}\n")
                elif masukJamKerja >= 12.00 and masukJamKerja <= 15.00:
                    print(f"\nSelamat siang {nama}\n")
                elif masukJamKerja >= 15.00 and masukJamKerja <= 18.00:
                    print(f"\nSelamat sore {nama}\n")
                elif masukJamKerja >= 18.00 and masukJamKerja <= 24.00:
                    print(f"\nSelamat malam {nama}\n")
                else:
                    print("Jam masuk kerja tidak valid!")
        break #berhentinya loop

    #while True karena kita ingin membuat proses loop juga di dalam sini
    while True:            
        # Input jam keluar kerja menggunakan string, sama seperti yang di atas
        jamKeluarKerja = (input("Jam keluar kerja [contoh untuk 18:30]: "))
        if not ":" in jamKeluarKerja:
            print("Jam keluar kerja tidak valid!")
            # jika input tidak valid program akan kembali ke input variabel jamKeluarKerja
            continue

        #sama seperti yang di atas, ini adalah untuk mengkonversi jamKeluarKerja menjadi integer
        #supaya bisa digunakan dalam perhitungan matematika
        jam1, menit1 = map(int, jamKeluarKerja.split(":"))

        #ini untuk perhitungan matematika
        keluarJamKerja = jam1 + menit1 / 60

        # Mengecek apakah jam keluar kerja valid (antara 0 hingga 24)
        if keluarJamKerja < 1.00 or keluarJamKerja > 24.00:
            print("Jam keluar kerja tidak valid!")

        # kondisi jika jam keluar kerja == valid
        else:
            # Ucapan selamat pagi, siang, sore, malam berdasarkan waktu
            if keluarJamKerja >= 6.00 and keluarJamKerja <= 12.00:
                print(f"\nSelamat pagi\n")
            elif keluarJamKerja >= 12.00 and keluarJamKerja <= 15.00:
                print(f"\nSelamat siang\n")
            elif keluarJamKerja >= 15.00 and keluarJamKerja <= 18.00:
                print(f"\nSelamat sore\n")
            elif keluarJamKerja >= 18.00 and keluarJamKerja <= 24.00:
                print(f"\nSelamat malam\n")
            else:
                #kondisi jika jam keluar kerja tidak valid
                print("Jam keluar kerja tidak valid!")

        print(5 * "-", "Rincian gaji", 5 * "-")
        #print nama
        print(f"Nama : {nama}")

        #ini perhitungan untuk berapa lama kita bekerja
        waktuKerja = (keluarJamKerja - masukJamKerja)

        #ini adalah 2 variabel untuk memecah waktuKerja menjadi format jam & menit
        jam3 = int(waktuKerja)
        menit3 = int((waktuKerja - jam3) * 60)

        #print waktu kerja
        print(f"Waktu Kerja = {int(waktuKerja)} jam, {menit3} menit ({jamKerja} s.d {jamKeluarKerja})")

        #kemungkinan jika waktu kerja kurang dari 8 jam
        if waktuKerja <= 8:
            gaji_total = gajiPerhari
            print(f"Gaji Total: Rp.{gaji_total}")
        
        #kemungkinan jika waktu kerja lebih dari 8 jam
        else:
            gaji_tambahan = (int(waktuKerja) - 8) * 15000
            gaji_total = gajiPerhari + gaji_tambahan

            print(f"Gaji perhari : Rp.{gajiPerhari}")
            print(f"Lembur : Rp.{gaji_tambahan} ({int(waktuKerja - 8)} jam * Rp.15,000)")
            print(f"Gaji Total: Rp.{gaji_total}")
            break #break loop 

    #input untuk opsi ulangi proses program atau tidak
    while True:
        ulangi = input("Ulangi Proses? (y/n) : ")
        if len(ulangi) <= 1:
            print("opsi tidak valid")
            continue
        else:
            break
    
    #jika input bukan y maka program akan terhenti
    if ulangi.lower() != "y":
        print("Terimakasih <3")
        break #akhir dari loop
