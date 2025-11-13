import colander
import deform.widget
from pyramid.view import view_config

# 1. Membuat Aturan Formulir (Schema)
class WikiPage(colander.MappingSchema):
    # Kolom Judul (Wajib isi, tipe String)
    title = colander.SchemaNode(colander.String(), title='Judul Halaman')
    
    # Kolom Isi (Wajib isi, tipe String, bentuknya Kotak Besar/TextArea)
    body = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.TextAreaWidget(rows=10),
        title='Isi Halaman'
    )

# 2. Logic Tampilan
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='wiki', renderer='wiki.pt')
    def wiki_view(self):
        schema = WikiPage()
        # Membuat objek Form dari Schema di atas
        form = deform.Form(schema, buttons=('submit',))

        # --- JIKA TOMBOL SUBMIT DITEKAN (POST) ---
        if 'submit' in self.request.POST:
            controls = self.request.POST.items()
            try:
                # Cek validasi (Apakah data sesuai aturan?)
                appstruct = form.validate(controls)
                
                # Jika SUKSES: Tampilkan formulir dalam mode "Read Only" (Hanya baca)
                # dan kirim data yang diinput user
                return {
                    'form': form.render(appstruct, readonly=True), 
                    'values': appstruct,
                    'message': 'Sukses! Data valid.'
                }
            
            except deform.ValidationFailure as e:
                # Jika GAGAL: Tampilkan formulir lagi beserta pesan error merahnya
                return {'form': e.render(), 'values': None, 'message': ''}

        # --- JIKA BARU BUKA HALAMAN (GET) ---
        # Tampilkan formulir kosong
        return {'form': form.render(), 'values': None, 'message': ''}