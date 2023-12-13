def banner():
    print("\n \n")

    print("@@@@   @@@@@   @@  @  @   @")
    print("@   @  @   @   @ @ @   @ @")
    print("@   @  @   @   @  @@    @")
    print("@@@@   @@@@@   @   @    @")

    print("\n \n")


def input_nama():
    while True:
        nama = input("Nama : ")
        if nama.isdigit() or not nama.isalpha():
            print("Masukkan nama yang valid!")
        else:
            return nama

def input_jam_kerja(nama):
    while True:
        jam_kerja = input("Jam masuk kerja : ")
        if not ":" in jam_kerja:
            print("Jam Tidak Valid!")
        else:
            jam, menit = map(int, jam_kerja.split(":"))
            masuk_jam_kerja = jam + menit / 60

            if 1.00 <= masuk_jam_kerja < 24.00:
                print_sapaan(masuk_jam_kerja, nama)
                return masuk_jam_kerja
            else:
                print("Jam masuk kerja tidak valid!")

def input_jam_keluar_kerja():
    while True:
        jam_keluar_kerja = input("Jam keluar kerja : ")
        if not ":" in jam_keluar_kerja:
            print("Jam keluar kerja tidak valid!")
        else:
            jam, menit = map(int, jam_keluar_kerja.split(":"))
            keluar_jam_kerja = jam + menit / 60

            if 1.00 <= keluar_jam_kerja < 24.00:
                print_sapaan(keluar_jam_kerja)
                return keluar_jam_kerja
            else:
                print("Jam keluar kerja tidak valid!")

def print_sapaan(jam_kerja, nama=""):
    if 6.00 <= jam_kerja < 12.00:
        waktu_sapaan = "Selamat pagi"
    elif 12.00 <= jam_kerja < 15.00:
        waktu_sapaan = "Selamat siang"
    elif 15.00 <= jam_kerja < 18.00:
        waktu_sapaan = "Selamat sore"
    else:
        waktu_sapaan = "Selamat malam"

    if nama:
        print(f"\n{waktu_sapaan} {nama}\n")
    else:
        print(f"\n{waktu_sapaan}\n")

def hitung_gaji(nama, masuk_jam_kerja, keluar_jam_kerja):
    gaji_perhari = 175000
    waktu_kerja = keluar_jam_kerja - masuk_jam_kerja

    jam_kerja = int(waktu_kerja)
    menit_kerja = int((waktu_kerja - jam_kerja) * 60)

    print(f"===Rincian Gaji===\n")
    print(f"Nama : {nama}")
    print(f"Waktu Kerja = {jam_kerja} jam, {menit_kerja} menit")
    if waktu_kerja <= 8:
        gaji_total = gaji_perhari
    else:
        gaji_tambahan = (jam_kerja - 8) * 15000
        gaji_total = gaji_perhari + gaji_tambahan

        print(f"Gaji perhari : Rp.{gaji_perhari}")
        print(f"Lembur : Rp.{gaji_tambahan} ({jam_kerja - 8} jam * Rp.15,000)")
    print(f"Gaji Total: Rp.{gaji_total}")

def main():
    while True:
        banner()
        nama = input_nama()
        masuk_jam_kerja = input_jam_kerja(nama)
        keluar_jam_kerja = input_jam_keluar_kerja()
        hitung_gaji(nama, masuk_jam_kerja, keluar_jam_kerja)

        ulangi = input("Ulangi Proses? (y/n) : ").lower()
        if ulangi not in ('yes', 'y'):
            print("Terimakasih <3")
            break

if __name__ == "__main__":
    main()
