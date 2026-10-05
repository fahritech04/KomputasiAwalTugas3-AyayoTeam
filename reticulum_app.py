# Mengimpor library Reticulum
import RNS

# Menentukan nama aplikasi
APP_NAME = "tugas3_ayayoteam"

# Menentukan aspect dari destination
ASPECTS = ("identity",)


# Membuat fungsi untuk mencetak judul bagian
def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# Membuat fungsi utama program
def main():

    # Inisialisasi Reticulum
    reticulum = RNS.Reticulum()

    # Membuat Identity baru
    identity = RNS.Identity()

    # Membuat Destination berdasarkan Identity
    destination = RNS.Destination(
        identity,
        RNS.Destination.IN,
        RNS.Destination.SINGLE,
        APP_NAME,
        *ASPECTS
    )

    # Menampilkan identitas
    print_section("IDENTITY")

    print("Identity hash:")
    print(identity.hash.hex())

    print("\nPrivate encryption key (X25519):")
    print(identity.prv_bytes.hex())

    print("\nPublic encryption key (X25519):")
    print(identity.pub_bytes.hex())

    print("\nPrivate signing key (Ed25519):")
    print(identity.sig_prv_bytes.hex())

    print("\nPublic signing key (Ed25519):")
    print(identity.sig_pub_bytes.hex())

    # Menampilkan informasi destination
    print_section("DESTINATION")

    print("Destination hash:")
    print(destination.hash.hex())

    print("\nParameter:")
    print("Identity     :", identity.hash.hex())
    print("Direction    :", "IN" if destination.direction == RNS.Destination.IN else "OUT")
    print("Type         :", "SINGLE" if destination.type == RNS.Destination.SINGLE else "GROUP")
    print("App name     :", APP_NAME)
    print("Aspects      :", ", ".join(ASPECTS))
    print("Full name    :", destination.name)


# Menjalankan fungsi main
if __name__ == "__main__":
    main()
