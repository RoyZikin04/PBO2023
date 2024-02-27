import flet as ft

def main(page):
    page.title = "Calculator Discount"
    page.padding = 35
    page.window_width = 418.0
    page.window_height = 371.0
    page.scroll = ft.ScrollMode.AUTO
    
    
    def btn_click(e):
        harga_barang.error_text = None
        jumlah_diskon.error_text = None
        
        if not harga_barang.value:
            harga_barang.error_text = "Mohon masukkan nilai!"
            page.update()
        elif not jumlah_diskon.value:
            jumlah_diskon.error_text = "Mohon masukkan nilai!"
            page.update()
        elif int(jumlah_diskon.value) == 100:
            page.add(ft.Text(f"Barang gratis"))
        else:
            harga_barang.value = int(harga_barang.value)
            jumlah_diskon.value = int(jumlah_diskon.value)
            rumus = harga_barang.value - (harga_barang.value * jumlah_diskon.value/100)
            rupiah = "{:,}".format(rumus)
            page.update()
            
            if jumlah_diskon.value > 0 and jumlah_diskon.value <= 100:
                page.add(ft.Text(f"Harga setelah di diskon adalah, Rp. {rupiah}"))
            else:
                jumlah_diskon.error_text = "Masukkan jumlah diskon dari 1-100 !"
                page.update()


    harga_barang = ft.TextField(
        label="Harga barang", 
        prefix_text="Rp ", 
        keyboard_type= ft.KeyboardType.NUMBER
        )
    jumlah_diskon = ft.TextField(
        label="Jumlah diskon", 
        suffix_text="%", 
        keyboard_type= ft.KeyboardType.NUMBER
        )
    page.add(harga_barang, jumlah_diskon, ft.ElevatedButton("hitung!", on_click=btn_click))


ft.app(main)