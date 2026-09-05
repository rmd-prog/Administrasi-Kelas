from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Pengaturan latar belakang
Window.clearcolor = (0.95, 0.96, 0.98, 1)

class MenuUtama(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Header Aplikasi
        header = Label(
            text="PUSAT ADMINISTRASI KELAS SD\n(Versi Kurikulum Merdeka & Deep Learning)",
            font_size='18sp',
            bold=True,
            color=(0.1, 0.2, 0.4, 1),
            halign='center',
            size_hint_y=None,
            height=60
        )
        layout.add_widget(header)

        # Container Tombol Utama (Grid 2 Kolom)
        scroll = ScrollView()
        grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        daftar_menu = [
            ("📘 RPM (Deep Learning)", "rpm"),
            ("🎯 Capaian Pembelajaran (CP)", "cp"),
            ("🗺️ Alur Tujuan (ATP)", "atp"),
            ("📅 Program Tahunan (Prota)", "prota"),
            ("📆 Program Semester (Prosem)", "prosem"),
            ("📝 Modul Ajar / RPP", "modul"),
            ("📊 Jurnal & Presensi", "jurnal"),
            ("📈 Pengolahan Nilai & Rapor", "nilai"),
            ("💼 Admin Penunjang Guru", "penunjang"),
            ("⚙️ Informasi Sekolah", "info")
        ]

        for text, screen_name in daftar_menu:
            btn = Button(
                text=text,
                size_hint_y=None,
                height=70,
                background_color=(0.2, 0.5, 0.8, 1),
                color=(1, 1, 1, 1),
                bold=True
            )
            btn.bind(on_release=lambda x, sc=screen_name: setattr(self.manager, 'current', sc))
            grid.add_widget(btn)

        scroll.add_widget(grid)
        layout.add_widget(scroll)
        self.add_widget(layout)

class HalamanDetail(Screen):
    def __init__(self, judul, poin_isi, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Title
        layout.add_widget(Label(
            text=judul,
            font_size='18sp',
            bold=True,
            color=(0.1, 0.2, 0.4, 1),
            size_hint_y=None,
            height=40
        ))

        # Content List
        scroll = ScrollView()
        box_isi = BoxLayout(orientation='vertical', spacing=8, size_hint_y=None)
        box_isi.bind(minimum_height=box_isi.setter('height'))

        for poin in poin_isi:
            lbl = Label(
                text=poin,
                color=(0.2, 0.2, 0.2, 1),
                size_hint_y=None,
                height=40,
                halign='left',
                valign='middle'
            )
            lbl.bind(size=lbl.setter('text_size'))
            box_isi.add_widget(lbl)

        scroll.add_widget(box_isi)
        layout.add_widget(scroll)

        # Tombol Kembali
        btn_back = Button(
            text="⬅️ Kembali ke Menu Utama",
            size_hint_y=None,
            height=50,
            background_color=(0.8, 0.2, 0.2, 1),
            bold=True
        )
        btn_back.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_back)

        self.add_widget(layout)

class AplikasiAdministrasiKelas(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuUtama(name='menu'))

        # Data Struktur Administrasi
        data_admin = {
            "rpm": ("Rancangan Pembelajaran Mindful (Deep Learning)", [
                "• Pendekatan Deep Learning: Mindful, Meaningful, Joyful",
                "• Pemetaan Kebutuhan & Kesiapan Belajar Murid",
                "• Kerangka Pembelajaran Konstruktif & Kontekstual",
                "• Refleksi Diri & Integrasi Karakter Pancasila"
            ]),
            "cp": ("Capaian Pembelajaran (CP) SD", [
                "• Dokumen CP Bahasa Indonesia (Fase A, B, C)",
                "• Dokumen CP Matematika (Fase A, B, C)",
                "• Dokumen CP IPAS (Fase B, C)",
                "• Dokumen CP PPKn & Seni Budaya"
            ]),
            "atp": ("Alur Tujuan Pembelajaran (ATP)", [
                "• Pemetaan Elemen & Sub-Elemen Materi",
                "• Urutan Tujuan Pembelajaran Sistematis",
                "• Alokasi Jam Pelajaran (JP) Per Minggu",
                "• Pemetaan Asesmen Awal & Akhir"
            ]),
            "prota": ("Program Tahunan (Prota)", [
                "• Pemetaan Alokasi Waktu Efektif 1 Tahun Ajaran",
                "• Distribusi Alokasi JP Per Bab / Elemen",
                "• Integrasi Jam Projek P5",
                "• Jadwal Cadangan Asesmen Sumatif"
            ]),
            "prosem": ("Program Semester (Prosem)", [
                "• Matriks Kalender Pendidikan Semester 1 & 2",
                "• Distribusi Jam Efektif Mingguan",
                "• Pemetaan Waktu Ujian Tengah & Akhir Semester",
                "• Agenda Kegiatan Khusus Sekolah"
            ]),
            "modul": ("Modul Ajar / RPP Integratif", [
                "• Identitas & Komponen Umum Modul",
                "• Langkah Pembelajaran (Pendahuluan, Inti, Penutup)",
                "• Lembar Kerja Peserta Didik (LKPD)",
                "• Rubrik Asesmen Diagnostik, Formatif, & Sumatif"
            ]),
            "jurnal": ("Jurnal Harian & Presensi Kelas", [
                "• Catatan Harian Pelaksanaan Pembelajaran",
                "• Rekapitulasi Kehadiran Siswa (Sakit, Izin, Alfa)",
                "• Catatan Kejadian Khusus / Pembiasaan",
                "• Dokumentasi Kegiatan Kelas"
            ]),
            "nilai": ("Pengolahan Nilai & Rapor", [
                "• Input Nilai Formatif (Harian)",
                "• Input Nilai Sumatif (Materi / Semester)",
                "• Pengolahan Deskripsi Capaian Kompetensi",
                "• Rekapitulasi Rapor Kurikulum Merdeka"
            ]),
            "penunjang": ("Administrasi Penunjang Guru", [
                "• Jadwal Pelajaran & Piket Kelas",
                "• Buku Inventaris Barang Kelas",
                "• Denah Tempat Duduk Siswa",
                "• Data Bimbingan Konseling (BK) & Keluhan Siswa",
                "• Daftar Hubungan Orang Tua / Wali Siswa"
            ]),
            "info": ("Identitas Sekolah & Pengaturan", [
                "• Nama Sekolah & Alamat Lengkap",
                "• Nama Kepala Sekolah & NIP",
                "• Nama Guru Kelas & NIP",
                "• Tahun Ajaran Running & Semester"
            ])
        }

        for key, (judul, isi) in data_admin.items():
            sm.add_widget(HalamanDetail(judul=judul, poin_isi=isi, name=key))

        return sm

if __name__ == '__main__':
    AplikasiAdministrasiKelas().run()
